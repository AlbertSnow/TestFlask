# We import the markdown library
import markdown
from flask import Flask
from flask import render_template
from flask import Markup
import os

app = Flask(__name__)
@app.route('/')

def index():
  print (os.environ['PYTHONPATH'])
  markdownContent = (open("./static/index.md", "r").read())
#   markdownContent = "***hello***"
  content = Markup(markdown.markdown(markdownContent))
  return render_template('index.html', **locals())                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

app.run(debug=True)