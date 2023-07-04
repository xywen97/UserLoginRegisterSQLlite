# Flask 用户认证应用程序

这是一个基于 Flask 框架的用户认证应用程序，支持用户注册、登录、注销和查看个人信息等功能。该应用程序使用 SQLite 数据库来存储用户信息，密码经过哈希处理以确保安全性。应用程序还使用会话对象（session）来存储用户 ID，以便在用户登录后跟踪其状态。

## 安装依赖

在运行应用程序之前，请确保已安装所有必需的依赖项。可以使用以下命令安装依赖项：

```
pip install -r requirements.txt
```

## 运行应用程序

要运行应用程序，请在命令行中输入以下命令：

```
python app.py
```

该命令将启动 Flask 应用程序并将其运行在 localhost 上的默认端口（5000）上。在浏览器中访问 `http://localhost:5000` 即可打开应用程序主页。

## 功能列表

该应用程序支持以下功能：

- 用户注册
- 用户登录
- 用户注销
- 查看个人信息

## 文件结构

该应用程序的文件结构如下：

```
.
├── app.py
├── README.md
├── requirements.txt
├── static
│   └── style.css
└── templates
    ├── home.html
    ├── login.html
    └── register.html
```

- `app.py`：Flask 应用程序的主要代码。
- `README.md`：该文件。
- `requirements.txt`：应用程序的依赖项清单。
- `static`：存储静态文件的目录，例如 CSS 样式表。
- `templates`：存储 HTML 模板文件的目录。

## 开发者

- [Xiangyu](https://xywen97.github.io/)

## 许可证

该应用程序基于 MIT 许可证进行许可。有关更多信息，请参见 LICENSE 文件。