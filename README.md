# supermarket-demo with chatbot
## 项目简介
 该项目完成了超市管理系统，包含用户主页查看超市各种信息以及商品，包含管理系统，进货，加库存等等。
 项目添加了客服机器人的简单demo，可以按需加入chatbot的回复逻辑

## 项目主要功能
*   **项目类型:**  基于 Django 框架开发的 **Web 应用程序**。
*   **目录结构:**  项目采用了典型的 Django 项目结构，包含 `app` (核心应用代码), `config` (项目配置), `static` (静态文件), `templates` (模板文件), `media` (媒体文件), `deploy` (部署配置) 等目录，结构清晰，模块化程度较高。
*   **主要功能模块:**  项目包括以下主要功能模块：
    *   **前台站点 (`front_site`):**  提供用户访问的前端页面，可能用于商品展示、信息浏览等 (`index`, `all`, `detail`, `about`, `feedback` 路由)。
    *   **后台管理 (`manage` 目录, `background` 目录):**  提供管理员使用的后台管理界面，用于管理系统数据和功能。
        *   **账号管理 (`accounts`):**  管理系统用户账号 (`account_all`, `account_add`, `profile` 等路由)。
        *   **供应商管理 (`providers`):**  管理商品供应商信息 (`provider`, `provider_add` 等路由)。
        *   **商品管理 (`goods`):**  管理商品信息，包括商品上下架、编辑等 (`goods`, `good_lower`, `good_edit` 等路由)。
        *   **进货管理 (`purchase`):**  管理商品进货业务 (`purchase`, `purchase_supplement` 路由)。
        *   **销售管理 (`sales`):**  销售台功能，可能用于记录销售信息 (`sale`, `sale_record` 路由)。
        *   **记录查询 (`records`):**  提供各种业务记录查询功能 (`records`, `storage` 路由)。
        *   **消息管理 (`message_handler`):**  处理用户反馈、消息通知等 (`messages`, `send_feedback`, `send_note` 路由)。
        *   **数据概览 (`index` in `background`):**  提供后台首页数据概览 (`view_all` 路由)。
        *   **登录与权限 (`login_handler`):**  用户登录、登出、权限控制 (`login`, `logout`, `profile` 路由)。

**项目用途**

*   **核心用途:**  这是一个用于 **超市或零售业务管理** 的信息系统。
*   **具体用途:**  该系统旨在帮助超市或零售商：
    *   **高效管理商品信息:**  包括商品分类、价格、库存、上下架等。
    *   **管理供应商信息:**  维护供应商信息，方便进货和采购。
    *   **处理进货业务:**  记录进货单据，跟踪进货状态。
    *   **进行销售管理:**  提供销售台功能，记录销售数据，统计销售额。
    *   **查询业务记录:**  方便查询各种业务数据，例如销售记录、库存记录、进货记录等。
    *   **进行用户和权限管理:**  管理系统操作人员账号，分配不同权限。
    *   **提供数据概览和报表:**  为管理者提供经营数据分析和决策支持。
    *   **可能包含前台商品展示:**  从 `front_site` 和 `templates/home` 包含一个面向顾客的前台网站，用于展示商品信息（具体功能需要进一步分析模板和视图代码）。
    *   **收集用户反馈:**  提供用户反馈入口，收集用户意见和建议。

**技术路径**
1.  **后端技术:**
    *   **编程语言:** Python
    *   **Web 框架:** Django
    *   **数据库:**  MySQL
    *   **WSGI 服务器:** Gunicorn (从 `config/gunicorn.py`)
    *   **项目配置:** `config` 目录下的 `settings.py`, `urls.py`, `wsgi.py` 等文件
    *   **应用逻辑:**  `app` 目录及其子目录下的 Python 代码 (`views.py`, `models.py`, `urls.py`, `libs` 等)

2.  **前端技术:**
    *   **HTML:**  构建页面结构 (`templates` 目录下的 `.html` 文件)
    *   **CSS:**  美化页面样式 (`static/home/css`, `static/manage/css` 目录下的 `.css` 文件)
    *   **JavaScript:**  实现前端交互逻辑 (`static/home/js`, `static/manage/js` 目录下的 `.js` 文件)
    *   **前端框架/库:**
        *   **Bootstrap:**  用于快速搭建响应式布局和通用 UI 组件 (`static/home/css/bootstrap.css`, `static/manage/demo/vendor/bootstrap`)
        *   **jQuery:**  JavaScript 库，简化 DOM 操作和 AJAX 请求 (`static/home/js/jquery-1.11.1.min.js`, `static/manage/demo/vendor/jquery`)
        *   **Font Awesome / Simple Line Icons:**  图标库 (`static/home/css/font-awesome.css`, `static/manage/demo/vendor/font-awesome`, `static/manage/demo/vendor/simple-line-icons`)
        *   **Owl Carousel, skdslider:**  可能用于实现轮播图或其他动态效果 (`static/home/css/owl.carousel.css`, `static/home/css/skdslider.css`, `static/home/js/owl.carousel.js`, `static/home/js/skdslider.min.js`)
        *   **Chart.js:**  后台数据可视化图表 (`static/manage/demo/vendor/chart.js`)

