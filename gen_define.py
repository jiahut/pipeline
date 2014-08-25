#!/usr/bin/env python
import string
import random
import sys

generators = {}

def register(the_type):
    def _generator(func):
        generators[the_type] = func
        return func
    return _generator

@register("str")
def str_generator(count=1, size=6, char_set=string.ascii_letters + string.digits):
    for _ in range(count):
        yield "".join(random.choice(char_set) for _ in range(size))

@register("int")
def int_generator(count=1, begin=1, end=101, is_fill=False):
    _len = len(str(end))
    for _ in range(count):
        if is_fill:
            yield str(random.randrange(begin,end)).zfill(_len)
        else:
            yield str(random.randrange(begin,end))


@register("file")
def file_generator(count=1, path="not_found.seed"):
    lines = [line.strip() for line in open(path,"r").readlines()]
    for _ in range(count):
        yield random.choice(lines)

def generator(count, the_type, *args):
    # if the_type == 'int':
    #     return int_generator(count, *args)
    # elif the_type == "str":
    #     return str_generator(count, *args)
    return generators[the_type](count, *args)
