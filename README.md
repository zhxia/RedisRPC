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