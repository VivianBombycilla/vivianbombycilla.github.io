from make_init import *

nav_menu = [
    {"link": "/", "title": "Home", "index": "index"},
    {"link": "/blog.html", "title": "Blog", "index": "blog"},
    {"link": "/reading.html", "title": "Reading", "index": "reading"},
]

nav_menu_blog = [
    {"link": "/blog.html", "title": "All", "index": "all"},
    {"link": "/blog/website.html", "title": "Website", "index": "website"},
    {"link": "/blog/games.html", "title": "Games", "index": "games"},
    {"link": "/blog/fun.html", "title": "Fun", "index": "fun"},
]

nav_menu_games = [
    {"link": "/blog/games.html", "title": "All", "index": "all"},
    {"link": "/blog/games/pks.html", "title": "PKS", "index": "pks"},
    {"link": "/blog/games/phg.html", "title": "PHG", "index": "phg"},
    {"link": "/blog/games/plza.html", "title": "PLZA", "index": "plza"},
    {"link": "/blog/games/ptcg.html", "title": "PTCG", "index": "ptcg"},
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

navbars_blog = {
    index: template.render(
        nav_menu = nav_menu_blog,
        current_page = index
    )
    for index in ["all","website","games","fun"]
}
navbars_games = {
    index: template.render(
        nav_menu = nav_menu_games,
        current_page = index
    )
    for index in ["all","pks","phg","plza","ptcg"]
}