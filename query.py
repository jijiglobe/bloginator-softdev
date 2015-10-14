import sqlite3

DB_NAME = "blog.db"

#Returns next available pid
def get_next_uid():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT uid FROM user"
    allUid = c.execute(q)
    conn.commit()
    conn.close()
    i = 0
    while i == int(uid):
        i+=1
    return i

#Returns next available cid
def get_next_cid():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT cid FROM comment"
    allCid = c.execute(q)
    conn.commit()
    conn.close()
    i = 0
    while i == int(uid):
        i+=1
    return i

#Returns next available pid
def get_next_pid():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT pid FROM post"
    allPid = c.execute(q)
    conn.commit()
    conn.close()
    i = 0
    while i == int(uid):
        i+=1
    return i

# Returns: Nothing
def register_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "INSERT INTO user values(" + str(get_next_uid())+ "," + username + "," + password + ")";
    c.execute(q);
    conn.commit()
    conn.close()

# Returns: a dictionary with the keys:
#   "title"     A string with the title of the post
#   "contents"  A string with the contents of the post
def get_post(pid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT title, content FROM post where pid=" + str(pid)
    result = c.execute(q);
    print(result)
    post = {'title': result[0] , 'content': result[1]}
    conn.commit()
    conn.close()
    return post

# Returns: a list of post ids made by the user specified by uid
#   Each element of the list should be an integer containing the pid of the post
def get_posts_by_user(uid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT uid FROM post,user where post.uid=" + str(uid)
    userPosts = c.execute(q)
    conn.commit()
    conn.close()
    return userPosts

# Returns: a list of dictionaries of all the posts
#   Each element of the list should be a dictionary containing the keys:
#       "commenter"
#       "comment_id"
#       "commenter_id"
def get_comments_for_post(pid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT username, cid, comment.uid FROM post,user,comment WHERE comment.pid = post.pid and comment.pid =" + str(pid)
    postComments = c.execute(q)
    conn.commit()
    conn.close()
    return postComments

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


