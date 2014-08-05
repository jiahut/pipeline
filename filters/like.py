import re

class Like:
    # def setup(self):
    #     pass

    # def release(self):
    #     pass

    def __init__(self, pattern):
        self.pattern = re.compile(pattern)


    def step(self, line):
        if re.match(self.pattern,line):
            return line.strip()
