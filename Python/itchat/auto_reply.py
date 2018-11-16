import requests
from wxpy import *
import json


# 图灵机器人
def talks_root(info = '你叫什么名字' ):
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = 'APIKey'
    data = {'key' : apikey,
            'info' : info }
    req = requests.post(api_url, data=data_).text
    replys = json.load(req)['text']
    return replys
    
# 微信自动回复

robot = Robot()

# 回复来自其他好友，群聊和公众号的消息
@robot.resister()
def reply_my_friend(msg):
    message = '{}'.format(msg.text)
    replys = talks_root(info=message)
    return replys

# 开始监听和自动处理消息
robot.start()






