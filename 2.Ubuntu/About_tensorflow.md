```shell
# Conda create evn with specific lib
$ conda deactivate
$ conda create --name tf tensorflow-gpu
$ conda info --envs


# gpu memory check
$ nvidia-smi
$ kill something
# Tensorflow version check
$ python3 -c 'import tensorflow as tf; print(tf.__version__)' 

```



```shell
env 생성
$ conda create -n tf python=3.5
Python 3.5 버전의 ‘snowdeer_env’라는 이름으로 env를 생성합니다. (현재 Windows에서 Keras를 설치할 거면 Python 버전을 3.6이 아닌 3.5로 해야 합니다.)

env 리스트 보기
$ conda env list

env 활성화
$ activate tf

env 비활성화
$ deactivate
env 삭제
$ conda env remove -n snowdeer_env

env에 Tensorflow, Keras 설치
$ activate snowdeer_env
$ pip install tensorflow
$ pip install keras

Tensorflow와 Keras의 설치 확인은 다음 명령어를 이용해서 확인할 수 있습니다.
$ python
$ import tensorflow as tf
$ print(tf.__version__)
>> 1.4.0
$ import keras
>> Using TensorFlow backend.
```

