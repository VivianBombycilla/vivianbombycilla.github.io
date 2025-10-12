import jinja2 as j2

blog_posts = []
blog_paths = [
    "2025-09-06.txt",
    "2025-09-07.txt",
    "2025-09-18.txt",
    "2025-10-01.txt"
]
for path in blog_paths:
    f = open("blog/"+path)
    blog_posts.append(f.read())
    f.close()

env = j2.Environment(
    loader = j2.FileSystemLoader("templates"),
    autoescape = j2.select_autoescape()
)

template = env.get_template("blog-template.jinja")
print(template.render(blog_posts = blog_posts))