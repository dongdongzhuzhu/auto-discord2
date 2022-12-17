import requests
import json
import random
import time
import os
# author : 二娃玩转区块链..
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
    print(chanel_id)
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
    chanel_list = ["740814068935557163",'740814068935557164','740814068935557166', '819059519773736990','862475492002889748','864705879408246794',
                   '883217854546194432','883287724226916352', '891571476631789579','897511179377848380','899313816402276512','899760482561458197','899932595637329971',
                   '901143068873469953','901235030842552410', '903605039103352872','906543466555785237',
                   '910372685597528095','911109746898116658','912252690392838144','915081587492790313',
                   '920886369096699984','921398347879841853','922403805776199691','924214083052531712','924210559216418845','929161814393094205',
                   '931453788265525299','932795973711847434','936225038036791377','938191249440137256',
                   '940863791166529567','943788649370230794','944290639875559454','944619788301393990','948482522612895815',
                   '950660053285863435','952453754647621632','954870871640666112','958865963753828423','959650164358938664',
                   '963693484076834849','964347471386005584','964539807592247383','968153663589736478',
                   '970021993611137114','973787780171857950','973844093685862421','974135848582938656','974585251592544256', '975085512840855582','976388953915678761','976947544670212106','978630701333221428','978654918707671121',
                   '982928212512346122','982932759293067334','984290464972820530','986122385688252426','986765554356486205',
                   '990837939883900958','996003566307262464',
                   '1011284281835913266','1015137689844076617'] # 这里是群聊号（url最右边）     
    authorization_list = os.environ['AUTHORIZATION_LIST1'] # 这里auth认证信息
    #while True:
    try:
        chat(chanel_list,authorization_list)
       
            #sleeptime = random.randrange(18000,21600) #发送间隔时间(秒)
            #time.sleep(sleeptime)
    except Exception as ex:
        
        print("出现如下异常%s" % ex)

