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
    q = """SELECT username, cid, comment.uid
    FROM post,user,comment
    WHERE user.uid = comment.uid and comment.pid = post.pid and comment.pid =""" + str(pid) + ";"
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
    q = """
    SELECT cid
    FROM user, comment
    WHERE user.uid = comment.uid and comment.uid=
    """ + str(uid) + ";"
    userComments = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    i = len(userComments) - 1
    while i >= 0:
        userComments[i] = userComments[i][0]
        i-=1
    return userComments

# Returns a string containing the content for the comment specified by cid
def get_comment_contents(cid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = """
    SELECT contet
    FROM comment
    WHERE cid = 
    """ + str(cid)
    text = c.execute(q).fetone()
    conn.commit()
    conn.close()
    return str(text[0])

# Returns a boolean saying whether the user exists
def authenticate(username):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = """
    SELECT username
    FROM user
    """
    result = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    i = len(result) - 1
    while i >= 0:
        if result[i] == username:
            return true
        else:
            i-=1
    return false

# Returns UID based on username and password
def get_uid(username, password):
    if authenticate(username, password):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        q = """
        SELECT uid, password
        FROM user
        WHERE username = 
        """ + username
        result = c.execute(q).fetchone()
        conn.commit()
        conn.close()
        if result[1] == password:
            return result[0]
        else:
            return "Incorrect username or password."
    else:
        return "Incorrect username or password."

# Adds new post
def addPost(uid,title, content):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = """ 
    INSERT INTO user values( """ + str(get_next_pid()) + "," + str(uid) + "," + title + "," + content +");"
    c.execute(q)
    conn.commit()
    conn.close()
    

# Adds new comment to a post
def addComment(uid, pid, content):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q= """
    INSERT INTO comment values( """ + str(get_next_cid()) + "," + str(pid) + "," + str(uid) + content + ");"
    c.execute(q)
    conn.commit()
    conn.close(0

# Delete post
def delPost(pid):
    pass

# Delete comment
def delComment(cid):
    pass

