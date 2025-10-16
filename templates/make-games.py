import frontmatter, markdown
import jinja2 as j2

test = frontmatter.load("blog/2025-09-18.md")

# print(markdown.markdown(test.content))
# print(test["content"])

blog_posts = []
blog_paths = [
    "PKS_2025-W41.md",
    "PKS_2025-W42.md",
    "HGSS_2025-10-14.md"
]

for path in reversed(blog_paths):
    with open('blog/games-diary/'+path) as f:
        metadata,content = frontmatter.parse(f.read())
    metadata["content"] = markdown.markdown(content)
    blog_posts.append(metadata)


    
env = j2.Environment(
    loader = j2.FileSystemLoader("templates"),
    autoescape = j2.select_autoescape()
)

template = env.get_template("games-template.jinja")
with open("public/games.html","w") as f:
    f.write(template.render(blog_posts = blog_posts))
