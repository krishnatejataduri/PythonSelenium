import json

class JsonUtil:

    def __init__(self,file_path):
        self.file_path = file_path
        self.data = None

    def load_json(self):
        with open(self.file_path,'r') as json_file:
            self.data = json.load(json_file)
            return self.data

