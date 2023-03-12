
class StringVar:
    def __init__(self):
        self.s = ''
    def set(self, data):
        self.s = data
    def get(self):
        return self.s

s = StringVar()
print(s.set('new word'))
print(s.get())
print(s.set('another word'))
print(s.get())