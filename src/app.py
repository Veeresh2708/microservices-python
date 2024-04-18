from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return str(host_name), str(host_ip)
    except:
        print("Unable to get Hostname and IP")

"""@app.route("/hostdetails")
def hostdetails():
    return get_Host_name_IP()
"""
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(status = "UP")

@app.route("/veer")
def veer():
    host_name,host_ip  = get_Host_name_IP()
    return render_template('index.html',HOST_NAME=host_name, HOST_IP=host_ip )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
