REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'

def redis_config():
    try:
        rd = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

    except:
        print("redis connection failure")