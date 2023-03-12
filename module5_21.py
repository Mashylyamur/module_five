import json
data = {}
with open('model.json', 'w') as f:
    json.dump(data, f)
class Model:
    pass
    def save(self):
        with open('model.json', 'r') as f:
            data = json.load(f)
            data = dir(Model)
        with open('model.json', 'w') as f:
            json.dump(data, f)
s = Model()
s.save()

