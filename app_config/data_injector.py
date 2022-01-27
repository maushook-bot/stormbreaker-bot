"""
CLASS: Data Injection from setting.json
"""
import json


class DataInjection:
    def __init__(self):
        with open("settings.json") as json_file:
            self.resource = json.load(json_file)
        print('Resource Initialized')

    def get_resource(self):
        return self.resource
