__author__ = 'zhxia'

from redisrpc.server import RedisRpcServer
from model import test

if __name__ == '__main__':
    rpcServer = RedisRpcServer()
    rpcServer.setDelegate(test())
    rpcServer.start()
