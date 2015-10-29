# encoding:utf-8
__author__ = 'zhxia'

import redis
import uuid
import msgpack

VERSION = r'2.0'


class RedisRpcClient(object):
    def __init__(self, serviceName='default', host='127.0.0.1', port=6379):
        self.serviceName = serviceName
        self.redis = redis.StrictRedis(host, port)

    def getRedisConf(self):
        pass

    def sendRequest(self, method, params=(), timeout=1):
        '''
        :param method:
        :param reqParams:
        :param timeout:
        :return:
        '''
        reqParams = (
            VERSION,
            str(uuid.uuid1()),
            method,
            params
        )
        data = msgpack.packb(reqParams)
        self.redis.lpush(self.serviceName, data)
        try:
            channel, response = self.redis.brpop(reqParams[1], timeout)
            version, reqId, reply = msgpack.unpackb(response, encoding='utf-8')
        except:
            reply = None
        return reply
