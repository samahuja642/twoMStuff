from flask import Flask
import os

def create_app(test_config=None):
 app = Flask(__name__)
 app.config.from_mapping(
      SECRET_KEY='dev',
     )
 if test_config is None:
     app.config.from_pyfile('config.py')
 else:
     app.config.from_mapping(test_config)

 try:
     os.makedirs(app.instance_path)
 except OSError:
     pass
 @app.route('/')
 def hello():
     return 'Hello, World!'
 if __name__=='__main__':
     app.run(debug=True)

create_app()    
