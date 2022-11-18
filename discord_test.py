import requests
import json
import random
import time
import os
# author : 二娃玩转区块链
# 视频教程在：YouTube ：https://www.youtube.com/watch?v=XQfhTPm_FJo （感谢支持，多多点赞）
# ➡️ 进discord 更多优质内容 ： https://discord.com/invite/RHtf7V6Z5G  （快讯推送，每日优质资料爬取，分类聊天。一站式服务）
# 作者更多优质内容：https://linktr.ee/erwaplayblockchain
def basic_context():
    context_list = [
    "great!","hello bro","let's go !","to the moon!","gm","couldn't sleep","have a good day","gm bro","!!!!","hello all","welcome everyone","thanks"
    ]
    text = random.choice(context_list)
    return text
def get_context(auth,chanel_id):
    headr = {
        "Authorization": auth,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    chanel_id = chanel_id
    url = "https://discord.com/api/v9/channels/{}/messages?limit=100".format(chanel_id)
    print(url)
    res = requests.get(url=url, headers=headr)

    result = json.loads(res.content)
    result_list = []
    #print(result)
    for context in result:
        if result != {'message': 'Missing Access', 'code': 50001}:
            if ('<') not in context['content'] :
                #print(2)
                if ('@') not in context['content'] :
                    if ('http') not in context['content']:
                        if ('?') not in context['content']:

                            result_list.append(context['content'])
                            if '' in result_list:
                                result_list.remove('')
        else:  return 'gm'
    #print(result_list)
    return random.choice(result_list)
def chat(chanel_list,authorization):
      header = {
          "Authorization": authorization,
          "Content-Type": "application/json",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
      }
      for chanel_id in chanel_list:
          msg = {
              #"content": basic_context(),
              "content": get_context(authorization,chanel_id),
              "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
              "tts": False,
          }
          url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
          try:
              res = requests.post(url=url, headers=header, data=json.dumps(msg))
              print(res.content)
              print(get_context(authorization,chanel_id))
          except Exception as ex:
              print("2出现如下异常%s" % ex)
              
              pass
          continue
      time.sleep(random.randrange(10, 30))
if __name__ == "__main__":
    chanel_list = os.environ['CHANEL_LIST1']  # 这里是群聊号（url最右边）
    authorization_list = os.environ['AUTHORIZATION_LIST1'] # 这里auth认证信息
    print(os.environ['TEST'])
    while True:
        try:
            chat(chanel_list,authorization_list)
            sleeptime = random.randrange(21600, 28800) #发送间隔时间(秒)
            time.sleep(sleeptime)
        except Exception as ex:
            print("出现如下异常%s" % ex)
            break
