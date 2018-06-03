from flask import Flask
from flask_wtf import CSRFProtect  # CSRFProtect защищет форму, чтобы проверить, что вернулась родная форма

from flask_bootstrap import Bootstrap   # фрайемворк для верстки
from flask_pony import Pony


app = Flask(__name__)
app.config.from_object('shop.setting.DevConfig')


pony = Pony(app)

CSRFProtect(app)
Bootstrap(app)

from . import models
from . import views

pony.connect()

