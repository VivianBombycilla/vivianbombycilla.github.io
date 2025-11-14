from make_navbars import *

# Get list of paths to posts
paths = list(filter(lambda path: path.endswith(".md"),os.listdir("blog")))

def get_link(post_id):
    '''Gets link to post from post id'''
    return "/blog/posts/"+str(post_id)+".html"

# Parse all blog posts into a DataFrame.
df = parse_posts(paths,"blog/")
# Declare new index
df.index = df["post-id"]
# Sort the DataFrame
df.sort_index(axis=0,inplace=True,ascending=False)

# Create links
df["link"] = df["post-id"].apply(get_link)

# Extract a list of posts in the form of Series.
posts = list(map(lambda x: x[1],df.iterrows()))
# Filter for posts which should be public
posts = filter_posts(posts,"published",True)


# write to blog.html
template = env.get_template("blog.jinja")
with open("public/blog.html","w",encoding="utf-8") as f:
    f.write(template.render(
        blog_posts = posts,
        navbar=navbars["blog"]
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
            navbar = navbars["blog"]
        ))
