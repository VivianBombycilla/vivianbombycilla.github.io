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
        # print(path)
        with open("blog/"+path) as f:
            # print(f.read())
            post = frontmatter.loads(f.read())
            post_dict = post.to_dict()
            # print(post_dict)
            sr = pd.Series(post_dict)
            df = pd.concat([df,sr],axis=1,ignore_index=True)
            # print(df)
        # input()
    # reorganize df
    df = df.transpose()
    df.index = df["post-id"]
    df["content"] = df["content"].apply(markdown.markdown)
    df.sort_index(axis=0,inplace=True,ascending=False)
    return df

def filter_posts(df,category):
    filtered_df = df[ df["category"] == category ]
    return map(lambda x: x[1],filtered_df.iterrows())

df = parse_blog_posts(paths)

env = j2.Environment(
    loader = j2.FileSystemLoader("templates"),
    autoescape = j2.select_autoescape()
)

# write to blog.html
template = env.get_template("blog-template.jinja")
with open("public/blog.html","w") as f:
    f.write(template.render(blog_posts = filter_posts(df,"website")))

# write to games.html
template = env.get_template("games-template.jinja")
with open("public/games.html","w") as f:
    f.write(template.render(blog_posts = filter_posts(df,"games")))