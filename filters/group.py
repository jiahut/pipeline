import re

class Group:

    def __init__(self, pattern):
        self.pattern = re.compile(pattern)


    def check(self, line):
        res = re.match(self.pattern, line)
        if res:
            return "\t".join(res.groups())
