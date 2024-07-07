#!/usr/bin/env python3
# Author ID: ACimafranca

try:
    abc = 'non_existent_file.txt'  # Define abc to avoid NameError
    f = open(abc, 'r')
    f.write('hello world\n')
    f.close()
except (FileNotFoundError, PermissionError):
    print('file does not exist or wrong permissions')
except IsADirectoryError:
    print('file is a directory')
except OSError:
    print('unable to open file')
except:
    print('unknown error occured')
    raise
