# conda

anacodna download link
https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh

## general_command 
```
conda create -n your_env_name python=X.X
conda env list
conda info
```
## change the source 
1. command
```
conda config --add channels
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
```
2. vim ~/.condarc
```
channels:
  - https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
  - https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - defaults
show_channel_urls: true
```

3. update conda 
```conda update conda ```


4. change to the default：
```conda config --remove-key channels```

remove conda env
```
conda env remove --name myenv
```

anacodna download link
https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh



## rename
```
conda create --name new_name --clone old_name
conda remove --name old_name --all
```

## export yal file
```
conda env export | grep -v "^prefix: " > environment.yml

conda env export > environment.yml

conda list -e > req.txt
```

## update env by yml file
conda env update --file local.yml




## install & uninstall
conda install xxx
conda uninstall xxx






# pip

## change source

### change forever
#### command
```
pip install pip -U #update the pip
pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/
```
#### vim ~/.config/pip/pip.conf
```
[global]

index-url = https://pypi.tuna.tsinghua.edu.cn/simple12
```
### temporal using
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

### pip source list
```
# 阿里云 
http://mirrors.aliyun.com/pypi/simple/
# 中国科技大学 
https://pypi.mirrors.ustc.edu.cn/simple/
# 豆瓣(douban) 
http://pypi.douban.com/simple/
# 清华大学 
https://pypi.tuna.tsinghua.edu.cn/simple/
# 中国科学技术大学 
http://pypi.mirrors.ustc.edu.cn/simple/
```



### offline install

pip install xx.whl
