``` bash 
pip freeze > requirements.txt
```
把环境中的包全部输出，包括自带包。不容易开源传播。

## 使用pipreqs工具
装在base环境里。属于工具包，而不是项目依赖包。
``` bash 
pipreqs . --force
```

`.`：表示目录下所有文件。  
`--force`：覆盖原来的requirements.txt文件。

pipreqs读取目录中所有文件，检索使用那些包，然后输入requirements.txt文件里。有一定概率warning，但不重要。
