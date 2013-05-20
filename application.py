from flask import Flask
from shared import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

if __name__ == '__main__':
	app.run()