__author__ = 'NakOh'


from flask import Flask
app = Flask(__name__)

@app.route('/profile/', methods=['POST', 'GET'])
def profile(username=None):
    error = None
    if request.method= 'POST' :
        username = request.form['username']
        email = request.form['email']
        if not username and not email:
            return add_profile(request.form)
    else:
        error = 'Invalid username or email'

    return render_template('profile.html', error=error)


