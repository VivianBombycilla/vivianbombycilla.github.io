from make_navbars import *
from make_blog import posts

# write to index.html
template = env.get_template("index.jinja")
with open("public/index.html","w",encoding="utf-8") as f:
    f.write(template.render(
        latest_post = posts[0],
        navbar = navbars["index"]
    ))
