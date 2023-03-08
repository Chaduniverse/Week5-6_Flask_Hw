from flask import render_template, request,flash, redirect, url_for
from app.blueprints.auth.forms import LoginForm, RegistrationForm, EditProfileForm
from app.blueprints.auth import auth
from app.models import User
from werkzeug.security import check_password_hash 
from flask_login import login_user,current_user, logout_user,login_required


# routes section 

@auth.route('/login',methods = ['GET','POST'])  
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        # query from our db
        queried_user = User.query.filter_by(email=email).first()
        if queried_user and check_password_hash(queried_user.password,password):
            login_user(queried_user)
            flash(f'Successfully Logged In! Welcome back, {queried_user.first_name}!','success')
            return redirect(url_for('main.home'))
        else: 
            error = ('Invalid email or password.')
            flash(f'{error}','danger')
            return render_template('login.html',form=form)
    return render_template('login.html',form=form)  

@auth.route('/logout', methods=['Get']) 
@login_required
def logout():
    if current_user: 
        logout_user()
        flash('You have successfully logged out!', 'warning') 
        return redirect(url_for('auth.login'))


@auth.route('/register',methods = ['GET','POST'])  
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        # grabbing our form data and storing into a dict  

        new_user_data = {
            'first_name':form.first_name.data.title(),
            'last_name':form.last_name.data.title(),
            'email': form.email.data.lower(),
            'password': form.password.data

        }  

        #create instance of user  
        new_user =User()  

        # implementing form values from our form data for our instance  

        new_user.from_dict(new_user_data)   

        #save our database  

        new_user.save_to_db()
        return redirect(url_for('auth.login')) 
    return render_template('register.html',form=form)


@auth.route('/edit_profile', methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        
        # grabbing our form data and storing into a dict  

            new_user_data = {
            'first_name':form.first_name.data.title(),
            'last_name':form.last_name.data.title(),
            'email': form.email.data.lower(),
            'password':current_user.password
        }  
            #query user based of email from database to change 
            queried_user = User.query.filter_by(email=new_user_data['email']).first()
            if queried_user:
                flash('Email already exists','danger')
                return redirect(url_for('auth.edit_profile'))
        
            else:
            # add changes to db
                current_user.from_dict(new_user_data)
                current_user.save_to_db()
                flash('Profile updated!', 'success')
                return redirect(url_for('main.home')) 
    return render_template('edit_profile.html',form=form)  
            
    