3.  **部署技术:**
    *   **Web 服务器:** Nginx (从 `deploy/nginx.conf` 推断)
    *   **进程管理:** Supervisor (从 `deploy/supervisor/django_demo.conf` 推断)
    *   **部署配置:** `deploy` 目录下的 `nginx.conf`, `supervisor` 配置等文件

**技术要点**
*   **MTV 设计模式:**  项目遵循 Django 的 MTV (Model-Template-View) 设计模式，代码组织结构清晰，易于维护和扩展。
*   **ORM (对象关系映射):**  Django 的 ORM 用于数据库操作，简化了数据访问代码的编写，提高了开发效率。
*   **URL 路由配置:**  使用 Django 的 URL 路由系统，将 URL 映射到对应的视图函数，实现灵活的 URL 设计。
*   **模板引擎:**  使用 Django 模板引擎，将动态数据渲染到 HTML 页面中，实现前后端分离。
*   **静态文件管理:**  Django 提供了静态文件管理机制，方便组织和管理 CSS, JavaScript, 图片等静态资源。
*   **用户认证和权限:**  项目包含了用户登录、登出、用户 profile 等功能，可能使用了 Django 的用户认证系统进行用户管理和权限控制。
*   **前后端分离:**  前端使用了 HTML, CSS, JavaScript 等技术，实现了前后端分离的开发模式。
*   **部署方案:**  项目提供了 Nginx + Gunicorn + Supervisor 的部署方案，是 Django 项目常用的生产环境部署架构。
*   **使用了多种前端库:**  Bootstrap, jQuery, Font Awesome 等前端库的运用，提高了前端开发效率和页面效果。


## 环境配置 (windows)
- windows 11
- python3.10

### 数据库 (mysqlclient)
1. windows安装mysql并启动
https://blog.csdn.net/weixin_45896437/article/details/132030152
root密码建议设置为123456简单一点

2. 安装miniconda或者anaconda
https://blog.csdn.net/ming12131342/article/details/140233867

2.1 创建conda环境, 打开Anaconda Prompt, 输入以下命令创建环境
```bash
> conda create -n my_env python=3.10
> conda activate my_env
> pip install django
> pip install mysqlclient
```

2.2 进入vscode安装插件python，此时在vscode的文件内选择一个python文件，可以看到右下角有个python版本号，点击选择python环境，选择刚刚创建的my_env环境


3. 使用/创建用户 admin, 使用创建数据库 demo_django_supermarket (root权限下)
    - 进入mysql命令行
    搜索并打开 MySQL 8.4 Command Line Client
    输入之前安装的时候的密码

    - 创建数据库 
    ```mysql
    mysql> CREATE DATABASE demo_django_supermarket DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    ```
    - 检查数据库默认编码
    ```mysql
    mysql> USE demo_django_supermarket;
    mysql> SELECT @@character_set_database, @@collation_database;
    +--------------------------+----------------------+
    | @@character_set_database | @@collation_database |
    +--------------------------+----------------------+
    | utf8mb4                  | utf8mb4_unicode_ci   |
    +--------------------------+----------------------+
    1 row in set (0.00 sec)

    mysql> SHOW TABLE STATUS FROM demo_django_supermarket;
   (略)
    ```
    - 创建数据库连接用户并授权
    ```mysql
    mysql> CREATE USER 'admin'@'localhost' IDENTIFIED BY '123456';
    mysql> GRANT ALL PRIVILEGES ON demo_django_supermarket.* TO 'admin'@'localhost';
    ```

### 初始化数据
1. migrate 迁移/初始化数据库
```bash
> D:/miniconda/envs/my_env/python.exe manage.py makemigrations
> D:/miniconda/envs/my_env/python.exe manage.py migrate
```
2. 设置一个超级管理员 admin (admin@123456)
> 参考
注意fixtures\root_manager.yaml内设置了管理员信息
```bash
> D:/miniconda/envs/my_env/python.exe manage.py loaddata fixtures/*
```

## 开始

1. 启动服务
```bash
> D:/miniconda/envs/my_env/python.exe manage.py runserver localhost:8001
```
> 若启动以 0.0.0.0:8001 还能在局域网内的其他设备访问，用浏览器打开该网站就能看到超市页面了



## 网页浮标客服机器人开发说明 (基于 Ollama 大模型)
1. chatbot apps 目录结构
 ```
 static/
 └── chatbot/  # chatbot 静态文件目录
     ├── css/  
     ├── js/
     └── images/ # 存放浮标图标等图片
 ```

 2. 继续开发的步骤：
  完成之前的网页部署后，此时可以开始修改chatbot\views.py，将用户的文字输入大模型，得到回答再返回即可
  tips：为了应对毕设，客服回答库存什么的完全可以固定回复来截图即可，如果需要现场演示可能得写一些代码将数据库的内容调过来加上用户的问题一起输入给大模型

