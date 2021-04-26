# -*- coding: UTF-8 -*-
import io
import socket
import sys


class WSGIServer(object):
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address):
        # Create a listening socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        # Allow to reuse the same address
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind
        listen_socket.bind(server_address)
        # Activate
        listen_socket.listen(self.request_queue_size)
        # Get server host name and port
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        # Return headers set by Web framework/Web application
        self.headers_set = []

    def set_app(self, application):
        self.application = application

    def serve_forever(self):
        listen_socket = self.listen_socket
        while True:
            # 轮询获取客户端的TCP连接
            self.client_connection, client_address = listen_socket.accept()
            # 处理一个HTTP请求，然后关闭
            self.handle_one_request()

    def handle_one_request(self):
        request_data = self.client_connection.recv(1024)
        self.request_data = request_data = request_data.decode('utf-8')
        # Print formatted request data a la 'curl -v'
        print(''.join(
            f'< {line}\n' for line in request_data.splitlines()
        ))

        self.parse_request(request_data)

        # 把原始的HTTP请求变成dict字典
        env = self.get_environ()

        # 这里就是WSGI协议部分
        # 传入包含请求信息的dict对象和回调函数start_response
        result = self.application(env, self.start_response)

        # Construct a response and send it back to the client
        self.finish_response(result)

    def parse_request(self, text):
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip('\r\n')
        # Break down the request line into components
        (self.request_method,  # GET
         self.path,  # /hello
         self.request_version  # HTTP/1.1
         ) = request_line.split()

    def get_environ(self):
        env = {}
        # The following code snippet does not follow PEP8 conventions
        # but it's formatted the way it is for demonstration purposes
        # to emphasize the required variables and their values
        #
        # Required WSGI variables
        env['wsgi.version'] = (1, 0)
        env['wsgi.url_scheme'] = 'http'
        env['wsgi.input'] = io.StringIO(self.request_data)
        env['wsgi.errors'] = sys.stderr
        env['wsgi.multithread'] = False
        env['wsgi.multiprocess'] = False
        env['wsgi.run_once'] = False
        # Required CGI variables
        env['REQUEST_METHOD'] = self.request_method  # GET
        env['PATH_INFO'] = self.path  # /hello
        env['SERVER_NAME'] = self.server_name  # localhost
        env['SERVER_PORT'] = str(self.server_port)  # 8888
        return env

    def start_response(self, status, response_headers, exc_info=None):
        # Add necessary server headers
        server_headers = [
            ('Date', 'Mon, 15 Jul 2019 5:54:48 GMT'),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers + server_headers]
        # To adhere to WSGI specification the start_response must return
        # a 'write' callable. We simplicity's sake we'll ignore that detail
        # for now.
        # return self.finish_response

    def finish_response(self, result):
        try:
            status, response_headers = self.headers_set
            response = f'HTTP/1.1 {status}\r\n'
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'
            for data in result:
                response += data.decode('utf-8')
            # Print formatted response data a la 'curl -v'
            print(''.join(
                f'> {line}\n' for line in response.splitlines()
            ))
            response_bytes = response.encode()
            self.client_connection.sendall(response_bytes)
        finally:
            self.client_connection.close()


SERVER_ADDRESS = (HOST, PORT) = '', 8888


def make_server(server_address, application):
    server = WSGIServer(server_address)
    server.set_app(application)
    return server


# if __name__ == '__main__':
#     if len(sys.argv) < 2:
#         sys.exit('Provide a WSGI application object as module:callable')
#     # 获取python my_wsgi_server.py后面的第一个参数
#     app_path = sys.argv[1]
#     module, application = app_path.split(':')
#     # myapp
#     module = __import__(module)
#     # myapp.application
#     application = getattr(module, application)
#     # 创建http服务器
#     httpd = make_server(SERVER_ADDRESS, application)
#     print(f'WSGIServer: Serving HTTP on port {PORT} ...\n')
#
#     httpd.serve_forever()

    from flask import Flask


