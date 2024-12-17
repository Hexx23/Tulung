from flask import Flask
from flask import session
from flask import redirect
from controller.authentication import Auth
from controller.beranda import Beranda
from controller.OTP import Otp
from controller.jasa import Jasa
from controller.postingan import Postingan
from controller.profile import Profile
from controller.post import Post
from model.postingan import PostinganModel


auth = Auth()
beranda = Beranda()
otp = Otp()
jasa = Jasa()
postingan = Postingan()
post_data = PostinganModel()
profile = Profile()
post = Post()

app = Flask(__name__)
app.secret_key = "tes"

@app.get("/")
def beranda_page():
    if "username" not in session:
        return redirect(f'/login')
    return beranda.beranda_page()

@app.get("/postingan")
def postingan_create_page():
    return postingan.postingan_create_page()

@app.post("/postingan/create")
def postingan_create():
    return postingan.create_post()
    

@app.get("/postingan/<id>")
def postingan_by_id_page(id):
    if "username" not in session:
        return redirect(f'/login')
    return postingan.postingan_by_id_page(id = id)

@app.get("/jasa")
def jasa_page():
    if "username" not in session:
        return redirect(f'/login')
    return jasa.jasa_page()



@app.get("/login")
def login_get():
    return auth.login_page()

@app.post("/login")
def login_post():
    return auth.do_login()

@app.get("/OTP")
def OTP_page():
    return otp.OTP_page()

@app.get("/daftar")
def daftar_get():
    return auth.regist_page()

@app.post("/daftar")
def daftar_post():
    return auth.do_daftar()

@app.get("/profile")
def profile_page():
    if "username" not in session:
        return redirect(f'/login')
    return profile.profile_page()

@app.post("/logout")
def logout_post():
    return auth.do_logout()

# @app.route("/profile/<name>/<alamat>")
# def profile_by_name(name, alamat):
#     return render_template('profile.html', name=name, alamat = alamat)

def handler(event, context):
    return app(event, context)


if __name__ == '__main__':
    app.run(debug = True)
