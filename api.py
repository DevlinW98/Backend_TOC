from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  

class Movie:
    def __init__(self, title="", url_picture="", score="", duration="", description="", director="", genre=""):
        self.__title = title
        self.__url_picture = url_picture
        self.__score = score
        self.__duration = duration
        self.__description = description
        self.__director = director
        self.__genre = genre

    def to_dict(self):
        return {
            "_Movie__title": self.__title,
            "_Movie__url_picture": self.__url_picture,
            "_Movie__score": self.__score,
            "_Movie__duration": self.__duration,
            "_Movie__description": self.__description,
            "_Movie__director": self.__director,
            "_Movie__genre": self.__genre
        }

@app.route('/movies', methods=['GET'])
def get_movies():
   
    with open('List_250movies.json', 'r') as json_file:
        movies_data = json.load(json_file)
    return jsonify(movies_data)

if __name__ == '__main__':
    app.run(debug=True)

def scaping_data():
    pass