from make_navbars import *

# Get list of paths to books
book_paths = list(filter(lambda path: path.endswith(".md"),os.listdir("reading")))

def parse_authors(author_list):
    '''Parses list of authors to a string.'''
    return ", ".join(author_list)

# Parse books into DataFrame
books_df = parse_posts(book_paths,"reading/")
# Declare new index
books_df.index = books_df["book-id"]
# Sort the DataFrame
books_df.sort_index(axis=0,inplace=True,ascending=False)

# Parse author column
books_df["author"] = books_df["author"].apply(parse_authors)

# Extract a list of books in the form of Series.
books = list(map(lambda x: x[1],books_df.iterrows()))

# Filter books based on reading status
books_read = filter_posts(books,"status","read")
books_reading = filter_posts(books,"status","reading")

# write to reading.html
template = env.get_template("reading.jinja")
with open("public/reading.html","w",encoding="utf-8") as f:
    f.write(template.render(
        books_read = books_read,
        books_reading = books_reading,
        navbar = navbars["reading"]
    ))
