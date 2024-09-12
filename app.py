import scrap
from flask import Flask, render_template, jsonify, send_file, render_template_string
from flask_cors import CORS
import json
import time

app = Flask(__name__)
CORS(app)

scap_status = 0


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movies', methods=['GET'])
def get_movies():   
    with open('List_250movies.json', 'r') as json_file:
        movies_data = json.load(json_file)
    return jsonify(movies_data)

@app.route('/scaping', methods=['GET'])
def get_scaping():
    global scap_status
    if scap_status == 0 :
        scap_status = 1
        try:
            # scrap.scap()
            time.sleep(60)
            scap_status = 0
            return jsonify({"message": "Scraping completed successfully."}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return "Gonna scaping"

@app.route('/status', methods=['GET'])
def get_status():
    global scap_status
    print(scap_status)
    return f"{scap_status}"

@app.route('/download')
def download_file():
    file_path = 'List_250movies.json'
    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
