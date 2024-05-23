from flask import render_template
class Post:
    def post_page(self):
        return render_template("post.html")