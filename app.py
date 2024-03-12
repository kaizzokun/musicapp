from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def handle_signup():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # To check if the passwords match
    if password != confirm_password:
        return "Passwords do not match. Please try again."

    # To check if the username is already taken
    if username in users:
        return "Username already taken. Please choose another username."

    # To store the user data in memory
    users[username] = password

    # To redirect to a index page 
    return redirect(url_for('index'))


@app.route('/')
def show_login():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # If the username and password are correct, redirect to main page or index.html
        return redirect(url_for('index'))
    else:
        # If username or password is incorrect, redirect back to login page
        return redirect(url_for('show_login'))


if __name__ == '__main__':
    app.run(debug=True)