#!/usr/bin/python3
import requests
import os

test_name = '购物车修改满赠商品'
project = '1'
username = 'admin'
password = '123456'
time_out_ms = 1000


def mail_msg(test_result):
    msg = []
    records = test_result['details'][0]['records']
    if not test_result['success']:
        msg.append('%s测试失败' % test_name)
        for record in records:
            status = record['status']
            if status != 'success':
                url = record['meta_data']['request']['url']
                msg.append('%s\n页面测试失败' % url)
    else:
        for record in records:
            response_time_ms = record['meta_data']['response']['response_time_ms']
            if response_time_ms >= time_out_ms:
                url = record['meta_data']['request']['url']
                if not msg:
                    msg.append('%s页面超时' % test_name)
                msg.append('{}\n页面超时{}ms'.format(url, response_time_ms))
    if msg:
        msg.append('请登录测试平台查看报告')
        msg.append('http://10.1.2.12:8082/#/fastrunner/login')
    return msg


payload_login = {'username': username, 'password': password}
r1 = requests.post('http://10.1.2.12:9000/api/user/login/', data=payload_login)
token = r1.json()['token']
payload_test = {'token': token, 'project': project, 'name': test_name}
r2 = requests.get('http://10.1.2.12:9000/api/fastrunner/run_testsuite_pk/6/', params=payload_test)
dict_test_result = r2.json()
message = mail_msg(dict_test_result)
if message:
    title = message[0]
    message.pop(0)
    message = '\n'.join(message)
    os.environ['title'] = title
    os.environ['message'] = message
    cmd = 'echo -e "$message"|mail -s $title xxx@dingtalk.com'
    os.system(cmd)
