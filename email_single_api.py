
#
from flask import Flask,jsonify,render_template,request
from pyisemail import is_email


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"


@app.route('/email',methods=['GET','POST'])
def api():
    if request.method == 'POST':
        email1=request.form["email"]
        verify = is_email(email1, check_dns=True)
        if verify==True:
            ver="Valid"
        else:
            ver="Invalid"
        return f'''
         <h1>The email is: {ver} email</h1>'''
    return '''
                  <form method="POST">
                      <label for="Email">Enter Email Here:</label>
    <input type="email" id="email" name="email"><br><br>
    <input type="submit" value="Validate">
                  </form>'''

if __name__ == "__main__":
    app.run(debug=True)
