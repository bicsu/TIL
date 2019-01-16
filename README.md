# 기억하고 싶은 것들 메모하기

#### 1. jupyter code 실행 시간 Check

```python
import time

start_vect=time.time()

# Your codes!!!!!!!!!!!!!!!!!!!!!!!

print("training Runtime: %0.2f Minutes"%((time.time() - start_vect)/60))


```



#### 2. putty jupyter notebook

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





