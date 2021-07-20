from flask import Flask
import requests

# initializing the application
app = Flask(__name__)

# initial route
@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    return  response

if __name__ == '__main__':
    app.run(debug=True)
