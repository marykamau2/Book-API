from app import create_app
from flask_script import Manager,Server

app = create_app('production')

if __name__ =='__main__':
    app.run()