import requests
import json
 
#配置参数入口
haidilao_cookies = ['2760828916934539592052190e8d6b9ea0e1a69c8b7e0b724ff6de186d91c3','2760828316935326968722942e60a3aaa340a386a124d2d17892a9311fbea7','276082a716935787476095366e1d02f5ef6d30488fed08cd487076c25a38b0']
haidilao_token = ['TOKEN_APP_f798497e-1fe7-4b7f-b883-b007a86c6958','TOKEN_APP_ccc950d9-f8df-4e8d-a599-d94cab3295bf','TOKEN_APP_af014df4-0875-44c6-b0e7-e21c962c2fb8']



for index in range(len(haidilao_token)):
    ck = {
    'acw_tc': haidilao_cookies[index],
    }
 #登录账号   
    headers1 = {
    'Host': 'superapp-public.kiwa-tech.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '10',
    'appId': '15',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    '_HAIDILAO_APP_TOKEN': haidilao_token[index],
    # 'Accept-Encoding': 'gzip,compress,br,deflate',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.40(0x18002831) NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wx1ddeb67115f30d1a/81/page-frame.html',
    }
    
    json_data1 = {
    'type': 1,
    }

    response1 = requests.post('https://superapp-public.kiwa-tech.com/activity/wxapp/applet/queryMemberCacheInfo', headers=headers1, json=json_data1)
    print("======== ",response1.json()['data']['mobile']," ========")

 #签到执行  
    headers2 = {
    'Host': 'superapp-public.kiwa-tech.com',
    'Accept': 'application/json, text/plain, */*',
    'ReqType': 'APPH5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Origin': 'https://superapp-public.kiwa-tech.com',
    'deviceId': 'null',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.40(0x18002831) NetType/WIFI Language/zh_CN miniProgram/wx1ddeb67115f30d1a',
    '_HAIDILAO_APP_TOKEN': haidilao_token[index],
    'Referer': 'https://superapp-public.kiwa-tech.com/app-sign-in/?SignInToken=TOKEN_APP_ccc950d9-f8df-4e8d-a599-d94cab3295bf&source=MiniApp',
    # 'Content-Length': '26',
    # 'Cookie': 'acw_tc=2760828916934539592052190e8d6b9ea0e1a69c8b7e0b724ff6de186d91c3',
    'Connection': 'keep-alive',
    }

    json_data2 = {
    'signinSource': 'MiniApp',
    }
    response2 = requests.post('https://superapp-public.kiwa-tech.com/activity/wxapp/signin/signin', cookies=ck,headers=headers2, json=json_data2)
    print(response2.json()['msg'])

#积分查询
    headers3 = {
    'Host': 'superapp-public.kiwa-tech.com',
    'ReqType': 'APPH5',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://superapp-public.kiwa-tech.com',
    'deviceId': 'null',
    'Content-Length': '0',
    '_HAIDILAO_APP_TOKEN': haidilao_token[index],
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.40(0x18002831) NetType/WIFI Language/zh_CN miniProgram/wx1ddeb67115f30d1a',
    'Referer': 'https://superapp-public.kiwa-tech.com/app-sign-in/?SignInToken=TOKEN_APP_ccc950d9-f8df-4e8d-a599-d94cab3295bf&source=MiniApp',
    # 'Cookie': 'acw_tc=2760828916934539592052190e8d6b9ea0e1a69c8b7e0b724ff6de186d91c3',
    'Connection': 'keep-alive',
    }

    response3 = requests.post('https://superapp-public.kiwa-tech.com/activity/wxapp/signin/queryFragment', cookies=ck, headers=headers3)
    print("积分余额：",response3.json()['data']['total'])

