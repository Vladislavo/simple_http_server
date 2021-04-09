from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def display():
    return "Looks like it works!"

@app.route('/alarm', methods=['POST'])
def alarm():
    print(request.data)
    return '', 200

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)