#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

print("hi there this prints")
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
@app.route('/print/<string:some_string>')
def print_string(some_string):
    print(some_string)
    return f"{some_string}" 
@app.route('/count/<int:int_variable>')
def count(int_variable):
    int_list = [str(int) for int in range(int_variable)]
    final_list = "\n".join(int_list) + "\n"
    return final_list
@app.route('/math/<string:num1>/<string:operation>/<string:num2>')
def math(num1, operation, num2):
    if operation == "div":
        operation = "/"
    return str(eval(f"{num1}{operation}{num2}"))


    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
print("HELLOOOOOOO")