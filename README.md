# 기억하고 싶은 것들 메모하기

#### 1. jupyter code 실행 시간 Check

```python
import time
from datetime import datetime
start_vect=time.time()

# Your codes!!!!!!!!!!!!!!!!!!!!!!!

print("training Runtime: %0.2f Minutes"%((time.time() - start_vect)/60))
print(datetime.today())        
```



#### 2. putty jupyter notebook

= 아래 6번에서 ssh설정을 먼저 해주시고 진행해주세요!!

- jupyter notebook --generate-config

```python
from notebook.auth import passwd
passwd()
'your pass word'
```

* jupyter config 파일 내에 아래 내용 수정(gedit ~/.jupyter/jupyter_config.py)
  + c.NotebookApp.password = u'your password'
  + c.NotebookApp.port = 8888
  + c.NotebookApp.ip = 'your IP(sever)'
  + c.NotebookApp.open_browser = False
  + c.NotebookApp.allow_remote_access = True
  + c.NotebookApp.password_required = True
  + c.NotebookApp.allow_origin = '' # 주석풀기

* putty에 ip, port 입력 후 SSH-tunnel 가서 8888, localhost:8888입력 후 'add' 클릭

* 혹시 안 될 시에는 방화벽을 내려보자..

  ```shell
  $ systemctl stop firewalld
  ```

* 접속하면 끗!!!!!!!!!!!



#### 3. chrome 환경변수 등록 폴더로 옮기기 ubuntu

* $ /opt/google/chrome # 이 위치에 'google-chrome' 실행 파일 확인

* ```shell
  $ sudo ln -s /opt/google/chrome/google-chrome /usr/bin/chrome
  ```

  위 명령어로 link를 걸어준다.

* 이 후에 어느 위치에서든 chrome 명령어로 web brower 실행한다.

  * tip 

```shell
		$ chrome <url 이름> 으로 바로 web으로 이동 가능
```



#### 4. anaconda 가상환경 활성화

```shell
conda create -n <가상환경 이름> python=<python version, ex)3.6>
```

* 가상환경 생성 위치: ~/anaconda3/envs/py35

* 가상환경 목록: $ conda info --envs

* ```vim ~/.bashrc```

  ```export PATH="/home/pirl/anaconda3/bin:$PATH```# 환경 변수 지정하기

* 콘다 내부의 패키지 리스트
  ```$ conda list 또는 conda list -n py35```

* 패키지 설치 (conda install package_name)
  `$ conda install python=2.7
  $ conda install scipy=0.15.0 curl -n py27
  $ conda install pandas`

* 패키지 업데이트
  ` conda update package_name`

* 패키지 삭제
  `$ conda remove -n py27 package_name`

* 가상환경 삭제
  `$ conda remove -n py27 --all`

* 7다중 커널 설치
  - Python2 를 추가   
    `$ conda create -n py27 python=2.7      
    $ source activate py27      
    $ conda install notebook ipykernel`
  
* `jupyter notebook --generate-config`
  ` c.NotebookApp.notebook_dir = ' ' `

###### Jupyter virtualenv 추가 및 삭제

```shell
## virtualenv 안에서

(py36) $ ipython kernel --user --name py36 #jupyter kernel에 추가
## window
$ python -m #을 붙여야함
(py36) $ jupyter kernelspec uninstall py36 # jupyter kernel에 삭제
```

#### 5. ubuntu  이런저런 설정

```shell
$ sudo apt-get install fcitx-hangul # 한글 세팅 → setting가서 ‘Hangul’로 수정(재부팅)

$ cd pycharm # 폴더 이동

$ ./pycharm.sh  # 설치
# 파일 지우기
$ dpkg --list #파일명 찾기 ex) avg.ext
$ sudo apt-get --purge remove <program name>
```

#### 6. ubuntu putty설정

```shell
$ dpkg -l | grep openssh
$ sudo apt-get update
$ sudo apt-get install openssh-server
$ dpkg -l | grep openssh #정상 설치 확인(openssh-server, openssh-sftp-server)
$ sudo service ssh start
$ service --status-all | grep + #여기에 ssh가 있으면 된 것
$ sudo netstat -antp # SSH 서비스가 몇 번 포트를 점유하고 있는지도 확인
$ 
```

#### 7. ubuntu 16.04 root 및 유저 변경

```shell
$ sudo su
$ su - <유저명 예)sam>
```

#### 8. pandas TIPs 

```python
pd.set_option('display.float_format', lambda x: '%.3f' % x)	
# set the options to see all columns, rows
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_info_columns', 1001)
import warnings
warnings.filterwarnings('ignore')
```

#### 9. Python으로 메일 보내기

```python
import smtplib
smtp_gmail = smtp
lib.SMTP('smtp.gmail.com', 587)
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

```

