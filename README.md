# NQB - NiX QQ Bot

该项目为 NiX 团队基于 Python 版 [qqbot](https://github.com/pandolia/qqbot) 开发的一系列插件。

## 部署

Linux 系统请按照以下步骤进行部署：

1. 安装 Python3
1. 安装 pip3
1. 克隆项目：`git clone https://github.com/NiX-Team/qqbot.git`
1. 进入项目根目录：`cd qqbot`
1. 安装虚拟环境及依赖包：`make install`

Windows 系统请按照以下步骤进行部署：

1. 安装 Python3
1. 安装 pip3
1. 克隆项目：`git clone https://github.com/NiX-Team/qqbot.git`
1. 进入项目根目录：`cd qqbot`
1. 安装虚拟环境：`pip3 install -U pipenv`
1. 新建虚拟环境：`pipenv --three`
1. 更新依赖包：`pipenv update`

## 运行

首先确保当前目录为项目根目录，Linux 下调用 `make run` 运行本机器人，Windows 请调用 `pipenv run qqbot -b .`。

## 插件模板生成

使用 `make plugin` 可以生成插件模板，该脚本生成之后的插件存入 plugins 目录。脚本中可以指定将新生成的插件加入配置文件。目前支持九种回调函数以及定时任务的模板生成。

## 数据清理

Linux 下调用 `make clean`，Windows 请手动清理。

## 插件开发

相关插件的开发规范请参考 [qqbot](https://github.com/pandolia/qqbot) 项目 README，将开发完成的插件放入 plugins 目录，并在配置文件 v2.x.conf 中注册相关插件。

也可以手动注册插件 `pipenv run qq plug {PluginName}`，手动注册的插件将在机器人重启之后失效。
