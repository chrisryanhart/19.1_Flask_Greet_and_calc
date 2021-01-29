# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

# need to call functions from operations.py
# how to call a func from another file?

@app.route('/add')
def add_search():
    a_text = request.args["a"]
    b_text = request.args["b"]

    a = int(a_text)
    b = int(b_text)

    sum = add(a,b)

    return f"""
    <html>
        <body>
          sum = {sum}
          a = {a}
          b = {b}
        </body>
    </html>
    """
@app.route('/sub')
def sub_search():
    a_text = request.args["a"]
    b_text = request.args["b"]

    a = int(a_text)
    b = int(b_text)
    
    diff = sub(a,b)

    return f"""
    <html>
        <body>
          diff = {diff}
          a = {a}
          b = {b}
        </body>
    </html>
    """

@app.route('/mult')
def mult_search():
    a_text = request.args["a"]
    b_text = request.args["b"]

    a = int(a_text)
    b = int(b_text)
    
    diff = mult(a,b)

    return f"""
    <html>
        <body>
          diff = {diff}
          a = {a}
          b = {b}
        </body>
    </html>
    """

@app.route('/div')
def div_search():
    a_text = request.args["a"]
    b_text = request.args["b"]

    a = int(a_text)
    b = int(b_text)
    
    quo = div(a,b)

    return f"""
    <html>
        <body>
          quotient = {quo}
          a = {a}
          b = {b}
        </body>
    </html>
    """



# @app.route('/add')
# def get_params():
#     print(request.args)



# get query terms by "term = request.args["term"]"
    # 