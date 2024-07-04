from flask import Flask,render_template,url_for,flash,redirect
from form import RegistrationForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY']='e0ffa31463abb69d1c115d97d446334a'
posts=[
       {
        'author':'Sheshi kumar',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'june 18,2024'},
       {
        'author':'nitin',
        'title':'Blog Post 2',
        'content':'second post content',
        'date_posted':'june 19,2024'}
       ]



@app.route("/")
@app.route("/home")
def home_page():
    return render_template('index.html',posts=posts)
    
@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route('/register' ,methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data}!','success')
        return redirect(url_for('home_page'))
    return render_template('register.html',title='Register',form=form)
    

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',title='Login',form=form)
        

if __name__=="__main__":
    app.run(debug=True)