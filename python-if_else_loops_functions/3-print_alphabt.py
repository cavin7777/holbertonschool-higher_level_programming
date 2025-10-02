#!/usr/bin/python3
from itertools import chain

alpha_ex = chain(range(97, 101), range(102, 113), range(114, 123))
for i in alpha_ex:
    print('{}'.format(chr(i)), end="")
