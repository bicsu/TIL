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



