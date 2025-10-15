import frontmatter, markdown
import jinja2 as j2

test = frontmatter.load("blog/2025-09-18.md")

# print(markdown.markdown(test.content))
# print(test["content"])

blog_posts = []
blog_paths = [
    "2025-09-06.md",
    "2025-09-07.md",
    "2025-09-18.md",
    "2025-10-01.md",
    "2025-10-12.md",
    "2025-10-13.md",
    "2025-10-14.md",
    "2025-10-15.md"
]

for path in reversed(blog_paths):
    with open('blog/'+path) as f:
        metadata,content = frontmatter.parse(f.read())
    metadata["content"] = markdown.markdown(content)
    blog_posts.append(metadata)


    
env = j2.Environment(
    loader = j2.FileSystemLoader("templates"),
    autoescape = j2.select_autoescape()
)

template = env.get_template("blog-template.jinja")
with open("public/blog.html","w") as f:
    f.write(template.render(blog_posts = blog_posts))
