import json
class Model:
    def __init__(self):
        self.title = '1'
        self.text = '2'
        self.author = '3'
    def save(self):
        data = self.__dict__
        with open('model.json', 'w') as f:
            json.dump(data, f)
s = Model()
s.save()


