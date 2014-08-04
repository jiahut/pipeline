#!/usr/bin/env python
import string
import random
import sys


def str_generator(count=1, size=6, char_set=string.ascii_letters + string.digits):
    for _ in range(count):
        yield "".join(random.choice(char_set) for _ in range(size))

def int_generator(count=1, begin=1, end=101, is_fill=False):
    _len = len(str(end))
    for _ in range(count):
        if is_fill:
            yield str(random.randrange(begin,end)).zfill(_len)
        else:
            yield str(random.randrange(begin,end))

def generator(count, the_type, *args):
    if the_type == 'int':
        return int_generator(count, *args)
    elif the_type == "str":
        return str_generator(count, *args)
