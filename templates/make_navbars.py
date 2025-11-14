from make_init import *

nav_menu = [
    {"link": "/", "title": "Home", "index": "index"},
    {"link": "/blog.html", "title": "Blog", "index": "blog"},
    {"link": "/reading.html", "title": "Reading", "index": "reading"},
]

# Get navbars
template = env.get_template("navbar.jinja")
navbars = {
    index: template.render(
        nav_menu = nav_menu,
        current_page = index
    )
    for index in ["index","blog","reading"]
}