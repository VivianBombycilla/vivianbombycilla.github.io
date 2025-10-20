import os
import frontmatter, markdown
import jinja2 as j2
import pandas as pd

# Get blog posts
paths = list(filter(lambda path: path.endswith(".md"),os.listdir("blog")))

def parse_blog_posts(paths):
    '''Parses a list of paths into a DataFrame'''
    df = pd.DataFrame()

    for path in paths:
        with open("blog/"+path) as f:
            post = frontmatter.loads(f.read())
            post_dict = post.to_dict()
            sr = pd.Series(post_dict)
            df = pd.concat([df,sr],axis=1,ignore_index=True)
    # reorganize df
    df = df.transpose()
    df.index = df["post-id"]
    df["content"] = df["content"].apply(markdown.markdown)
    df["link"] = df["post-id"].apply(get_link)
    df.sort_index(axis=0,inplace=True,ascending=False)
    return df

def get_link(post_id):
    '''Gets link to post from post id'''
    return "blog/"+str(post_id)+".html"

def filter_posts(posts,category):
    filtered_posts = [post for post in posts if post["category"] == category]
    return filtered_posts

df = parse_blog_posts(paths)
posts = list(map(lambda x: x[1],df.iterrows()))
print(filter_posts(posts,"games"))
print(filter_posts(posts,"website"))


env = j2.Environment(
    loader = j2.FileSystemLoader("templates"),
    autoescape = j2.select_autoescape()
)

# write to blog.html
template = env.get_template("blog-template.jinja")
with open("public/blog.html","w") as f:
    f.write(template.render(blog_posts = filter_posts(posts,"website")))

# write to games.html
template = env.get_template("games-template.jinja")
with open("public/games.html","w") as f:
    f.write(template.render(blog_posts = filter_posts(posts,"games")))

# write blog post pages
template = env.get_template("blog-post-template.jinja")
for post in posts:
    with open("public/"+post["link"],"w") as f:
        f.write(template.render(blog_post = post))
