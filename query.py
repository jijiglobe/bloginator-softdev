import sqlite3

DB_NAME = "blog.db"

# Returns: Nothing
def register_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # FILL ME IN
    conn.commit()
    conn.close()

# Returns: a dictionary with the keys:
#   "title"     A string with the title of the post
#   "contents"  A string with the contents of the post
def get_post(pid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # FILL ME IN
    conn.commit()
    conn.close()

# Returns: a list of post ids made by the user specified by uid
#   Each element of the list should be an integer containing the pid of the post
def get_posts_by_user(uid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # FILL ME IN
    conn.commit()
    conn.close()

# Returns: a list of dictionaries of all the posts
#   Each element of the list should be a dictionary containing the keys:
#       "commenter"
#       "comment_id"
#       "commenter_id"
def get_comments_for_post(pid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # FILL ME IN
    conn.commit()
    conn.close()

# Returns: a list of comment ids made by the user specified by uid
#   Each element of the list should be an integer that is the comment id
def get_comments_for_user(uid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # FILL ME IN
    conn.commit()
    conn.close()

# Returns a string containing the content for the comment specified by cid
def get_comment_contents(cid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # FILL ME IN
    conn.commit()
    conn.close()
