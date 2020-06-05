#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter17/asciidl.py
# Downloads README from remote and writes it to disk.

import os
from ftplib import FTP

def main():
    if os.path.exists('README'):
        raise IOError('refusing to overwrite your README file')
    print('ok')
    ftp = FTP('ftp1.at.proftpd.org')
    ftp.login()
    print('ok')
    ftp.cwd('/historic/source/')
    
    with open('proftpd-1.2.10rc1.tar.gz', 'w', encoding='utf-8') as f:
        def writeline(data):
            f.write(data)
            f.write(os.linesep) #给出当前平台使用的行终止符,例如,Windows使用'\r\n'

        ftp.retrlines('RETR proftpd-1.2.10rc1.tar.gz', writeline)
        
    ftp.quit()

if __name__ == '__main__':
    main()
