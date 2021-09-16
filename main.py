
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/',methods = ['Get','Post'])
def welcome():
    return "Welcome to Praxis"

@app.route('/anothername/<your_name>',methods = ['Get','Post'])
def names(your_name):
    return f"Welcome to Praxis {your_name}" 


if __name__ == '__main__':
    app.run(debug= True,host = "0.0.0.0",port = 3400)
