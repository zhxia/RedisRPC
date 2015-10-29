# RedisRPC
use redis implement Remote Procedure Call Protocol

### example: ###
client.py

```python
from redisrpc.client import RedisRpcClient

if __name__ == '__main__':
    rpcClient = RedisRpcClient()
    print rpcClient.sendRequest('sum', (1, 2, 3, 4))
    print rpcClient.sendRequest('getTime')

```
output:
> data: [u'2.0', u'b55a1b84-7df5-11e5-96c0-080027b4ecc6', u'sum', [1, 2, 3, 4, 7, 8, 9, 10]]
> data: [u'2.0', u'b55a414a-7df5-11e5-96c0-080027b4ecc6', u'getTime', []]

server.py

```python
from redisrpc.server import RedisRpcServer
from model import test

if __name__ == '__main__':
    rpcServer = RedisRpcServer()
    rpcServer.setDelegate(test())
    rpcServer.start()
```

model.py
```python
import time

class test(object):
    def sum(self, *params):
        total = 0
        for it in params:
            total += it
        return total

    def getTime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
```