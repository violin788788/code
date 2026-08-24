import sys,platform
sys.path.insert(0, r"A:\Users\-\code")
from utils import *
def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)
#new_file = os.path.join(a,b,c)
drive = os.path.splitdrive(os.getcwd())[0]
cwd = os.getcwd()
files = os.listdir(cwd)



from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    x = request.form.get("x", "")
    return render_template("test.html", x=x)
#app.run(debug=True)
if __name__ == '__main__':
    current_os = platform.system()
    print(current_os)
    if "Windows" in current_os:
        os.startfile("http://127.0.0.1:5000")

    app.run(debug=True)

