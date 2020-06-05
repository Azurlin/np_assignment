# -*- coding: utf-8 -*-
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
# 新建一个用户组
authorizer = DummyAuthorizer()
# 添加用户名，密码，指定目录，权限 
authorizer.add_user("fff", "123456", "F:", perm="elradfmwM")  # adfmw
# 这个是添加匿名用户,任何人都可以访问
#authorizer.add_anonymous("E:/", perm='l')
handler = FTPHandler
handler.authorizer = authorizer
# 开启服务器
server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()