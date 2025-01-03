import json

class secretmanager:
    def __init__(self):
        fileName = open("secret.json")
        self.secret = json.load(fileName)
        fileName.close
    def jsonify(self):
        return self.secret