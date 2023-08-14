#UTF8编码
#-*-coding:utf-8-*-

#获取QQ群成员列表
#一次最多搜索40个


#获取配置信息
def get_config():
    with open('./config.yaml', 'r', encoding='utf-8') as fp:
        config = yaml.load(fp, Loader=yaml.FullLoader)
        User_Agent = config['User-Agent']
        Group_Id1 = config['Group_Id1']
        Group_Id2 = config['Group_Id2']
    
    return Group_Id1, Group_Id2, User_Agent


import requests
import json
import time
import yaml
from concurrent.futures import ThreadPoolExecutor

def get_group_members(group_id, bkn, headers, post_url, cookie):
    members = []
    total_count = 100
    search_count = 0
    search_addition = 40

    while search_count < total_count:
        data = {
            'gc': group_id,
            'st': search_count,
            'end': min(search_count + search_addition, total_count - 1),
            'sort': '0',
            'bkn': bkn
        }
        response = requests.post(url=post_url, headers=headers, data=data, cookies=cookie)
        json_data = response.json()
        total_count = json_data['search_count']
        mems = json_data['mems']
        members.extend(mem['nick'] for mem in mems)
        search_count += search_addition + 1
        time.sleep(2)  # 控制请求间隔

    return members

def get_common_group_members(bkn, cookie):
    # ... 读取配置信息 ...
    configs = get_config()
    post_url = 'https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'
    headers = {
        'User-Agent': configs[2],
    }

    with ThreadPoolExecutor(max_workers=2) as executor:
        group_id1 = configs[0]
        group_id2 = configs[1]
        future_group1 = executor.submit(get_group_members, group_id1, bkn, headers, post_url, cookie)
        future_group2 = executor.submit(get_group_members, group_id2, bkn, headers, post_url, cookie)

        QQ_Ids_1 = future_group1.result()
        QQ_Ids_2 = future_group2.result()

    common_members = set(QQ_Ids_1) & set(QQ_Ids_2)
    print("两个群的公共成员为:", common_members)

# if __name__ == "__main__":
#     main()
