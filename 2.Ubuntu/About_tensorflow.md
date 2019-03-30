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
$ activate tfc

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

### CUDA9.0 설치

Install Nvidia CUDA-9.0 on Ubuntu 16.04 for Deep Learning
Friday, February 16, 2018
The latest version of CUDA is 9.1. However some deep learning frameworks are not yet ready for CUDA 9.1. The installation script of CUDA-9.1 is very similar to this one.

OS: Ubuntu 16.04 x86_64

(Optional) Uninstall old version CUDA Toolkit such as:

```shell
sudo apt-get purge cuda
sudo apt-get purge libcudnn6
sudo apt-get purge libcudnn6-dev
#Install CUDA Toolkit 9.0 and cuDNN 7.0 as follows:
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libcudnn7_7.0.5.15-1+cuda9.0_amd64.deb
wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libcudnn7-dev_7.0.5.15-1+cuda9.0_amd64.deb
wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libnccl2_2.1.4-1+cuda9.0_amd64.deb
wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/libnccl-dev_2.1.4-1+cuda9.0_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
sudo dpkg -i libcudnn7_7.0.5.15-1+cuda9.0_amd64.deb
sudo dpkg -i libcudnn7-dev_7.0.5.15-1+cuda9.0_amd64.deb
sudo dpkg -i libnccl2_2.1.4-1+cuda9.0_amd64.deb
sudo dpkg -i libnccl-dev_2.1.4-1+cuda9.0_amd64.deb
sudo apt-get update
sudo apt-get install cuda=9.0.176-1
sudo apt-get install libcudnn7-dev
sudo apt-get install libnccl-dev
#Reboot the system to load the NVIDIA drivers.

#Set up the development environment by modifying the PATH and LD_LIBRARY_PATH variables, also add them to the end of .bashrc file:

export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}


```



