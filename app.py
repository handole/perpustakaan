import os
from views import app
from model import db

db.create_all()
app.run(debug=True)