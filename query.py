import sqlite3

DB_NAME = "blog.db"

#Returns next available uid
def get_next_uid():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT uid FROM user ORDER BY uid ASC;"
    allUid = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    i = 0
    for uid in allUid:
        if i != uid[0]:
            return i
        i += 1
    return i
    
#Returns next available cid
def get_next_cid():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT cid FROM comment ORDER BY cid ASC;"
    allCid = c.execute(q)
    conn.commit()
    conn.close()
    i = 0
    for uid in allUid:
        if i != uid[0]:
            return i
        i += 1
    return i

#Returns next available pid
def get_next_pid():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT pid FROM post ORDER BY pid ASC;"
    allPid = c.execute(q)
    conn.commit()
    conn.close()
    i = 0
    for uid in allUid:
        if i != uid[0]:
            return i
        i += 1
    return i

# Returns: Nothing
def register_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "INSERT INTO user values(" + str(get_next_uid())+ "," + username + "," + password + ");";
    c.execute(q);
    conn.commit()
    conn.close()

# Returns: a dictionary with the keys:
#   "title"     A string with the title of the post
#   "contents"  A string with the contents of the post
def get_post(pid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT title, content FROM post where pid=" + str(pid)+";"
    result = c.execute(q).fetchone();
    post = {'title': str(result[0]) , 'content': str(result[1])}
    conn.commit()
    conn.close()
    return post

# Returns: a list of post ids made by the user specified by uid
#   Each element of the list should be an integer containing the pid of the post
def get_posts_by_user(uid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT pid FROM post,user where user.uid = post.uid and post.uid=" + str(uid)+";"
    userPosts = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    i = len(userPosts) - 1
    while (i >= 0 ):
        userPosts[i] = userPosts[i][0]
        i-=1
    return userPosts

# Returns: a list of dictionaries of all the posts
#   Each element of the list should be a dictionary containing the keys:
#       "commenter"
#       "comment_id"
#       "commenter_id"
def get_comments_for_post(pid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = """SELECT username, cid, comment.uid FROM post
    ,user,comment WHERE user.uid = comment.uid and comment.pid
    = post.pid and comment.pid =""" + str(pid) + " ORDER BY cid ASC;"
    postComments = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    i = len(postComments) - 1
    while i >= 0:
        postComments[i] = {'commenter': str(postComments[i][0])
                           , 'comment_id': postComments[i][1],
                           'commenter_id': postComments[i][2]}
        i-=1
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


