from flask import Flask
app = Flask(__name__)

@app.route('/')   # 这个根目录，就是127.0.0.1:5000进入的位置
def hello_world():
	return "hello world"

if __name__ == '__main__':
	app.run()
