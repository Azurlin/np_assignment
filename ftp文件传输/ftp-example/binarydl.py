#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter17/binarydl.py

import os
from ftplib import FTP

def main():
    if os.path.exists('proftpd-1.2.10rc1.tar.bz2.md5'):
        raise IOError('refusing to overwrite your proftpd-1.2.10rc1.tar.bz2.md5 file')

    ftp = FTP('ftp1.at.proftpd.org')
    ftp.login()
    ftp.cwd('/historic/source/')
    #print('size is:', ftp.size('/historic/source/proftpd-1.2.10rc1.tar.bz2.md5'))
    with open('proftpd-1.2.10rc1.tar.bz2.md5', 'wb') as f:
        ftp.retrbinary('RETR proftpd-1.2.10rc1.tar.bz2.md5', f.write)

    ftp.quit()

if __name__ == '__main__':
    main()