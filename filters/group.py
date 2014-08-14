import re

class Group:

    def __init__(self, pattern, options):
        self.options = options
        self.pattern = re.compile(pattern)


    def step(self, line):
        res = re.match(self.pattern, line)
        if res:
            return "\t".join(res.groups())
