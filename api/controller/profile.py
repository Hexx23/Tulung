from flask import render_template, session
from model.postingan import PostinganModel
class Profile:
    def __init__(self):
        self.post = PostinganModel()

    def profile_page(self):
        username = session['username']
        data = self.post.get_by_user(session['$id'])
        return render_template("profile.html", username = username, data = data)
    