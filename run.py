from flaskblog import create_app
from os import environ

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get('FLASK_RUN_PORT'))