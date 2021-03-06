import os
from flask import Flask, render_template, redirect, url_for, request
import wsgiref
app = Flask(__name__)


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin123':
            error = 'Invalid Username/Password.'
        else:
            # return redirect(url_for('home'))
            error = "Login Successful!"
    return render_template('login2.html', error=error)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
