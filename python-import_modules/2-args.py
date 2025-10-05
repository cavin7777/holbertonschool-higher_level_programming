#!/usr/bin/python3

import sys
  
argv = sys.argv[1:]
argc = len(argv)

if argc == 0:
    print('0 arguments.')
else:
    if argc == 1:
        print('1 argument:')
    else:
        print('{} arguments:'.format(argc))
    for i in range(argc):
        print('{} : {}'.format(i + 1, argv[i]))
