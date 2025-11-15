import os
import frontmatter
import markdown
import jinja2 as j2
import pandas as pd

def parse_posts(paths, directory):
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

def filter_posts(posts,filter_by,category):
    '''Filter a list of posts'''
    filtered_posts = [post for post in posts if post[filter_by] == category]
    return filtered_posts

# Load Jinja environment
env = j2.Environment(
    loader = j2.FileSystemLoader("templates"),
    autoescape = j2.select_autoescape(),
    trim_blocks = True,
    lstrip_blocks = True
)