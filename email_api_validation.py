
#
from flask import Flask,jsonify,render_template,request
from pyisemail import is_email

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def api():
    if request.method == 'POST':
        email1=request.form["email"]
        verify = is_email(email1, check_dns=True)
        if verify==True:
            ver="Valid"
        else:
            ver="Invalid"
        a= {email1: ver}
        return jsonify(a)
    return render_template("home.html")

@app.route('/email',methods=['GET','POST'])
def api2():
    if request.method == 'POST':
        files = request.files['files']
        str_files=files.read().decode('utf-8')
        file_t=str_files.splitlines()
        for i in file_t:
                bool_result_with_dns = is_email(i, check_dns=True)
                if bool_result_with_dns==False:
                    f=open("Invalid_email.txt","a+")
                    f.write(str(i))
                    f.write("\n")
                    f.close()
                else:
                    f=open("Valid_emails.txt",'a+')
                    f.write((str(i)))
                    f.write("\n")
                    f.close()

    return render_template("email_csv.html")


if __name__ == "__main__":
    app.run(debug=True)
