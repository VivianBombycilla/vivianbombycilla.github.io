import os
import frontmatter, markdown
import jinja2 as j2
import pandas as pd

# Get blog posts
paths = list(filter(lambda path: path.endswith(".md"),os.listdir("blog")))

def parse_blog_posts(paths):
    '''Parses a list of paths into a DataFrame'''
    df = pd.DataFrame()
    # For each path, extract the frontmatter and content and combine them into a Series, which is then concatenated into the DataFrame df.
    for path in paths:
        with open("blog/"+path) as f:
            post = frontmatter.loads(f.read(), **{"work-in-progress":False})
            post_dict = post.to_dict()
            sr = pd.Series(post_dict)
            df = pd.concat([df,sr],axis=1,ignore_index=True)
    df = df.transpose() # Transpose the DataFrame (important before any further actions)
    df.index = df["post-id"] # Declare new index
    df["content"] = df["content"].apply(markdown.markdown) # Parse the markdown
    df["link"] = df["post-id"].apply(get_link) # Create links
    df.sort_index(axis=0,inplace=True,ascending=False) # Sort the DataFrame
    return df

def get_link(post_id):
    '''Gets link to post from post id'''
    return "/blog/"+str(post_id)+".html"

def filter_posts(posts,filter_by,category):
    '''Filter a list of posts'''
    filtered_posts = [post for post in posts if post[filter_by] == category]
    return filtered_posts

df = parse_blog_posts(paths)
posts = list(map(lambda x: x[1],df.iterrows()))
posts = filter_posts(posts,"work-in-progress",False)

# Load Jinja environment
env = j2.Environment(
    loader = j2.FileSystemLoader("templates"),
    autoescape = j2.select_autoescape()
)

# write to blog.html
template = env.get_template("blog-template.jinja")
with open("public/blog.html","w") as f:
    f.write(template.render(blog_posts = posts))

# # write to games.html
# template = env.get_template("games-template.jinja")
# with open("public/games.html","w") as f:
#     f.write(template.render(blog_posts = filter_posts(posts,"category","games")))

# write blog post pages
template = env.get_template("blog-post-template.jinja")
for i in range(len(posts)):
    post = posts[i]
    prev_post = None
    next_post = None
    if i > 0:
        next_post = posts[i-1]
    if i < len(posts)-1:
        prev_post = posts[i+1]
    with open("public/"+post["link"],"w") as f:
        f.write(template.render(
            blog_post = post,
            prev_post = prev_post,
            next_post = next_post
        ))
