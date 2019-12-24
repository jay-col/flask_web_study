import os
from liuyan import app


dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path),'data.db')

SECRET_KEY = os.getenv('SECRET_KEY','secret string')
SQLALCHEMY_TRACK_MODIFICATION = False
SQLALCHEMY_DATEBASE_URI = os.getenv('DATABASE_URI',dev_db)

