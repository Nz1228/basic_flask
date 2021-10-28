from flask import Flask, render_template
app = Flask(__name__)

#Root / is not important :)

@app.route('/')
def index():
    return '<h1>This app is running!</h1>'

#/<int:number> will display integers from 1 to that number
@app.route('/<int:number>')
def view_int(number):
    return "Integers from 1 to " + str(number) + ":" + render_template("loop.html", num = number, view = 'normal')
    
#/<int:number>/odd will display only odd numbers in that range
@app.route('/<int:number>/odd')
def odd_int(number):
    return "Odd integers from 1 to " + str(number) + ":" + render_template("loop.html", num = number, view = 'odd')

#/<int:number>/even will display only even numbers in that range
@app.route('/<int:number>/even')
def even_int(number):
    return "Even integers from 1 to " + str(number) + ":" + render_template("loop.html", num = number, view = 'even')

#/<int:number>/prime will display only prime numbers in that range
@app.route('/<int:number>/prime')
def prime_int(number):
    return "Prime numbers from 1 to " + str(number) + ":" + render_template("loop.html", num = number, view = 'prime')

if __name__ == '__main__':
 app.run(debug=True)
