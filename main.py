#!/usr/bin/env python3

from compyte import *

output = open('tests/output.html','w')
output.write(parse(open("tests/index.html","r").read(),{}))