# -*- coding: utf-8
import threading
locks = threading.local()
locks.redis = {}
def key_for(user_id):
    return "account_{}".format(user_id)

def _lock(client, key):
    return bool(client.set(key, True, nx=True, ex=5))

def _unlock(client, key):
    print("=",client.get(key))
    client.delete(key)

def lock(client, user_id):
    key = key_for(user_id)
    print(locks.redis)
    if key in locks.redis:
        locks.redis[key] += 1
        return True
    ok = _lock(client, key)
    if not ok:
        return False
    locks.redis[key] = 1
    return True

def unlock(client, user_id):
    key = key_for(user_id)
    if key in locks.redis:
        locks.redis[key] -= 1

        if locks.redis[key] <= 0:
            del locks.redis[key]
        return True
    return False
# client = redis.StrictRedis()
# print ("lock", lock(client, "codehole"))
# print ("lock", lock(client, "codehole"))
# print ("unlock", unlock(client, "codehole"))
# print ("unlock", unlock(client, "codehole"))

# an example of python decorator
def deco1(func):
    print(1)
    def wrapper1():
        print(2)
        func()
        print(3)
    print(4)
    return wrapper1

def deco2(func):
    print(5)
    def wrapper2():
        print(6)
        func()
        print(7)
    print(8)
    return wrapper2
#
# @deco2
# @deco1
# def func():
#     print('This is func')

def decorator_02(func):
    print(3)
    def inner_02(*args):
        print(4)
        func(*args)
        print(7)
    return inner_02

def decorator_01(num):
    def outer(func):
        print(2)
        def inner_01(*args):
            func(*args)
            for i in range(num):
                print(6)
        return inner_01
    print(1)
    return outer

@decorator_02
@decorator_01(1)
def my_func(*args):
    print(5)

# my_func('hello,world', 'hello,python')
# print(my_func.__name__)

#https://www.jianshu.com/p/c7cc96b38d8e 多重装饰器



class Single:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super().__new__(cls)

        return  cls._instance


# s1= Single()
# s2 = Single()
#
# print(id(s1),id(s2))


f = map(lambda li: li*2, [1,2,3,4,5])
# print(list(f))
import random
print(random.random())

ct={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

import collections
s = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"

rst = collections.Counter(s)
print(list(filter(lambda x:x%2,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
a=(1,)
b=(1)
c=("1")

rst = [1,5,7,9]
rst2 = [2,2,6,8]


x="abc"
y="def"
z=["d","e","f"]

#daebfc
#

class A(object):
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')


class D(B):
    def test(self):
        print('from D')


class E(C):
    def test(self):
        print('from E')


class F(D, E):
    # def test(self):
    #     print('from F')
    pass


f1 = F()
f1.test()
print(F.__mro__)  #

from werkzeug.local import Local, LocalStack
import threading, time

my_stack = LocalStack()
my_stack.push(1)
print('in main thread after push, value is:' + str(my_stack.top))


def worker():
    print('in new thread before push , value is:' + str(my_stack.top))  # 因为线程隔离，所以为None
    my_stack.push(2)
    print('in new thread after push , value is:' + str(my_stack.top))


new_t = threading.Thread(target=worker, name='localstack_thread')
new_t.start()

time.sleep(1)

print('finally, in main thread , value is : {}'.format(my_stack.top))



def quit_sort(listData):
    _len = len(listData)
    if _len < 2:
        return listData

    _tempData = listData[0]
    _leftList = []
    _rightList = []

    for i in range(1,_len):
        if listData[i] <_tempData:
            _leftList.append(listData[i]);
        else:
            _rightList.append(listData[i]);
    return quit_sort(_leftList) + [_tempData] + quit_sort(_rightList)






rst = Solution()
tt = rst.lenStr("abcabcbb")
print(tt)