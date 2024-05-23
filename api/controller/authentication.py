from flask import render_template
from flask import request, session
from flask import redirect
from model.account import AccountModel
from model.user_profile import User
from model.admin_profile import Admin
from model.account_profile import AkunProfileModel

class Auth:
    def __init__(self):
        self.akun = AkunProfileModel()
    def login_page(self):
        return render_template("login.html")

    def do_login(self):

        email_input = request.form['email']
        password_input = request.form['password']
        akun_in_db = self.akun.get_by_email(email_input)
        if akun_in_db == None:
            return render_template('login.html', error = 'akun tidak ditemukan')
        if password_input != akun_in_db['Password']:
            return render_template('login.html',error='*Password salah') 
        session['username'] = akun_in_db['Username']
        session['email'] = akun_in_db['Email']
        session['$id'] = akun_in_db['$id']
        return redirect(f'/')
    
    def regist_page(self):
        return render_template("daftar.html")
    
    def do_daftar(self):
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        akun_in_db = self.akun.get_by_email(email)
        if akun_in_db == None:
            self.akun.create_account(email,password,username)
            return redirect(f'/login')
        else:
            return render_template('daftar.html', error = "akun sudah digunakan")
    def do_logout(self):
        session.clear()
        return redirect(f'/login')
        