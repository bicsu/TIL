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

#### 5. ubuntu  한글 설정

```shell
$ sudo apt-get install fcitx-hangul # 한글 세팅 → setting가서 ‘Hangul’로 수정(재부팅)

$ cd pycharm # 폴더 이동

$ ./pycharm.sh  # 설치

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
$ su - <유저명 예)pirl>
```

#### 8. pandas e 멱수 없애기 

```python
pd.set_option('display.float_format', lambda x: '%.3f' % x)	
```

