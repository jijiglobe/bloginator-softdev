from flask import Flask, render_template, session, redirect, request, url_for
import query

@app.route("")
@app.route("/home")
def home():
    return render_template("home.html")
    
@app.route("/login", methods=["GET","POST"])
def login(): #confirm uid and password exists
        if request.method == "GET":
            if 'logged_in' in session and session['logged_in']:
                return redirect(url_for("posts"))
            else:
                return render_template("home.html")
        else:
            assert(request.method == "POST")
            username = request.form['uname']
            password = request.form['pword']
            if query.authenticate(username, password)
                session['logged_in'] = True
                session['UID'] = query.get_uid(username, password)
                return redirect(url_for("posts"))
            else:
                session['logged_in'] = False
                return render_template("login.html", error="User not in database. Need an account?") #we should put a link to the register page on login.html

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route("/register", methods=["GET","POST"]) 
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        assert(request.method=="POST")
        query.register_user(request.form['uname'], request.form['pword'])
        return redirect(url_for("login"))

@app.route("/profile/<uid>", methods=["GET","POST"]) #list of all user posts + most recent comments
def profile():
    
    #how do you validate this? what if it is an invlaid number or something
    postList = query.get_posts_by_user(session['UID']) #post ids
    retList = []
    ctr = 0
    while ctr < len(postList):
        d = query.get_post(postList[ctr]) # {"title":-, "contents":-, "username":-,}
        listOfComments = query.get_comments_for_post(postList[ctr])
        lastInd = len(listOfComments) -1
        topCommentID = listOfComments[lastInd]["comment_id"]
        topCommentString = query.get_comment_contents(topCommentID)
        d['last_comment'] = topCommentString
        retList.append(d)
        ctr += 1
    #retList in the format [ {"title":,"contents":,"username":,"last_comment":}, {...}]
    return render_template("userposts.html", POST_LIST = retlist)
    
#add new posts here
@app.route("/posts") #shows all posts, title + most recent comment. 
def posts():
    postList = query.get_post_list(); #list of all pid's
    listOfDicts = []
    ctr = 0;
    while ctr < len(postList):
        title = query.get_post(postList[ctr])["title"] 
        #content = query.get_post(postList[ctr])["contents"]
        topCommentID = query.get_comments_for_post(postList[ctr])[0]["comment_id"]
        topComment = query.get_comment_contents(topCommentID)
        postDict[title]=topComment
        ctr += 1
    return render_template("allposts.html", POST_DICT = postDict)#, PIDS_LIST = postList) 

@app.route("/posts/<pid>", methods = ["GET","POST"]) #for individual posts
def onepost(pid=0):
    if request.method == "GET":
        commentList = query.get_comments_for_post(pid) #actually a dicitonary
        ctr = 0;
        while ctr < len(commentList):
            x = query.get_comment_contents(commentList[ctr]["comment_id"])
            commentList[ctr] = x
            ctr += 1
        #commentList is now a list of strings of the contents
        pid = int(pid)
        #check for valid pid somehow?
        return render_template("post.html", POST_CONTENT = query.get_post(pid), COMMENT_LIST = commentList)
    else:
        assert(request.method == "POST")
        query.add_comment(request.form['comment_content'])
        return redirect(url_for("posts/<pid>"))


if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)
