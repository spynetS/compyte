#!/usr/bin/env python3

from skibidi import *

asd = open('tests/output.html','w')
asd.write(parse(open("tests/index.html","r").read()))
