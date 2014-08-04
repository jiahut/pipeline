#!/usr/bin/env python
import copy
import sys
import re
from gen_define import *

tpl_path, __size = sys.argv[1:]
count = int(__size)

def convert(s):
    try:
        return int(s)
    except:
        if s == "True":
            return True
        elif s == "False":
            return False
        else:
            return s

if __name__ == "__main__":
    with open(tpl_path,"r") as f:
      tpl = f.read().strip()
    names = re.findall('''(\$.*?)\((.*?)\)''',tpl)

    for name,args in names:
        argv = [ convert(x) for x in args.split(",")]
        argv.insert(0, count)
        _name_gen = generator(*argv)
        exec("%s_gen = _name_gen"%name[1:])
    del _name_gen
    tpl = re.sub('''\(.*?\)''',"",tpl)
    for _ in range(count):
        variables = copy.copy(locals())
        for _ in variables:
            if _.endswith("_gen"):
                exec "%s = %s.next()"%(_[0:-4], _)
        print(string.Template(tpl).substitute(**locals()))
