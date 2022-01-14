import schedule
import requests
import json
import time
from datetime import datetime


def kakaotalk_me():
    with open("kakao_code.json", "r") as fp:
        tokens = json.load(fp)

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    headers = {
        "Authorization": "Bearer " + tokens["access_token"]
    }

    now = datetime.now()
    now_re = str(now.month) + '월 ' + \
        str(now.day) + '일 ' + str(now.hour) + "시 " + str(now.minute) + "분 입니다."

    print(now_re)

    template = {
        "object_type": "text",
        "text": now_re,
        "link": {
            "web_url": "www.naver.com",
        },
    }

    data = {
        "template_object": json.dumps(template)
    }
    response = requests.post(url, headers=headers, data=data)
    response.status_code
    if response.json().get('result_code') != 0:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))

# 10초에 한번씩 실행
# schedule.every(10).second.do(job)
# 10분에 한번씩 실행
# schedule.every(10).minutes.do(job)
# 매 시간 실행
# schedule.every().hour.do(job)
# 매일 10:30 에 실행
# schedule.every().day.at("10:30").do(job)
# 매주 월요일 실행
# schedule.every().monday.do(job)
# 매주 수요일 13:15 에 실행
# schedule.every().wednesday.at("13:15").do(job)


schedule.every(3).minutes.do(kakaotalk_me)

while True:
    # schedule 모듈 자동화
    schedule.run_pending()
    time.sleep(1)
