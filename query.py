import random
from pymongo import MongoClient

# connection = MongoClient('hostname')
connection = MongoClient()

db = connection.blog
user = db.user
post = db.post
comment = db.comment
# To authenticate after connecting
# db = connection.admin
# db.authenticate('username','password')

#????
def get_next_uid():
    allUid = user.find({"uid":True}).sort({"uid":-1})
    return allUid[0]["uid"]

def get_next_cid():
    
    return


def get_next_pid():
    
    return


def register_user(username, password):
    
    return


def get_post(pid):

    return


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


