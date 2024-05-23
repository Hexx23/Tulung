from flask import render_template, request, redirect, session
from model.postingan import PostinganModel
import os


class Postingan:
    def __init__(self):
        self.post = PostinganModel()

    def postingan_create_page(self):
        return render_template("post.html")
        
    def  create_post(self):
        description = request.form['Deskripsi']
        image = request.files['file']
        if image: 
            path_directory = os.path.join(os.getcwd(), "static")
            image.save(os.path.join(path_directory, image.filename))
        self.post.create_post(user_id= session['$id'], image="../static/" + image.filename , description= description)
        return redirect(f'/')
    
    def postingan_by_id_page(self,id):
        return render_template("postingan.html", post = self.post.get_by_id(id))
    