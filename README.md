# UCAS Helper
## 前言
### 关于课程资源下载
国科大的课程网站在高校中已经算是很便利的了，老师可以发布ppt或其他课程资源到网站上，
学生可以登录课程网站下载需要的资源，但唯一让我感觉不爽的就是每个资源（如ppt），
只能一个个单独下载，没有批量下载的选项。另一方面，每次网站发布了新的资源，
我都要登录课程网站一个个点，真的心累。要是有个脚本可以直接将我本地的课程资源，
与课程网站一键同步就好了。所以就写了一个可用自动同步所有课程资源到本地的项目。

### 关于wifi登录
本来想着是破解往年的账号来使用，但是一方面这种未经过师兄师姐同意破解他人账号的事不太合理，
如果被有心之人利用不太好；另一方面，即便开了多进程，本机破解的效率实在过于低下，几个小时才破解一个账号。
因此只提供了自动登录的功能，且允许添加多个账号，当一个账号流量使用完后，可用下一个账号自动登录，
每月自动更新。


## 版本号

1.0.1

## 作者
- name: 董超鹏
- nickname: GentleCP
- e-mail: 574881148@qq.com
- website: https://www.gentlecp.com

## 实现功能
- 小白使用窗口  
    ![](img/2-1.png)
- 自动登录校园网  
    ![](img/3-1.png)
- 显示本学期课程列表  
    ![](img/1-1.png)
    
- 同步所有课程资源到本地  
    ![](img/1-2.png)
- 同步指定课程的资源到本地      
    ![](img/1-3.png)
- 同步指定课程的指定一个资源到本地  
  

## 部署

### 使用前提
项目采用python语言编写，需要你本地装有python3环境（建议python3.5+）

### 配置修改
- 获取课程资源
    - 进入settings.py，修改你自己的用户名和密码
    - 修改SOURCE_DIR，这个目录是所有课程资源存放的目录，根据你的个人需求修改  
        > 例如`D:/UCAS-sources`
    > 在校园网内无需登录wifi，直接可登录课程网站
- 登录wifi  
    - wifi登录需修改根目录下的wifi账号，添加到useful_accounts中，格式如下：
        ```text
          {
              "useful_accounts": [
                {
                   "stuid":"xxx",
                   "pwd":"xxx"
                },
                {
                    "stuid":"xxx",
                    "pwd":"xxx"
                }
               
              ],
              "useless_accounts": [],
              "current_month": 12
            }
        ```
        每个账号一个，允许存储多个账号，当遇到一个账号流量不够的时候自动切换到下一个账号登录

### 使用步骤
- 克隆本项目到本地  
    ```text
    git clone https://github.com/GentleCP/UCASHelper.git
    ```
- 安装依赖包  
    ```text
    pip install -r requirements.txt
    ```

- 运行main.py  
    ```text
    python manage.py
    ```
