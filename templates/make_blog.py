from make_navbars import *

# Get list of paths to posts
paths = glob.glob("blog/*/*/*.md")

def get_link(post_id):
    '''Gets link to post from post id'''
    return "/blog/posts/"+str(post_id)+".html"

def find_adjacent_posts(post_id,posts,df):
    '''Returns the previous and next post in the list.'''
    ids = list(map(lambda post:post["id"],posts))
    prev_post_id = max(list(filter(lambda x: x < post_id, ids)) or [None])
    next_post_id = min(list(filter(lambda x: x > post_id, ids)) or [None])
    print(ids,post_id,prev_post_id,next_post_id)
    return find_post(prev_post_id,df),find_post(next_post_id,df)

def find_post(post_id,df):
    '''Finds a post with the id given, or returns None if post_id is None.'''
    if post_id == None:
        return None
    return df.loc[post_id]

# Parse all blog posts into a DataFrame.
df = parse_posts(paths,"")

# Create links
df["link"] = df["id"].apply(get_link)

# Extract a list of posts in the form of Series.
posts = list(map(lambda x: x[1],df.iterrows()))
# Filter for posts which should be public
posts = filter_posts(posts,"published",True)

# write to blog.html
template = env.get_template("blog.jinja")
with open("public/blog.html","w",encoding="utf-8") as f:
    f.write(template.render(
        blog_posts = posts,
        navbars = (navbars["blog"], navbars_blog["all"])
    ))

# write blog category pages
for category in ["website", "games", "fun"]:
    if category == "games":
        current_navbars = (navbars["blog"], navbars_blog[category], navbars_games["all"])
    else:
        current_navbars = (navbars["blog"], navbars_blog[category])
    with open("public/blog/"+category+".html","w",encoding="utf-8") as f:
        f.write(template.render(
            blog_posts = filter_posts(posts,"category",category),
            navbars = current_navbars
        ))

# write blog/games pages
game_posts = filter_posts(posts,"category","games")
for game in ["pks","phg","plza","ptcg"]:
    with open("public/blog/games/"+game+".html","w",encoding="utf-8") as f:
        f.write(template.render(
            blog_posts = filter_posts(game_posts,"post-series",game),
            navbars = (navbars["blog"], navbars_blog["games"], navbars_games[game])
        ))



# write blog post pages
for i in range(len(posts)):
    post = posts[i]
    post_id = post["id"]
    # make blog post navbars
    template = env.get_template("blog-post-navbar.jinja")
    prev_post,next_post = find_adjacent_posts(post_id,posts,df)
    blog_post_navbars = [template.render(
        blog_post = post,
        prev_post = prev_post,
        next_post = next_post,
        middle_text = "Current"
    )]
    # category navbar
    prev_post,next_post = find_adjacent_posts(post_id,filter_posts(posts,"category",post["category"]),df)
    blog_post_navbars.append(template.render(
        blog_post = post,
        prev_post = prev_post,
        next_post = next_post,
        middle_text = ("Category: "+post["category"])
    ))
    
    # series navbar
    if post["post-series"]:
        prev_post,next_post = find_adjacent_posts(post_id,filter_posts(posts,"post-series",post["post-series"]),df)
        blog_post_navbars.append(template.render(
            blog_post = post,
            prev_post = prev_post,
            next_post = next_post,
            middle_text = ("Series: "+post["post-series"])
        ))
    # write
    template = env.get_template("blog-post.jinja")
    with open("public/"+post["link"],"w",encoding="utf-8") as f:
        f.write(template.render(
            blog_post = post,
            blog_post_navbars = blog_post_navbars,
            navbar = navbars["blog"]
        ))
