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
    i = 0
    for cid in allCid:
        if i != cid[0]:
            return i
        i += 1
    conn.commit()
    conn.close()
    return i

#Returns next available pid
def get_next_pid():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT pid FROM post ORDER BY pid ASC;"
    allPid = c.execute(q)
    i = 0
    for pid in allPid:
        if i != pid[0]:
            return i
        i += 1
    conn.commit()
    conn.close()
    return i

# Returns: Nothing
def register_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "INSERT INTO user values (?,?,?);"
    c.execute(q, (str(get_next_uid()), username.lower(), password))
    conn.commit()
    conn.close()

# Returns: a dictionary with the keys:
#   "title"     A string with the title of the post
#   "contents"  A string with the contents of the post
#   "username"  A string with the username of the poster
def get_post(pid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT title,content,username FROM post,user where post.uid = user.uid and pid=" + str(pid)+";"
    result = c.execute(q).fetchone()
    post = {}
    if len(result) == 3:
        post = {'title': str(result[0]) , 'content': str(result[1]), 'username': str(result[2])}
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
    i = len(postComments) - 1
    while i >= 0:
        postComments[i] = {'commenter': str(postComments[i][0])
                           , 'comment_id': postComments[i][1],
                           'commenter_id': postComments[i][2]}
        i-=1
    conn.commit()
    conn.close()
    return postComments

# Returns: a list of comment ids made by the user specified by uid
#   Each element of the list should be an integer that is the comment id
def get_comments_for_user(uid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # FILL ME IN
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
    SELECT content
    FROM comment
    WHERE cid = 
    """ + str(cid) + ";"
    text = c.execute(q).fetchone()
    conn.commit()
    conn.close()
    return str(text[0])
       
# Returns a boolean saying whether the user exists
def authenticate(username):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = """
    SELECT username
    FROM user;
    """
    result = c.execute(q).fetchall()
    conn.commit()
    conn.close()
    i = len(result) - 1
    while i >= 0:
        if str(result[i][0]).lower() == username.lower():
            return True
        else:
            i-=1
    return False

# Returns UID based on username and password
def get_uid(username, password):
    if authenticate(username):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        q = """
        SELECT uid, password
        FROM user
        WHERE username = '""" + username + "';"
        result = c.execute(q).fetchone()
        conn.commit()
        conn.close()
        if result is None:
            return -1
        if str(result[1]) == password:
            return result[0]
        else:
            return -1
    else:
        return -1

# Adds new post
def addPost(uid,title, content):
    pid = get_next_pid()
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "INSERT INTO post VALUES (?,?,?,?);"
    c.execute(q, (str(pid), str(uid), title, content))
    conn.commit()
    conn.close()
    

# Adds new comment to a post
def addComment(uid, pid, content):
    cid = get_next_cid()
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q= "INSERT INTO comment VALUES (?,?,?,?)"
    c.execute(q, (str(cid), str(pid), str(uid), content))
    conn.commit()
    conn.close()

# Delete post
def delPost(pid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = """
    DELETE FROM post WHERE pid = 
    """ + str(pid)
    c.execute(q)
    conn.commit()
    conn.close()

# Delete comment
def delComment(cid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = """
    DELETE FROM comment WHERE cid = 
    """ + str(cid)
    c.execute(q)
    conn.commit()
    conn.close()

#gets all comment content for a post
def comments_contents_for_user(uid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    cids = get_comments_for_user(uid)
    content = []
    for cid in cids:
        content += [get_comment_contents(cid)]
    conn.commit()
    conn.close()
    return content


    
#return list the posts in a dictionary with keys
#       {'title': title
#        'content':content
#        'username':username }
def get_all_pids():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = "SELECT pid FROM post;"
    result = list(c.execute(q))
    pids = []
    for pid in result:
        pids += [pid[0]]
    conn.commit()
    conn.close()
    return pids

#return uid from post
def get_uid_from_post(pid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = """
    SELECT uid
    FROM post
    WHERE pid = 
    """ + str(pid) +";"
    result = c.execute(q).fetchone()
    conn.commit()
    conn.close()
    return result[0]

#return uid from comment
def get_uid_from_comment(cid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = """
    SELECT uid
    FROM comment
    WHERE cid = 
    """ + str(cid) +";"
    result = c.execute(q).fetchone()
    conn.commit()
    conn.close()
    return result[0]

#return pid from comment
def get_pid_from_comment(cid):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    q = """
    SELECT pid
    FROM comment
    WHERE cid = 
    """ + str(cid) +";"
    result = c.execute(q).fetchone()
    conn.commit()
    conn.close()
    return result[0]

#Changes password
def change_password(username, oldpass, newpass):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    uid = get_uid(username,oldpass)
    if not (uid == -1):
        q = """UPDATE user SET password ='""" + newpass + "' WHERE uid = " + str(uid) + ";"
        c.execute(q)
    conn.commit()
    conn.close()