#### 10. Tensorflow 설치(Ubuntu)

```shell
# in System
$ pip3 install --user --upgrade tensorflow
# in VIRTUALENV
$ pip install --upgrade tensorflow
```



#### 11 .Ubuntu PSCP이용해 파일 전송 windows to Unbuntu

```shell
# 윈도우 자기가 원하는 folder에서
C:\directionyouwant>pscp -r -P <port> C:\yourfolder/* <username>@<ip or hostname>:/home/user/
# -r은 모든 폴더 및 파일 -P로 port를 명시화해서 잘 찾아갈 수 있게
# 위 명령어가 작동하면 ubunutu password를 입력하게 되고 그 후에 파일이 복사 된다.
```



#### 12 .Ubuntu의 그림판 kolourpaint설치

```shell
$ sudo apt-get install kolourpaint4
```

#### 13. Github markdown에 image 추가하기

```markdown
![Image description](link-to-image) 
* 이미지를 해당 repo에 올려서 address를 얻는다
```

#### 14. pip install 안될 때 가상환경에 직접 설치

```shell
$ pip install --target=/home/pirl/anaconda3/envs/tf/lib/python3.6/site-packages --upgrade pillow
$ conda install mysql-connector-python --name VENV_NAME
$ conda update mysql-connector-python --name VENV_NAME
```

#### 15. Ubuntu GUI folder 자세히보기로 변경

```shell
# Ubuntu16.04 folder detailed_view <'icon-view' and 'compact-view'>
$ gsettings set org.gnome.nautilus.preferences default-folder-viewer 'list-view'

```

#### 16. Excel 창분리

```
Excel 파일을 각각의 프로세스에서 실행하는 방법
a. 윈도우 시작 버튼을 클릭합니다. 
b. 검색 및 실행 창에 [regedit]를 입력합니다.
이미지

c. 레지스트리 편집기가 실행되면, 해당 폴더로 이동합니다.
(HKey_Classes_Root\Excel.Sheet.8\Shell\Open)
(HKey_Classes_Root\Excel.Sheet.12\Shell\Open) 
d. 해당 폴더를 선택한 후 마우스 우측 버튼을 클릭하여, [내보내기]를 통해서 레지스트리를 백업합니다.
(추후에 다른 문제가 발생할 경우 백업한 레지스트리를 실행하면, 기존 레지스트리 값이 재 등록됩니다.)
이미지

e. 백업이 완료되면, 다시 마우스 우측 버튼을 클릭하여, [삭제]를 통해서 레지스트리를 제거합니다.
이미지

f. 레지스트리 편집기를 종료하고, 바탕화면에서 마우스 우측 버튼을 클릭하여, [새로 만들기]의 [텍스트 문서]를 선택합니다.
이미지

g. 새로운 텍스트 문서를 2개 만들고 그 내용에 각가 아래 내용을 입력합니다.
----------------------------------------------------------------------------------------------------------

Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Excel.Sheet.12\shell\Open]
@="열기(&O)"

[HKEY_CLASSES_ROOT\Excel.Sheet.12\shell\Open\command]
@="\"C:\\Program Files\\Microsoft Office\\Office14\\EXCEL.EXE\" /m \"%1\""

-----------------------------------------------------------------------------------------

Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Excel.Sheet.8\shell\Open]
@="열기(&O)"

[HKEY_CLASSES_ROOT\Excel.Sheet.8\shell\Open\command]
@="\"C:\\Program Files\\Microsoft Office\\Office14\\EXCEL.EXE\" /m \"%1\""

-----------------------------------------------------------------------------------------

h.위 내용들을 입력한 후 확장자명을 *.txt에서 [*.reg]로 변경한 후 실행합니다. 
j. 새로 등록한 레지스트리 키값이 입력이 되면, Excel 프로그램을 실행하여 확인합니다.


```

from : https://answers.microsoft.com/ko-kr/office/forum/office_2010-excel/office-2010%EC%97%90%EC%84%9C/b5f473a9-f061-4097-9192-76be7031f24d

#### 사용 장비 cpu, gpu현황 tensorflow

```python
from tensorflow.python.client import device_lib
device_lib.list_local_devices()
```

#### Jupyter notebook extension

```shell
# conda
$ conda install -c conda-forge jupyter_contrib_nbextensions
$ jupyter notebook

> http://localhost:8888/nbextensions 들어가서 설정 후 enable
```

#### Jupyter notebook 글꼴 사이즈 바꾸기

* .jupyter/custom 폴더 만들어 custom.css 만들기.
  그 css파일 안에 아래 내용 작성

  ```css
  .CodeMirror pre {font-family: Arial; font-size: 14pt; line-height: 140%;}
  ```

  

