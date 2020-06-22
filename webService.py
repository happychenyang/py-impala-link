#!/usr/lib/python2.7
#-*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
import json
from ImpalaLink import ImpalaLink
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # body = r'<h1>Hello, %s!</h1>'%(environ['PATH_INFO'][1:] or 'web')
    request_body = environ["wsgi.input"].read(int(environ.get("CONTENT_LENGTH", 0)))
    request_body = json.loads(request_body)
    hostip = str(request_body["hostip"])
    portnum = int(request_body["portnum"])
    sqlstrs = str(request_body["sqlstrs"])
    actions = str(request_body["actions"])
    #链接客户端信息
    opts = {
      'host': hostip,
      'port': portnum
    }
    client = ImpalaLink(opts)
    if actions == 'add':
        data_list = str(client.insert(sqlstrs))
    elif actions == 'query':
        data_list = str(client.query(sqlstrs))
    elif actions == 'queryone':
        data_list = str(client.query_one(sqlstrs))
    elif actions == 'upload':
        data_list = str(client.update(sqlstrs))
    elif actions == 'delete':
        data_list = str(client.delete(sqlstrs))
    elif actions == 'execute':
        data_list = str(client.execute(sqlstrs,None))

    return data_list.encode('utf-8')

httpd = make_server('0.0.0.0', 8002, application)
print('Serving HTTP on port 8002...')
httpd.serve_forever()
