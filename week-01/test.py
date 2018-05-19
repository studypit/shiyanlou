class Test:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Test: {}'.format(self.name)

t = Test('python')
print(t)
print(t.name)
