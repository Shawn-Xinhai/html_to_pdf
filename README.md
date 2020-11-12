# HTML转PDF的python工具

## 介绍

这个工具是模拟karbon后台的pdf生成过程，生成的pdf和最终后台生成的效果是一样的。

可以作为前端，测试pdf模版的工具。

---------

## 环境

- python3.9
- pip20.2.3

---------

## 安装

**解决平台依赖(macOS)**

因为pdf渲染库`weasyprint`需要`GTK+lib`, 所以需要安装一些平台依赖

下面的命令适用于 macOS，其他系统可参考
[weasyprint依赖安装](https://weasyprint.readthedocs.io/en/stable/index.html)

`brew install cairo pango gdk-pixbuf libffi libmagic`

**安装virtualenv**

`python3 -m pip install --user virtualenv`


**创建python运行环境**

在当前目录运行
`python3 -m venv env`


**安装依赖**

`pip install -r requirements.txt`

---------

## 用法

`python html_to_pdf.py <HTML_name> <output_pdf_name>`

例如

`python html_to_pdf.py index.html output.pdf`
