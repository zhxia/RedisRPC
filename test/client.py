__author__ = 'zhxia'

from redisrpc.client import RedisRpcClient

if __name__ == '__main__':
    rpcClient = RedisRpcClient()
    print rpcClient.sendRequest('sum', (1, 2, 3, 4))
    print rpcClient.sendRequest('getTime')
