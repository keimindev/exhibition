from flask import Flask, render_template, jsonify, request
import requests
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


# 코딩 시작
@app.route('/')
def home():
    exhibition = list(db.exhibition.find({}, {'_id':False}))

    return render_template("index.html", exhibition=exhibition)


#
# @app.route('/list', methods=['GET'])
# def show_exhibitions():
#     exhibition = list(db.exhibition.find({}, {'_id':False}))
#     return jsonify({'exhi_list': exhibition})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)