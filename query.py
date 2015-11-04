import random
import pymongo
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
#Returns next available uid
def get_next_uid():
    totalUsers=db.user.count({})
    """i=0
    for i in range(totalUsers+1):
        i += 1"""
    return totalUsers+1
    #allUid = user.find({"uid":True}).sort({"uid":-1})
    #return allUid[0]["uid"]

#Returns next available cid                                                                                                         
def get_next_cid():
    totalComments=db.comment.count({})
    """i=0
    for i in range(totalComments+1):
        i+=1
    """
    return totalComments+1 

#returns next available cid
def get_next_pid():
    totalPosts = db.post.count({})
    """i=0
    for i in range(totalPosts+1):
        i+=1"""
    return totalPosts+1

#returns nothing
def register_user(username, password):
    d = {'uid':get_next_uid(), 'username':username, 'password':password}
    db.user.insert(d)
    return

# Returns: a dictionary with the keys:
#   "title"     A string with the title of the post
#   "contents"  A string with the contents of the post
#   "username"  A string with the username of the poster                                                                             
def get_post(pid):
    d = db.post.find({'pid':pid})
    post = d.content
    return post

#IDK WHAT DOES FIND EVEN RETURN
# Returns: a list of post ids made by the user specified by uid
#   Each element of the list should be an integer containing the pid of the post def get_posts_by_user(uid):
    userPosts = post.find({"uid":uid},{"pid":True})
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

# Returns: a list of comment ids made by the user specified by uid
#   Each element of the list should be an integer that is the comment id
def get_comments_for_user(uid):
    userComments = comment.find({"uid":uid},{"content":True})
    #i = len(userComments) - 1
    #while i >= 0:
    #userComments[i] = userComments[i][0]
    #i-=1
    ans = []
    for x in userComments:
        ans.append[x["cid"]]
    return ans

# Returns a string containing the content for the comment specified by cid
def get_comment_contents(cid):
    comment = comment.find({"cid":cid}, {"content":True})
    return comment["content"]


def authenticate(username):
    result = user.find({"username":username})
    return #result["password"] == 

# Returns UID based on username and password
def get_uid(username, password):
    result == user.find({"username":username},{"uid":True, "password":True})
    if result is None:
        return -1
    if result[password] == password:
        return result[uid]
    else:
        return -1

#Adds new Post
def addPost(uid, title, content):
    d= {'uid':uid,'title':title,'content':content}
    db.post.insert(d)
    return


#Adds new Comment to Post
def addComment(uid, pid, content):
    d= {'uid':uid,'pid':pid,'content':content,"cid":get_next_cid()}
    db.comments.insert(d)
    return

#deletes a post
def delPost(pid):
    db.post.remove({'pid':pid})
    return

#deletes a comment
def delComment(cid):
    db.comments.remove({'cid':cid})
    return

#gets all comment content for a post
def comments_contents_for_user(pid):
    return db.post.comments.find({'pid' : pid}, {pid : 0, _id : 0, content : 1})

#gets a list of all pids
def get_all_pids():
    return db.post.find({},{_id : 0, pid : 1})

#gets the uid of a post with this.pid==pid
def get_uid_from_post(pid):
    post = db.posts.find({"pid":pid})
    for x in post:
        return x["uid"]

#gets the uid of a comment with this.cid=cid
def get_uid_from_comment(cid):
    post = db.
    return

#gets the pid of a comment with this.cid=cid
def get_pid_from_comment(cid):
    return

#changes the password of username from oldpass to newpass
def change_password(username, oldpass, newpass):
    return


