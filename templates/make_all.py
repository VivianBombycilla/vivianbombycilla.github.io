import os
import frontmatter
import markdown
import jinja2 as j2
import pandas as pd

# Get blog posts
paths = list(filter(lambda path: path.endswith(".md"),os.listdir("blog")))
book_paths = list(filter(lambda path: path.endswith(".md"),os.listdir("reading")))

nav_menu = [
    {"link": "/", "title": "Home", "index": "index"},
    {"link": "/blog.html", "title": "Blog", "index": "blog"},
    {"link": "/reading.html", "title": "Reading", "index": "reading"},
]

def parse_blog_posts(paths, directory):
    '''Parses a list of paths into a DataFrame.'''
    df = pd.DataFrame()
    # For each path, extract the frontmatter and content and combine them into a Series, which is then concatenated into the DataFrame df.
    for path in paths:
        with open(directory + path, encoding="utf-8") as f:
            # Extract frontmatter and content into a frontmatter.Post object
            post = frontmatter.loads(f.read())
            # Convert Post to dictionary for handling using pandas
            post_dict = post.to_dict()
            # Initializes pd.Series object with the data from the dictionary
            sr = pd.Series(post_dict)
            # Adds sr to df, as a new column
            df = pd.concat([df,sr],axis=1,ignore_index=True)
    # We want each post to be a row, rather than a column, therefore we transpose the DataFrame.
    df = df.transpose()
    # Parse markdown in the content of each post.
    df["content"] = df["content"].apply(lambda text: markdown.markdown(text,extensions = ["tables"]))
    return df

def get_link(post_id):
    '''Gets link to post from post id'''
    return "/blog/posts/"+str(post_id)+".html"

def filter_posts(posts,filter_by,category):
    '''Filter a list of posts'''
    filtered_posts = [post for post in posts if post[filter_by] == category]
    return filtered_posts

def parse_authors(author_list):
    return ", ".join(author_list)

# Parse all blog posts into a DataFrame.
df = parse_blog_posts(paths,"blog/")
df.index = df["post-id"] # Declare new index
df["link"] = df["post-id"].apply(get_link) # Create links
df.sort_index(axis=0,inplace=True,ascending=False) # Sort the DataFrame

posts = list(map(lambda x: x[1],df.iterrows()))
posts = filter_posts(posts,"published",True)

books_df = parse_blog_posts(book_paths,"reading/")
print(books_df)
books_df.index = books_df["book-id"] # Declare new index
books_df.sort_index(axis=0,inplace=True,ascending=False) # Sort the DataFrame
books_df["author"] = books_df["author"].apply(parse_authors)
books = list(map(lambda x: x[1],books_df.iterrows()))
books_read = filter_posts(books,"status","read")
books_reading = filter_posts(books,"status","reading")

# Load Jinja environment
env = j2.Environment(
    loader = j2.FileSystemLoader("templates"),
    autoescape = j2.select_autoescape()
)

# get navbar
template = env.get_template("navbar.jinja")
navbar_index = template.render(nav_menu = nav_menu,current_page = "index")
navbar_blog = template.render(nav_menu = nav_menu,current_page = "blog")
navbar_reading = template.render(nav_menu = nav_menu,current_page = "reading")

# write to blog.html
template = env.get_template("blog.jinja")
with open("public/blog.html","w",encoding="utf-8") as f:
    f.write(template.render(blog_posts = posts,navbar=navbar_blog))

# write to index.html
template = env.get_template("index.jinja")
with open("public/index.html","w",encoding="utf-8") as f:
    f.write(template.render(latest_post = posts[0],navbar=navbar_index))

# write to reading.html
template = env.get_template("reading.jinja")
with open("public/reading.html","w",encoding="utf-8") as f:
    f.write(template.render(
        books_read = books_read,
        books_reading = books_reading,
        navbar = navbar_reading
    ))

# write blog post pages
template = env.get_template("blog-post.jinja")
for i in range(len(posts)):
    post = posts[i]
    prev_post = None
    next_post = None
    if i > 0:
        next_post = posts[i-1]
    if i < len(posts)-1:
        prev_post = posts[i+1]
    with open("public/"+post["link"],"w",encoding="utf-8") as f:
        f.write(template.render(
            blog_post = post,
            prev_post = prev_post,
            next_post = next_post,
            navbar = navbar_blog
        ))

print("test")