## import app object
from app import app


## run our app
if __name__ == '__main__':
    app.run( host='0.0.0.0', port=1555, load_dotenv=True )