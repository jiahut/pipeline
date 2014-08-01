import io

class In:
    # def setup(self):
    #     pass

    # def release(self):
    #     pass

    def __init__(self, file_name):
        _set = []
        self._range = set()
        for line in io.open(file_name,"r").readlines():
            line = line.strip()
            _set.append(line)
            self._range.add(len(line))
        self._set = set(_set)


    def check(self, line):
        has = False
        for idx in self._range:
            if line[:idx] in self._set:
                has = True
        return has