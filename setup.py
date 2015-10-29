from distutils.core import setup

setup(
    name='RedisRpc',
    version='1.0.0',
    packages=['redisrpc'],
    url='http://www.cnblogs.com/xiazh/',
    license='LICENSE.txt',
    author='zhxia',
    author_email='zhxia84@gmail.com',
    description='redis rpc service',
    install_requires=[
        "pyzmq >= 2.1.7"
    ]
)
