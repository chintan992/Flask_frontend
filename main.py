from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return '1234'

@app.route('/hello')
def hello_world1():
   return 'hello world'
app.add_url_rule('/', 'hello', hello_world1)


if __name__ == '__main__':
   app.run(debug = True)