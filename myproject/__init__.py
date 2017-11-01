from flask import Flask

app = Flask(__name__)
app.config.from_object('myproject.config')

from myproject.views import index

@app.route('/')
def hello():
  return "hello"
