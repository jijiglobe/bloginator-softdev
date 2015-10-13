import sqlite3

conn = sqlite3.connect("blog.db")
c = conn.cursor()

def aPost():
    allPosts="""
    SELECT post.title, user.name, post.content
    FROM post,user
    WHERE post.uid=user.uid
    """
    result = c.execute(allPosts);
    for r in result:
        print (r)

def uPost(uid):
    userPosts="""
    SELECT user.name, post.title, post.content
    FROM post,user
    WHERE user.uid=
    """+str(uid)
    result = c.execute(userPosts);
    for r in result:
        print (r)

def comments(pid):
    postComments ="""
    SELECT user.name, comment.content 
    FROM post,comment,user
    WHERE comment.uid = user.uid and comment.pid = post.pid and comment.pid =
    """+ str(pid)
    result = c.execute(postComments)
    for r in result:
        print (r)

aPost()
print ("\n\nUserposts")
uPost(2)
print ("\n\nPostcomments")
comments(1)
