from flask import Flask

app = Flask(__name__)


@app.route('/product/edit')
@app.route('/product/edit/<int:pk>')
def hello(pk=None):
    """view, endpoint"""
    return 'Hello, Flask'

"""
@app.route('/product/edit')
@app.route('/product/edit/<int:uid>/<int:git>')
def hello(uid=None, git=None):
    #view, endpoint
    return 'Hello, Flask'
"""