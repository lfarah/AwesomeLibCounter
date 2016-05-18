import os
from flask import Flask,redirect
import re
import urllib, json
import base64
from flask import jsonify
app = Flask(__name__)

@app.route('/', methods=['POST'])
def refresh():
	client_id = "9125bb5527815f9fe111"
	client_secret = "2e47088bcd09d03431aaee34603be902be689924"
	url = "https://api.github.com/repos/vsouza/awesome-ios/contents/README.md?ref=master&client_id=" + client_id + "&client_secret=" + client_secret
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	text_file = open("README.md", "w+")
	text_file.write(str(base64.b64decode((data["content"]))))
	text_file.close()
	return jsonify(result={"status": 200})

@app.route('/swift')
def hello():
	f2 = open("README.md","r")
	text = f2.readlines()
	swiftCount = 0
	for line in text[138:]:
		if "*" in line:
			if ":large_orange_diamond:" in line:
				swiftCount += 1
	url = "https://img.shields.io/badge/swift_projects-" + str(swiftCount) + "-orange.svg"
	return redirect(url, code=302)

@app.route('/objc')
def objc():
	f2 = open("README.md","r")
	text = f2.readlines()
	ObjCCount = 0
	for line in text[138:]:
		if "*" in line:
			if ":large_orange_diamond:" not in line:
				ObjCCount += 1
	url = "https://img.shields.io/badge/objc_projects-" + str(ObjCCount) + "-blue.svg"
	return redirect(url, code=302)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)