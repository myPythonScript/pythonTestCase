'''获取数据'''
import yaml
import os
import json

class Data(object):
    def __init__(self,file_data):
        self.base_path = os.path.dirname(os.path.abspath(file_data))
        self.file_path = os.path.join(self.base_path, 'data', file_data)
        print(self.file_path)
    def from_yaml(self):
        with open(self.file_path,encoding = 'utf-8') as f:
            yaml_data = yaml.safe_load(f)
        return yaml_data

    def from_json(self):
        with open(self.file_path,encoding = 'utf-8') as f:
            json_data = json.load(f)
        return json_data

# if __name__ == '__main__':
#     d = Data("data.yaml")
#     data = d.from_yaml()
#     print(data)
#     print(data[2]['data']['CardInfo']['cardNumber'])