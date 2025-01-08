from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    print("有收到")
    data = request.json
    username = data.get('username')
    print(username)
    # 在這裡可以將 username 存儲到 session 或資料庫
    return jsonify({'message': 'Login successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)