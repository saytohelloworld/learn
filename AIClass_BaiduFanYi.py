import requests
import json
from hashlib import md5


# 获取输入
def getInput():
    global query
    global to

    query = str(input('请输入待翻译的内容 (hello)：'))
    while query == '':
        query = str(input('请输入待翻译的内容 (hello)：'))

    to = str(input('请输入翻译后的语言 (zh,en...)：'))
    while to == '':
        to = str(input('请输入翻译后的语言 (zh,en...)：'))


# 生成签名
def getSign(a, b, c, d):
    sign_str = (a + b + c + d).encode('utf-8')
    return md5(sign_str).hexdigest()


# 请求数据
def post(data, headers):
    req = requests.post(API_Baidu, data=data, headers=headers)

    res = req.json()
    # # indent 缩进, ensure_ascii 不对中午进行 Ascii 编码
    # print('\n', json.dumps(res, indent=2, ensure_ascii=False))

    print('翻译为', data['to'], '的内容是：', res["trans_result"][0]['dst'], '\n')


if __name__ == "__main__":
    # 百度翻译的 API 请求地址
    API_Url = 'https://fanyi-api.baidu.com'
    API_Path = '/api/trans/vip/translate'
    API_Baidu = API_Url + API_Path

    # 百度翻译开发者信息
    API_APPID = '20230303001584108'
    API_KEY = 'EucA7Sf0JGEajuH2Lq1n'

    # 随机的 Salt 值
    API_SALT = 'mnOtwZlPJh'

    while 1:
        getInput()

        # 请求头
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # 请求体
        data = {
            'q': query,
            'from': 'auto',
            'to': to,
            'appid': API_APPID,
            'salt': API_SALT,
            'sign': getSign(API_APPID, query, API_SALT, API_KEY)
        }

        post(data, headers)
