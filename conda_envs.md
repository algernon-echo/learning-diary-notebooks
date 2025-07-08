
|Command |Function ||
|:------|:------|------|   
|`conda env list` | 列出conda中所有环境 ||
|`conda list` | 列出环境中的包 ||
|`conda create -n/--name myenv`| 创造新环境||
|`conda activate myenv`| 激活环境||
|`conda deactivate`| 解除环境||
|``|||


### conda 和 pip 的关系

要确保pip在当前conda环境中工作。使用`which pip`检查。  
同理，使用`which python`检查python路径是否正确。  

```bash 
/opt/anaconda3/bin/python
#path of base environment

/opt/anaconda3/envs/myproject/bin/python
#path of the project environment
```

尽量使用`pip install <package_name>`从PyPL (Python Package Index)安装包。

