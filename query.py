import random
from pymongo import MongoClient

# connection = MongoClient('hostname')
connection = MongoClient()

# To authenticate after connecting
# db = connection.admin
# db.authenticate('username','password')

db = connection['blog']

def get_next_uid():
    totalUsers=db.user.count({})
    i=0
    for i in range(totalUsers+1):
        i++
    return i

def get_next_cid():
    totalComments=db.comment.count({})
    i=0
    for i in range(totalComments+1):
        i++
    return i 


def get_next_pid():
    totalPosts = db.post.count({})
    i=0
    for i in range(totalPosts+1):
        i++
    return i


def register_user(username, password):
    d = {'uid':get_next_uid(), 'username':username, 'password':password}
    db.user.insert(d)
    return


def get_post(pid):
    d = db.post.find({'pid':pid})
    post = d.content
    return post


def get_posts_by_user(uid):
    return

def get_comments_for_post(pid):
    return

def get_comments_for_user(uid):
    return

def get_comment_contents(cid):
    return

def authenticate(username):
    return

def get_uid(username, password):
    return

def addPost(uid, title, content):
    return

def addComment(uid, pid, content):
    return

def delPost(pid):
    return

def delComment(cid):
    return

def comments_contents_for_user(uid):
    return

def get_all_pids():
    return

def get_uid_from_post(pid):
    return

def get_uid_from_comment(cid):
    return

def get_pid_from_comment(cid):
    return

def change_password(username, oldpass, newpass):
    return


