import redis
import werobot
from werobot.session.redisstorage import RedisStorage

db = redis.Redis(host='120.92.51.158',password='redismima123',db=2)
session_storage = RedisStorage(db, prefix="wechat_")
robot = werobot.WeRoBot(token="ttttsdadfhjkdsfhjkhdskjf", enable_session=True,
                        session_storage=session_storage, app_id='wxe2e692448d474e1d',
                        encoding_aes_key='UsRKHwgRpLRE1ZUuphvWXfr3sxTOs2GYSXF9ZKQd1u4')

@robot.handler
def hello(message):
    return 'Hello World!'
