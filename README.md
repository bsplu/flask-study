# flask 学习日志

**[教程](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)**



---





## 安装

[virtualenv的介绍](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000). 该介绍只是科普, 主要还是按照最上面教程来

``` shell
$ source venv-p2p/bin/activate
$ deactivate
```

[设置环境变量](http://barkas.com/2016/set-environment-variables-activating-virtualenv/)





## 创建templete

``` shell
$ mkdir app/tempates
$ gedit index.html
```

index.thml

``` html
<html>
    <head>
        <title>{{ title }} - Microblog</title>
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
    </body>
</html>
```
