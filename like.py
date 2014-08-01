import re

class Like:
    # def setup(self):
    #     pass

    # def release(self):
    #     pass

    def __init__(self, pattern):
        self.pattern = re.compile(pattern)


    def check(self, line):
        return re.match(self.pattern,line) is not None
