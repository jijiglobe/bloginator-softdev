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
    totalUsers=db.user.count({})
    i=0
    for i in range(totalUsers+1):
        i += 1
    return i
    #allUid = user.find({"uid":True}).sort({"uid":-1})
    #return allUid[0]["uid"]

def get_next_cid():
    totalComments=db.comment.count({})
    i=0
    for i in range(totalComments+1):
        i+=1
    return i 


def get_next_pid():
    totalPosts = db.post.count({})
    i=0
    for i in range(totalPosts+1):
        i+=1
    return i


def register_user(username, password):
    d = {'uid':get_next_uid(), 'username':username, 'password':password}
    db.user.insert(d)
    return


def get_post(pid):
    d = db.post.find({'pid':pid})
    post = d.content
    return post

#IDK WHAT DOES FIND EVEN RETURN
def get_posts_by_user(uid):
    userPosts = post.find({"uid":uid},{"pid":True})
    i = len(userPosts) - 1
    while (i >= 0 ):
        userPosts[i] = userPosts[i][0]
        i-=1
    return userPosts 

def get_comments_for_post(pid):
    postComments = comments.find({"pid":pid},{"uid": True, "content":True})
    i = len(postComments) - 1
    while i >= 0:
        postComments[i] = {'commenter': str(get_user(postComments[i][0])),
                           'comment_id': postComments[i][1],
                           'commenter_id': postComments[i][2]}
        i-=1
    return postComments

def get_user(uid):
    return user.find({"uid":uid},{"username":True})

def get_comments_for_user(uid):
    userComments = comment.find({"uid":uid},{"content":True})
    #i = len(userComments) - 1
    #while i >= 0:
    #userComments[i] = userComments[i][0]
    #i-=1
    return userComments

def get_comment_contents(cid):
    return comment.find({"cid":cid}, {"content":True})

def authenticate(username):
    result = user.find({"username":username})
    return result==username

def get_uid(username, password):
    d = user.find({$and [{"username":username},{"password":password}]},{"uid":True})
    
    

def addPost(uid, title, content):
    pid = get_next_pid()
    d= {'pid':pid,'uid':uid,'title':title,'content':content}
    db.post.insert(d)
    return

def addComment(uid, pid, content):
    cid = get_next_cid()
    d= {'cid':cid,'uid':uid,'pid':pid,'content':content}
    db.comments.insert(d)
    return

def delPost(pid):
    db.post.remove({'pid':pid})
    return

def delComment(cid):
    db.comments.remove({'cid':cid})
    return

def comments_contents_for_user(uid):
    return

def get_all_pids():
    return

def get_uid_from_post(pid):
    d=db.post.find({'pid'=pid})
    result = d['uid']
    return result

def get_uid_from_comment(cid):
    d=db.comment.find({'cid'=cid})
    result = d['uid']
    return result

def get_pid_from_comment(cid):
    d = db.comment.find({'cid'=cid})
    result = d['pid']
    return result

def change_password(username, oldpass, newpass):
    uid = get_uid(username,oldpass)
    return


