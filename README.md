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
* 접속하면 끗!!!!!!!!!!!