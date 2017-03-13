from bottle import route, view, template
from datetime import datetime
import bottle

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

app = bottle.default_app();
