### Python으로 메일 보내기

```python
import smtplib
smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)
# 서버 연결을 설정하는 단계
smtp_gmail.ehlo()
# 연결을 암호화
smtp_gmail.starttls()
#로그인
smtp_gmail.login('<yourID>@gmail.com','<password>')
from email.message import EmailMessage
msg=EmailMessage()
 
# 제목 입력
msg['Subject']="test합친거csv임니다"
 
# 내용 입력
msg.set_content("test합친거입니다.")
 
# 보내는 사람
msg['From']='sender@naver.com'
 
# 받는 사람
msg['To']='reciever@naver.com'
# 보내기
file='./csv/abc.csv'
fp = open(file,'rb')
file_data=fp.read()
msg.add_attachment(file_data,maintype='text',subtype='plain',filename="abcd.csv")
smtp_gmail.send_message(msg) # 실질적 보내기

#에러가 날 시에 구글링 ㄱㄱ port를 바꾸거나, google 계정 보안 낮추기
```

