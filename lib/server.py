# encoding:utf-8
__author__ = 'zhxia'

import redis
import msgpack

VERSION = r'2.0'


class RedisRpcServer(object):
    def __init__(self, host='127.0.0.1', port=6379, serviceName='default'):
        self.serviceName = serviceName
        self.redis = redis.StrictRedis(host, port)

    def setDelegate(self, delegate):
        self.delegate = delegate

    def start(self):
        print 'sever is running...'
        while True:
            try:
                channel, request = self.redis.brpop(self.serviceName)  # 此处返回的是一个元组
                if request:
                    request = msgpack.unpackb(request, encoding='utf-8')
                    print 'data:', request
                    reqId = request[1]
                    method = request[2]
                    params = request[3]
                    result = getattr(self.delegate, method)(*params)  # params 前必须加*，否则被当做第一个参数处理，类似于指针
                    reply = (VERSION, reqId, result)
                    self.redis.lpush(reqId, msgpack.packb(reply, use_bin_type=True))
                    self.redis.expire(reqId, 30)
            except:
                pass
