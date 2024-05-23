from flask import render_template
from model.postingan import PostinganModel


class Beranda:
    def __init__(self):
        self.post = PostinganModel()

    def beranda_page(self):
        return render_template("beranda.html", daftar_post = self.post.get_all_post())