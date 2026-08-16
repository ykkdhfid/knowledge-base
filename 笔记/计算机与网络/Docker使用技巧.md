# Docker使用技巧

> 科目：计算机与网络 ｜ 收录日期：2026-08-16 ｜ 原文：《Docker使用技巧（小白版）.docx》

从零到上班够用 · 手把手中文教程
## 写在前面
你好！欢迎打开这本《Docker 使用技巧（小白版）》。如果你之前完全没接触过 Docker，看到命令行就心里发怵，那这本书就是专门为你写的。我会用最土的大白话、最贴近生活的比喻，把 Docker 讲明白，再带你一个一个命令地敲。
你需要准备什么？只需要一台能上网的电脑（Windows、Mac、Linux 都行），会开关机、会复制粘贴，就够了。不需要任何编程基础，不需要背任何东西——本书的每一章都会先讲道理、再给操作、最后给例子，你照着敲一遍就学会了。
这本书怎么用？建议按顺序读：第 1 章打比方建立感觉，第 2 章装好环境，第 3 到第 8 章是核心内容，第 9 到第 11 章是上班实战。每章的“命令”都放在灰色代码块里，你在终端（Windows 用 PowerShell 或 CMD，Mac 用“终端”）里一行一行输入即可。
几个阅读约定：以 $ 开头的行表示“提示符”，$ 本身不用输入；命令里的 <尖括号> 内容要换成你自己的内容，比如 <容器名> 就换成 mynginx；本书以 Linux / Mac 和 Windows 通用写法为主，个别 Windows 专属命令会单独标注。
**【提示】**放心大胆敲命令。就算敲错了，最坏的结果也就是报个错，不会弄坏你的电脑。多报错、多查错，是学 Docker 最快的路。
## 目录
- 第1章 Docker 是什么：集装箱比喻与三个核心名词
- 第2章 安装与环境：Docker Desktop、国内加速源、验证安装
- 第3章 镜像操作：搜索、下载、查看、删除、构建、推送
- 第4章 容器操作（核心章）：run 参数、生命周期、进入容器、日志
- 第5章 数据卷：为什么数据会丢、volume 与 bind mount、MySQL 实战
- 第6章 网络：三种模式、端口映射、容器名互访
- 第7章 Dockerfile 详解：全部指令、完整例子、多阶段构建
- 第8章 docker-compose：yaml 语法、三服务实战、常用命令
- 第9章 常用组合实战：MySQL、Redis、Nginx 反代、Portainer
- 第10章 排错与清理：常见问题、stats、df、prune
- 第11章 安全与生产技巧：非 root、只读、健康检查、资源限制
- 附录A 命令速查总表
- 附录B 常见坑清单
## 第1章 Docker 是什么
### 1.1 先打一个比方：集装箱
想象一下搬家。以前搬家，大家把锅碗瓢盆、衣服被子零散地搬，容易丢、容易碎、到了新家还得重新归置，特别累。后来海运行业发明了“集装箱”：不管里面装的是玩具还是汽车，统统塞进一个标准尺寸的铁箱子里，吊车一吊就上船，全世界的港口都能装卸。从此搬家、运输变得又快又标准。
Docker 就是软件世界的“集装箱”。程序员经常遇到一个烦恼：程序在我电脑上跑得好好的，怎么换台电脑就报错了？原因很简单——每台电脑的操作系统、软件版本、环境配置都不一样。Docker 的思路是：把“程序本身 + 它运行需要的所有环境”一起打包进一个标准箱子里，走到哪、搬到哪，打开就能跑，再也不用管底下是什么电脑。
围绕这个“集装箱”，Docker 有三个最核心的名词，请一定记住：
- 镜像（Image）＝ 菜谱 + 半成品食材。做一道菜需要说明步骤、准备食材，这些都打包好了，但菜还没做出来，不能直接吃。镜像就是这样一个“只读模板”，它包含程序代码和运行环境，但它本身不能运行。
- 容器（Container）＝ 按菜谱做出来的那盘菜。真正在运行、真正能用的，是容器。同一个镜像可以做出很多盘一模一样的菜，也就是一个镜像可以启动很多个容器。
- 镜像仓库（Registry）＝ 菜市场。菜市场里摆着各种各样的菜谱，想用哪个就去拿（下载）。Docker Hub 就是最大的“菜市场”，docker pull 就是从里面把镜像下载到本地。
用一个简单的图来记：镜像 ——docker run——> 容器。镜像只能看不能跑，容器才是跑起来的程序；删掉容器不影响镜像，还可以再用镜像再做一个新容器。

| 概念 | 生活中的比方 | 在 Docker 里是什么 | 常用命令 |
| --- | --- | --- | --- |
| 镜像 Image | 菜谱 + 半成品食材 | 只读的程序模板 | docker pull / docker build |
| 容器 Container | 做好的菜 | 正在运行的程序实例 | docker run / docker ps |
| 镜像仓库 Registry | 菜市场 | 存放镜像的远程服务器 | docker pull / docker push |
| 标签 Tag | 菜谱的版本号 | 镜像的版本标识，如 nginx:1.27 | docker tag |

### 1.2 虚拟机 vs 容器（大白话）
在 Docker 出现之前，大家解决“环境不一致”的办法是虚拟机（VM）。虚拟机是什么呢？打个比方：你家里有一栋楼，想再住一户人，干脆在楼旁边再盖一栋一模一样的楼——地基、水电、墙、家具全都要新的。虚拟机就是在你的电脑里“再装一台完整的电脑”，它有自己的一套操作系统，占硬盘、占内存，启动要几分钟。
容器就不一样了：它不重新装操作系统，而是直接“借用”你电脑的操作系统内核（可以理解成大楼的水电管道），只是把自己需要的那部分程序和环境搬进去，像一个房间一样。所以容器启动只要几秒钟，占用的资源也小得多。

| 比较项 | 虚拟机 | 容器 |
| --- | --- | --- |
| 启动速度 | 几分钟 | 几秒钟 |
| 占用资源 | 大（每台都要整套操作系统） | 小（共用内核，只带自己的程序） |
| 体积 | 几个 GB 起步 | 几十 MB 到几百 MB |
| 隔离程度 | 非常彻底（完全独立的系统） | 较彻底（共用内核，进程隔离） |
| 典型用途 | 需要完整独立系统时 | 跑应用、微服务、开发环境 |

**【技巧】**一句话记忆——虚拟机是“搬家搬一整栋楼”，容器是“只搬自己的房间，水电（内核）共用大楼的”。
### 1.3 为什么开发、上班都要用 Docker
- 环境一致：再也不会有“我电脑上能跑，你电脑上报错”。把镜像打包好，谁拉下来跑都是一模一样的环境。
- 一键部署：上班时把代码做成镜像，服务器上一条 docker run 就能把服务跑起来，不用在服务器上一步步装环境。
- 依赖隔离：不同项目要的软件版本可能互相打架（这个要 Python 3.9，那个要 Python 3.12），用 Docker 各装各的，互不干扰。
- 秒级启动、轻松扩容：流量大了，多启动几个容器就行。
- 团队协作标准化：Dockerfile（后面第 7 章会讲）就是一份“环境说明书”，新同事来了照着说明书就能复现环境。
### 1.4 常见术语速记

| 术语 | 大白话解释 |
| --- | --- |
| 镜像 Image | 只读的程序模板，相当于菜谱加半成品食材 |
| 容器 Container | 镜像运行起来的实例，相当于做好的菜 |
| 仓库 Registry | 存放镜像的服务器，相当于菜市场 |
| 标签 Tag | 镜像的版本号，比如 nginx:1.27 里的 1.27 |
| Dockerfile | 写镜像“怎么做”的文本文件（制作说明书） |
| docker-compose | 一次性管理多个容器的工具（晚宴菜单） |
| 宿主机 | 你正在用的这台电脑 |
| 守护进程 daemon | Docker 在后台干活的管家，负责真正创建容器 |

## 第2章 安装与环境
### 2.1 Windows：Docker Desktop + WSL2
Windows 上最省事的方式是安装 Docker Desktop。它会自带一个图形界面，日常操作和看状态都很方便。Docker Desktop 在 Windows 上推荐配合 WSL2 使用，WSL2 可以理解成 Windows 里内置的一个“轻量 Linux”，Docker 在里面跑得又快又稳。
- 第一步：开启 WSL2。用管理员身份打开 PowerShell，输入下面的命令，按提示重启电脑（Windows 10 较新版本或 Windows 11 都支持）。
wsl --install
- 第二步：安装 Docker Desktop。去 Docker 官网 docker.com 下载 Docker Desktop for Windows，一路“下一步”安装完成。
- 第三步：启动 Docker Desktop，在设置（Settings）→ General 里勾选 Use the WSL 2 based engine。
- 第四步：等右下角的小鲸鱼图标变成绿色，就说明 Docker 引擎启动成功了。
**【提示】**如果你的电脑比较老，装 WSL2 之前要先在 BIOS 里打开“虚拟化”（VT-x / AMD-V）。打开方式因电脑品牌而异，一般是开机时按 F2 或 Del 进 BIOS，找到 Virtualization 设为 Enabled。
### 2.2 Mac 和 Linux 安装
Mac 用户：同样去 docker.com 下载 Docker Desktop for Mac。如果你的 Mac 是 Apple 芯片（M1/M2/M3/M4），下载时选 Apple Silicon 版本；Intel 芯片选 Intel 版本。
Linux 用户：最省事的是用官方提供的一键安装脚本（需要 root 权限，Ubuntu / Debian / CentOS 都适用）：
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
装完 Linux 版后，一般还要把当前用户加入 docker 用户组，这样不用每次敲 sudo：
sudo usermod -aG docker $USER
newgrp docker
**【提示】**$USER 是系统自动填好的变量，不用改。加入用户组后要重新登录一次终端才生效。
### 2.3 配置国内镜像加速源
默认情况下，Docker 从国外的 Docker Hub 下载镜像，在国内经常很慢甚至超时。解决办法是配置“镜像加速源”，相当于在菜市场旁边开一个国内分店，下载就快了。
Windows 用户：打开 Docker Desktop → Settings → Docker Engine，把下面的内容粘贴进去，然后点 Apply & Restart。
{
  "registry-mirrors": [
    "https://docker.mirrors.ustc.edu.cn",
    "https://hub-mirror.c.163.com"
  ]
}
Linux 用户：编辑 /etc/docker/daemon.json（没有就新建），内容同上，然后重启 Docker：
sudo systemctl restart docker
**【重点】**阿里云、腾讯云都提供免费的镜像加速地址，其中阿里云的地址是每个人专属的，需要登录阿里云容器镜像服务控制台查看，格式类似 https://xxxx.mirror.aliyuncs.com，把它替换进上面的列表即可。改完一定要重启 Docker 才生效。
### 2.4 验证安装：docker version 和 docker info
安装完成后，先验证一下 Docker 是否正常。在终端里输入：
docker version
输出会分成 Client 和 Server 两段。Client 是命令行工具，Server 是后台引擎。重点看 Server 段有没有内容——只有 Server 也正常输出了，才说明 Docker 真的能用。
再看一下系统信息：
docker info
里面能看到 Containers（当前有几个容器）、Images（有几个镜像）、Operating System 等信息。以后排错也经常用到它。
### 2.5 跑一个 Hello World 试试
第一个实验，让 Docker 跑一个最最简单的“你好世界”容器：
docker run hello-world
第一次运行会先从网上把这个镜像下载下来，然后运行它，最后屏幕上会出现一段欢迎文字。看到 “Hello from Docker!” 就说明你的 Docker 已经彻底装好、能正常工作了。
**【技巧】**如果这一步卡住或超时，多半是网络问题，先按 2.3 节配置好国内加速源再试。
## 第3章 镜像操作
### 3.1 镜像是什么（再复习一遍）
镜像就是“只读的程序模板”，像一张游戏光盘：内容固定不变，插进不同的游戏机（启动成容器）就能玩。你可以在同一张光盘的基础上，运行出很多个游戏实例。
### 3.2 搜索镜像：docker search
想看看菜市场里有没有某个镜像，用 docker search：
docker search nginx
结果里的 NAME 是镜像名，STARS 是点赞数（越高越多人用），OFFICIAL 带 [OK] 表示官方出品。一般来说，优先选官方镜像，出问题的概率小。
### 3.3 下载镜像：docker pull
下载镜像用 docker pull，后面跟镜像名。不写标签时默认下载 latest（最新版）：
docker pull nginx
想指定版本，就在镜像名后面加冒号和标签。比如下载 nginx 的 1.27 版、redis 的 alpine 精简版：
docker pull nginx:1.27
docker pull redis:7-alpine
下载时会看到一层一层地下载（pull 的过程就是按层拉取），已经有的层会显示 Already exists，不用重复下载。
### 3.4 查看本地镜像：docker images
看本地已经有哪些镜像：
docker images
表格里 REPOSITORY 是镜像名，TAG 是版本标签，IMAGE ID 是镜像的唯一编号，SIZE 是大小。镜像很多时可以用 docker images | findstr nginx（Windows）或 docker images | grep nginx（Mac/Linux）来过滤。
### 3.5 给镜像打标签：docker tag
docker tag 可以给镜像起一个“别名+版本号”，方便自己管理。它只是加一个引用，不会复制一份镜像：
docker tag nginx:latest mynginx:v1
之后再 docker images，就会看到多了一行 mynginx:v1，但它和 nginx:latest 指向同一个镜像。
### 3.6 删除镜像：docker rmi
删除镜像用 docker rmi（remove image 的缩写），后面跟镜像名或 IMAGE ID：
docker rmi mynginx:v1
如果镜像正在被某个容器使用，会删不掉并提示 image is being used by container，这时要先删除使用它的容器（第 4 章会讲），或者用 -f 强制删除：
docker rmi -f nginx:latest
**【警告】**rmi 删的是镜像，不是容器；rm 才是删容器（第 4 章）。新手最容易搞混这两个命令。强制删除 -f 只在确认镜像没用的时候用。
### 3.7 构建镜像：docker build
用自己的代码做镜像，要写一份 Dockerfile（第 7 章详解），然后在 Dockerfile 所在目录执行：
docker build -t myapp:v1 .
-t 是给新镜像起名，末尾的 . 表示“使用当前目录下的 Dockerfile”。这条命令现在先了解，第 7 章会完整实战。
### 3.8 推送镜像：docker push
把自己做的镜像传到仓库（菜市场）里，先登录，再推送：
docker login
docker push 你的用户名/myapp:v1
登录时会提示输入用户名和密码。注意：推送到 Docker Hub 时，镜像名前面要带你的用户名。
### 3.9 镜像分层：为什么镜像越小越好
镜像不是一整块，而是由很多“层（Layer）”像千层饼一样叠起来的：基础系统一层、装软件一层、复制代码一层……每一层都是只读的，构建时如果某层没变，就能直接复用缓存，不用重新做。
因为镜像要下载、要存盘、要启动，所以镜像越小越好：
- 下载快：团队拉镜像不用等。
- 启动快：容器启动要把镜像内容准备好。
- 占磁盘小：机器上镜像多了也扛得住。
- 更安全：东西越少，能被攻击的面越小。
常见的瘦身技巧：
- 优先选 alpine 等精简版镜像，比如 redis:7-alpine、python:3.12-alpine。
- 一个 RUN 里把多条命令用 && 连起来，减少层数。
- 装完软件顺手清理缓存，比如 apt-get clean。
- 用多阶段构建（第 7 章有例子），最终镜像只留成品。
**【技巧】**判断镜像好坏，第一眼就看 SIZE 列和基础镜像是不是精简版。
## 第4章 容器操作（核心章）
### 4.1 一句话理解容器
容器就是“镜像跑起来之后的样子”。镜像是一张菜谱，容器是照菜谱做出来的菜；菜可以有很多盘，互不影响。每个容器都有自己的文件系统、进程和网络，但比虚拟机轻得多。
这一章是全书最核心的一章，请耐心跟着敲。我们会用 nginx（一个网页服务器）来做例子，因为它最容易看到效果。
### 4.2 docker run：创建并启动容器
docker run 是最常用的命令，它负责“用镜像创建一个新容器并启动”。最简单的写法：
docker run hello-world
但真实项目里，docker run 后面会跟一大堆参数。下面这张表把这些参数一次讲清楚，请收藏：

| 参数 | 大白话含义 | 例子 | 说明 |
| --- | --- | --- | --- |
| -d | 后台运行（关掉终端容器也不停） | docker run -d nginx | 不加 -d 会占住终端，Ctrl+C 会停掉容器 |
| -p 电脑端口:容器端口 | 端口映射：把电脑的端口转发到容器里 | -p 8080:80 | 左边是电脑的，右边是容器里的，别写反 |
| -v 电脑路径:容器路径 | 数据卷挂载：把数据存在容器外面 | -v mydata:/data | 容器删了数据还在（第 5 章） |
| -e 变量名=值 | 环境变量：给容器里的程序传配置 | -e MYSQL_ROOT_PASSWORD=123456 | 一个 -e 传一个变量，可以写多个 |
| --name 名字 | 给容器起个名字 | --name mynginx | 不写会随机生成一个难记的名字 |
| --rm | 容器停止后自动删除 | --rm | 适合临时测试，用完即扔 |
| -it | 交互式终端（进入容器操作） | -it ubuntu bash | i 表示交互，t 表示分配终端，一般成对出现 |
| --network 网络名 | 指定容器加入哪个网络 | --network mynet | 第 6 章详解 |
| --restart 策略 | 容器退出后自动重启 | --restart always | always 表示开机自启+崩溃重启，服务器常用 |
| --cpus 数字 | 限制容器最多用几个 CPU 核 | --cpus 0.5 | 0.5 表示最多用半个 CPU 核 |
| --memory 大小 | 限制容器最多用多少内存 | --memory 512m | 防止某个容器把内存吃光 |

下面把最常见的几种组合各敲一遍。
例子 1：后台运行一个 nginx，并把电脑的 8080 端口映射到容器内的 80 端口，容器名叫 mynginx：
docker run -d --name mynginx -p 8080:80 nginx
跑起来后打开浏览器，访问 http://localhost:8080，能看到 nginx 的欢迎页面就成功了。
例子 2：传环境变量。启动 MySQL 时把 root 密码通过 -e 传进去：
docker run -d --name mysql8 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql:8
例子 3：交互式进入一个 Ubuntu 容器，在里面敲命令：
docker run -it --name ubuntu1 ubuntu bash
进入后你会看到提示符变成了 root@xxx:/#，说明你现在已经在容器里面了，可以随便敲 ls、cat 等命令。输入 exit 退出容器。
例子 4：限制资源。启动一个最多用半个 CPU、256MB 内存的 nginx：
docker run -d --name tiny-nginx --cpus 0.5 --memory 256m nginx
**【重点】**-p 左边写电脑的端口，右边写容器里程序的端口。不写 -p 时，容器里的程序外面是访问不到的。左边端口一旦被别的程序占用，启动会直接报错（第 10 章讲怎么解决）。
### 4.3 查看容器：docker ps / docker ps -a
查看正在运行的容器：
docker ps
查看所有容器（包括已经停止的）：
docker ps -a
只看容器 ID（后面批量操作经常用）：
docker ps -aq
结果里重点看 NAMES（容器名）、STATUS（Up 表示运行中，Exited 表示已停止）、PORTS（端口映射，比如 0.0.0.0:8080->80/tcp 表示电脑 8080 转发到容器 80）。
### 4.4 启动、停止、重启容器
停止一个运行中的容器（优雅停止，相当于正常关机）：
docker stop mynginx
启动一个已停止的容器（注意是 start，不是 run，run 会新建）：
docker start mynginx
重启容器（先停再起）：
docker restart mynginx
如果容器卡死，优雅停止没反应，可以强制杀掉（相当于拔电源）：
docker kill mynginx
**【技巧】**stop 和 kill 的区别：stop 会先给容器里的程序发“请退出”的信号，程序来得及保存数据；kill 是直接干掉。能用 stop 就别用 kill。
### 4.5 删除容器：docker rm / rm -f
删除一个已经停止的容器：
docker rm mynginx
强制删除一个正在运行的容器：
docker rm -f mynginx
一次删掉所有容器（慎用）：
docker rm -f $(docker ps -aq)
**【警告】**删容器等于把“这盘菜”倒掉。容器里的数据是临时的，一删就没（第 5 章教你把数据存到容器外面）。rm -f 很暴力，运行中的容器也会被直接干掉，使用前一定确认容器名没写错。
### 4.6 进入容器：exec 与 attach 两种姿势
想进到容器里面看看、敲命令，有“两种姿势”。新手请只用第一种：
姿势一：docker exec（推荐）。它相当于“另开一扇门”进容器，在里面退出不影响容器运行：
docker exec -it mynginx bash
进入后可以随便逛，比如看看 nginx 的配置文件在哪：
ls /etc/nginx
exit
姿势二：docker attach。它直接“接上”容器的主进程，退出时可能会把容器也带停，新手容易误操作，不推荐：
docker attach mynginx

| 对比项 | docker exec -it | docker attach |
| --- | --- | --- |
| 本质 | 在容器里新开一个进程 | 连接到容器主进程 |
| 退出后容器 | 照常运行 | 可能随之停止 |
| 适用场景 | 日常排查、改配置 | 看主进程的输出 |

**【提示】**进入容器报 “exec: no such file or directory” 时，说明这个精简镜像里没有 bash，把 bash 换成 sh 再试：docker exec -it mynginx sh。alpine 之类的精简镜像只有 sh。
### 4.7 查看日志：docker logs
容器里的程序把日志打到哪去了？用 docker logs 看：
docker logs mynginx
实时跟踪日志（像看电影一样一直刷新，Ctrl+C 退出）：
docker logs -f mynginx
只看最后 20 行：
docker logs --tail 20 mynginx
排错时这句是救命稻草：容器一启动就退出？先 docker logs 看它说了什么（第 10 章还会细讲）。
### 4.8 复制文件：docker cp
把容器里的文件复制到电脑上：
docker cp mynginx:/etc/nginx/nginx.conf ./nginx.conf
把电脑上的文件复制进容器：
docker cp ./index.html mynginx:/usr/share/nginx/html/index.html
语法就是“docker cp 来源 目标”，来源和目标里带容器名的就是容器里的路径。
### 4.9 查看容器内进程与资源占用
看容器里正在跑哪些进程：
docker top mynginx
实时看所有容器的 CPU / 内存占用（像任务管理器，Ctrl+C 退出）：
docker stats
只看一次就退出：
docker stats --no-stream
**【技巧】**发现某个容器 CPU 一直 100%，八成是程序写了个死循环，用 docker stats 一眼就能抓到它。
## 第5章 数据卷
### 5.1 为什么容器删了数据就没了
还记得吗？容器是“做好的菜”，而它运行中产生的文件（数据库数据、日志、上传的图片等）都写在容器的“可写层”里。这层是临时的：容器一删除，这层就跟着被倒掉了，数据就没了。
打个比方：食堂的菜做好后放在临时餐盘里，客人吃完餐盘收走，菜自然就没了。如果你想让菜“留下来”，就得把菜装进自己的保温盒——这个“保温盒”就是数据卷。
所以结论很重要：凡是重要的数据，一定不要放在容器里，要挂载（存）到容器外面。
### 5.2 两种挂载方式：volume 和 bind mount
Docker 提供两种“把数据放到容器外”的方式：
volume（数据卷）：Docker 自己帮你管理的一块存储空间，位置由 Docker 决定。你只管给它起个名字，比如 mydata。它安全、好备份，最适合放数据库数据。
bind mount（绑定挂载）：直接把“你电脑上的某个文件夹”借给容器用。你改文件夹里的文件，容器里立刻就能看到，最适合开发时改代码即时生效。

| 比较项 | volume 数据卷 | bind mount 绑定挂载 |
| --- | --- | --- |
| 谁来管理位置 | Docker 自己管理 | 你自己指定电脑上的路径 |
| 大白话 | Docker 帮你租的仓库 | 把你家客厅直接借给它 |
| 适合场景 | 数据库、重要数据、生产环境 | 开发时改代码即时生效 |
| 备份迁移 | 方便（名字即身份） | 路径换了就找不到了 |
| 删除容器后 | 数据还在 | 数据还在（就在你电脑上） |

### 5.3 -v 的三种写法
挂载都通过 docker run 的 -v 参数完成，一共三种写法，请对照着记：
写法一：具名卷（推荐）。格式 -v 卷名:容器内路径：
docker run -d --name myweb -v mydata:/data nginx
写法二：匿名卷。只写容器内路径，Docker 随机生成一个卷名，不好管理，不推荐：
docker run -d --name myweb2 -v /data nginx
写法三：绑定挂载。格式 -v 电脑上的绝对路径:容器内路径。Windows 上要注意路径写法：
docker run -d --name myweb3 -v D:\myapp:/data nginx
开发 Python / Node 项目时，经常把当前目录直接挂进去（$(pwd) 表示当前目录）：
docker run -d --name dev -v $(pwd):/app -w /app node:20
**【重点】**推荐一律使用“具名卷”（写法一）。匿名卷难找难删，绑定挂载要注意路径别写错。Windows 下用 Git Bash 时，路径写成 /d/myapp 这种格式。
### 5.4 数据卷的管理命令
查看有哪些数据卷：
docker volume ls
查看某个卷的详细信息（能看到它在电脑上的真实位置 Mountpoint）：
docker volume inspect mydata
删除一个数据卷：
docker volume rm mydata
清理所有没被使用的数据卷：
docker volume prune
**【警告】**删除数据卷 = 把里面的数据真的删掉，没有回收站！prune 会一次删掉所有“没人在用”的卷，执行前先 docker volume ls 看清楚。
### 5.5 实战：MySQL 数据挂载完整例子
我们把前面学的串起来，做一个小实验：启动一个 MySQL，往里面建库建表插数据，然后删掉容器再重新启动，看看数据还在不在。
第一步：创建一个具名数据卷：
docker volume create mysql-data
第二步：启动 MySQL，把数据目录 /var/lib/mysql 挂载到这个卷上：
docker run -d --name mysql8 -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -v mysql-data:/var/lib/mysql \
  mysql:8
第三步：进入容器，连上 MySQL，建一个库、一张表，插一条数据：
docker exec -it mysql8 mysql -uroot -p123456
mysql> CREATE DATABASE mydb;
mysql> USE mydb;
mysql> CREATE TABLE users (id INT, name VARCHAR(50));
mysql> INSERT INTO users VALUES (1, '小明');
mysql> exit;
第四步：狠心删掉这个容器：
docker rm -f mysql8
第五步：用同一个数据卷再启动一个一模一样的 MySQL：
docker run -d --name mysql8 -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -v mysql-data:/var/lib/mysql \
  mysql:8
第六步：再次进入，查一下数据还在不在：
docker exec -it mysql8 mysql -uroot -p123456 -e "SELECT * FROM mydb.users;"
看到那条“小明”还在，就说明数据卷挂载完全成功了——容器可以随便删，数据稳如泰山。
**【重点】**mysql 官方镜像默认把数据放在容器内的 /var/lib/mysql，所以挂载时这个路径必须写对；挂错路径等于没挂，数据照样丢。
## 第6章 网络
### 6.1 三种网络模式：bridge、host、none
每个容器都有自己的网络。Docker 默认提供三种模式，大白话解释一下：
bridge（桥接，默认）：像小区。每户（容器）都有自己的门牌号（IP），通过小区里的马路（虚拟网桥）互相串门，也能连到外面。这也是默认模式，日常 99% 都在用它。
host（主机）：像把房间门拆了，直接住客厅。容器直接使用电脑的网络，没有自己的 IP，端口也不隔离。好处是快，坏处是不安全、容易端口打架。
none（无网络）：像被关进小黑屋，没有网卡。适合纯计算、离线任务。

| 模式 | 大白话 | 有自己的 IP 吗 | 什么时候用 |
| --- | --- | --- | --- |
| bridge | 小区，每家每户走马路串门 | 有 | 默认模式，日常开发、部署都用它 |
| host | 拆了门住客厅，直接用电脑的网络 | 没有 | 追求极致的网络性能时 |
| none | 小黑屋，没有网络 | 没有 | 纯计算、离线任务 |

查看当前有哪些网络：
docker network ls
### 6.2 端口映射 -p 8080:80 到底是什么意思
容器在“小区”里，外面（你的浏览器）默认是看不到它的。端口映射就是给容器开一扇门：电脑上的某个端口收到请求，就转发给容器里的某个端口。
语法是 -p 电脑端口:容器端口。比如：
docker run -d --name mynginx -p 8080:80 nginx
这句话的意思是：电脑的 8080 端口 → 转发给容器里的 80 端口。之后浏览器访问 http://localhost:8080，就能看到 nginx 页面。
为什么容器里是 80？因为 nginx 镜像里 nginx 默认监听 80 端口。为什么电脑上是 8080？因为我们怕 80 被别的程序占用，所以随便挑了一个没被占用的端口。
**【技巧】**-p 8080:80 和 -p 80:8080 完全是两回事！左边永远是“电脑的端口”，右边永远是“容器内的端口”，写反了就会连不上。想不通的时候，默念三遍：左外右内。
### 6.3 自定义网络：让容器用名字互相访问
实际项目里常常需要两个容器互相通信，比如网页要连数据库。这时候有个大坑：容器的 IP 是随机的，重启一次就变。怎么办？
答案是：把容器都放进同一个“自定义网络”，然后直接用容器名互相访问，Docker 会自动把名字翻译成 IP。
第一步：创建一个自定义网络（相当于建一个新的小区）：
docker network create mynet
第二步：把两个容器都放进这个网络：
docker run -d --name web1 --network mynet nginx
docker run -d --name web2 --network mynet nginx
第三步：在 web1 里访问 web2，直接用名字：
docker exec web1 wget -qO- http://web2
能看到 nginx 的 HTML 输出，就说明两个容器已经可以通过名字互相访问了。
**【重点】**容器之间互相访问，永远用容器名（或服务名），不要用 localhost，也不要自己记 IP。localhost 在容器里指的是“容器自己”，不是别的容器！这个坑无数新手踩过。
## 第7章 Dockerfile 详解
### 7.1 Dockerfile 是什么
Dockerfile 是一个文本文件，相当于“镜像的制作说明书”。你把制作步骤一行行写进去，docker build 就会照着说明，一步步做出一个镜像来。
先看一个最简单的例子。建一个文件夹，里面放一个 index.html 和一个 Dockerfile：
Dockerfile 内容：
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
然后在文件夹里执行构建：
docker build -t mynginx:v1 .
构建完成后，这个镜像就包含了一个 nginx 加上你自己的首页。运行它：
docker run -d --name mypage -p 8080:80 mynginx:v1
浏览器打开 http://localhost:8080，看到的就是你的 index.html。从“写说明”到“出镜像”，就这么简单。
### 7.2 指令逐个讲
#### FROM：第一行必须是它
指定“基础镜像”，也就是在这张菜谱的基础上加工。就像做菜要先说“以什么食材为主料”。
FROM python:3.12-slim
FROM nginx:alpine
#### RUN：构建时执行命令
构建镜像的过程中要执行的命令，比如安装软件、下载依赖。每一条 RUN 都会生成新的一层。
RUN apt-get update && apt-get install -y curl
注意：多条命令尽量用 && 连成一条 RUN，少分几层，镜像更小。
#### COPY：把文件拷进镜像
把“电脑上（构建上下文里）的文件”复制到镜像里。格式 COPY 电脑路径 镜像路径。
COPY app.py /app/app.py
COPY requirements.txt /app/
#### ADD：COPY 的加强版
ADD 和 COPY 功能差不多，但多两个能力：能自动解压 tar 压缩包、能直接下载 URL 文件。正因为它“太能干”，行为不好预测，一般推荐用 COPY，除非真的需要解压。
ADD app.tar.gz /app/
#### WORKDIR：设置工作目录
设置之后所有命令的“默认目录”，相当于 cd。容器启动后也默认在这个目录。
WORKDIR /app
#### ENV：设置环境变量
和 docker run 的 -e 作用一样，在 Dockerfile 里提前写好，容器运行时就能读到。
ENV APP_PORT=8080
#### EXPOSE：声明端口
告诉别人“我这个容器里哪个端口提供服务”。注意它只是声明，真正让外面能访问，还是要在 docker run 时用 -p 映射。
EXPOSE 8080
#### VOLUME：声明数据卷挂载点
声明容器内哪个目录是“放数据的地方”，建议用 -v 挂载。只写声明，真正的卷还是由 docker run -v 或 compose 创建。
VOLUME /data
#### CMD：容器启动时执行的命令
容器一启动就跑它。注意：docker run 后面如果跟了命令，会把 CMD 覆盖掉。写法推荐用“数组形式”。
CMD ["python", "app.py"]
#### ENTRYPOINT：容器启动的入口命令
和 CMD 类似，但更“顽固”：docker run 后面跟的命令不会覆盖它，而是作为参数追加给它。适合固定程序入口的场景。
ENTRYPOINT ["python", "app.py"]
#### USER：切换运行用户
指定容器以哪个用户身份运行，生产环境强烈建议用非 root 用户（第 11 章细讲）。
USER nobody
CMD 和 ENTRYPOINT 的区别，用一张表记牢：

| 对比项 | CMD | ENTRYPOINT |
| --- | --- | --- |
| docker run 后面跟命令时 | 会被覆盖 | 不会被覆盖，追加为参数 |
| 典型场景 | 默认启动命令，允许用户改 | 固定入口，不允许改 |
| 例子 | CMD ["python", "app.py"] | ENTRYPOINT ["python", "app.py"] |

COPY 和 ADD 的区别：

| 对比项 | COPY | ADD |
| --- | --- | --- |
| 复制文件 | 可以 | 可以 |
| 自动解压 tar | 不可以 | 可以 |
| 直接下载 URL | 不可以 | 可以 |
| 推荐度 | 推荐（行为简单可控） | 少用（行为多，难预测） |

### 7.3 完整例子：构建一个 Python 应用镜像
假设你的项目长这样：
myapp/
├── app.py
├── requirements.txt
└── Dockerfile
app.py 内容（一个最简单的 Flask 服务）：
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello Docker!'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
requirements.txt 内容：
flask
Dockerfile 内容：
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
逐行解释：
- FROM python:3.12-slim：基于精简版 Python 3.12。
- WORKDIR /app：后面的命令都在 /app 目录下执行。
- COPY requirements.txt .：先把依赖清单拷进去。
- RUN pip install ...：安装依赖（用了清华源，国内下载快）。
- COPY . .：再把项目源码全部拷进去。
- EXPOSE 8000：声明 8000 端口。
- CMD ["python", "app.py"]：启动时运行程序。
构建并运行：
docker build -t mypyapp:v1 .
docker run -d --name mypyapp -p 8000:8000 mypyapp:v1
浏览器打开 http://localhost:8000，看到 “Hello Docker!” 就成功了。
**【重点】**先 COPY 依赖文件、装完依赖、再 COPY 源码，这个顺序非常重要，是为了吃满“构建缓存”（7.5 节讲）。顺序反了，以后每次改代码都要重装依赖。
### 7.4 多阶段构建：镜像瘦身神器
有些语言（比如 Go、Java、前端打包）需要先“编译/打包”，编译过程要装一大堆工具，但这些工具最终运行时根本用不到。多阶段构建的思路是：先用一个“大厨房”把所有准备工作做完，最后只把“成品菜”端到一个小房间里。
看一个 Go 项目的例子：
# 第一阶段：编译（大厨房）
FROM golang:1.22 AS builder
WORKDIR /src
COPY . .
RUN go build -o app main.go
# 第二阶段：运行（小房间，只留成品）
FROM alpine:3.20
COPY --from=builder /src/app /app
CMD ["/app"]
最终镜像只有 alpine + 一个编译好的程序，可能就几 MB，而 golang 镜像本身要几百 MB。这就是多阶段构建的威力。
### 7.5 .dockerignore 与构建缓存
.dockerignore 文件的作用，和 .gitignore 类似：告诉 Docker“构建时不要把这些文件拷进去”，比如本地的虚拟环境、缓存、密钥。
一个典型的 .dockerignore：
.git
__pycache__
*.pyc
node_modules
venv
.venv
.env
为什么要写它？一是镜像更小，二是防止把带密码的 .env 文件不小心打进镜像。
再说构建缓存。Docker 构建是一层一层来的，只要某一步的输入没变，它就复用上次的结果（缓存），秒出。这带来一个黄金法则：把“不容易变的东西”放前面，“容易变的东西”放后面。
坏例子（每次改代码都要重装依赖，慢）：
FROM python:3.12-slim
COPY . /app
RUN pip install -r /app/requirements.txt
好例子（依赖文件不变就命中缓存，快）：
FROM python:3.12-slim
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . /app
**【技巧】**想强制不用缓存重新构建，加 --no-cache：docker build --no-cache -t myapp:v1 .。
## 第8章 docker-compose
### 8.1 为什么需要 docker-compose
一个正经项目往往不止一个容器：网页服务 + 数据库 + 缓存，三个容器要互相配合。如果都用 docker run，命令又长又多，还要记住参数，很容易漏。
docker-compose 的解决办法是：把“要启动哪些服务、每个服务什么镜像、什么端口、什么卷”全部写进一个 yml 文件，然后一条命令全部启动。
打个比方：Dockerfile 是“做菜谱”，docker-compose 是“今天晚宴的整份菜单”——一口气安排好几道菜，谁先上、谁后上都有讲究。
现在的 Docker 已经内置了 compose 命令（Docker Desktop 自带），直接 docker compose 就能用。
### 8.2 yaml 语法小白讲解
yml（yaml）是一种“用缩进表示层级”的配置文件。新手最容易在这里翻车，先记住三条铁律：
- 用空格缩进，绝对不能用 Tab。
- 同一层级的配置，缩进的空格数要完全一样。
- 键和值之间，冒号后面必须有一个空格，比如 ports: 不能写成 ports:。
错误示范（缩进混乱 + 冒号没空格）：
services:
  web:
   image: nginx
  ports:
   - "8080:80"
正确示范：
services:
  web:
    image: nginx
    ports:
      - "8080:80"
**【重点】**编辑器里能显示空格/Tab 的（比如 VS Code），开起来，一眼就能看出缩进问题。yaml 解析报错时，十有八九就是缩进或冒号空格。
### 8.3 完整例子：web + redis + mysql 三个服务
新建一个项目文件夹，里面放这个 docker-compose.yml：
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - REDIS_HOST=redis
      - MYSQL_HOST=mysql
    depends_on:
      - redis
      - mysql
    restart: always
  redis:
    image: redis:7
    volumes:
      - redis-data:/data
  mysql:
    image: mysql:8
    environment:
      - MYSQL_ROOT_PASSWORD=123456
    volumes:
      - mysql-data:/var/lib/mysql
    ports:
      - "3306:3306"
volumes:
  redis-data:
  mysql-data:
逐段解释：
- services 下面列出三个服务：web、redis、mysql。
- web 用 build: . 表示“用当前目录的 Dockerfile 构建”（也可以换成 image: xxx 直接用现成镜像）。
- ports 是端口映射，格式和 -p 一样，左边电脑端口，右边容器端口。
- environment 是环境变量，相当于 -e。这里告诉 web：数据库在哪（用服务名 redis、mysql 就能访问）。
- depends_on 表示“先启动 redis 和 mysql，再启动 web”。
- 最下面的 volumes 声明了两个具名卷，给 redis 和 mysql 存数据。
**【重点】**在 compose 里，服务之间互相访问直接写服务名（redis、mysql）就行，compose 会自动把它们放进同一个网络，不用自己配 IP。
### 8.4 常用命令
在 docker-compose.yml 所在目录执行。后台启动所有服务：
docker compose up -d
查看服务状态：
docker compose ps
查看某个服务的日志（实时跟踪加 -f）：
docker compose logs -f web
进入某个服务的容器：
docker compose exec web bash
停止并删除所有容器（默认不删数据卷）：
docker compose down
连数据卷一起删（数据真的没了！）：
docker compose down -v
**【警告】**docker compose down -v 会把 compose 里声明的数据卷一起删掉，数据库数据就没了！平时用 docker compose down 就够了，别手滑加 -v。
### 8.5 常用配置项速查

| 配置项 | 作用 | 例子 |
| --- | --- | --- |
| image | 直接用哪个镜像 | image: nginx:1.27 |
| build | 用哪个目录的 Dockerfile 构建 | build: . |
| container_name | 自定义容器名 | container_name: myweb |
| ports | 端口映射（列表） | ports: ["8080:80"] |
| volumes | 数据卷挂载（列表） | volumes: ["mydata:/data"] |
| environment | 环境变量（列表或字典） | environment: [MYSQL_ROOT_PASSWORD=123456] |
| depends_on | 依赖哪些服务先启动 | depends_on: [redis, mysql] |
| restart | 重启策略 | restart: always |
| command | 覆盖容器启动命令 | command: python app.py |
| networks | 加入哪个网络 | networks: [mynet] |

## 第9章 常用组合实战
### 9.1 实战：跑一个 MySQL
一条命令启动 MySQL 8，端口 3306，数据挂到具名卷，开机自启：
docker run -d --name mysql8 \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -v mysql-data:/var/lib/mysql \
  --restart always \
  mysql:8
验证能否连接：
docker exec -it mysql8 mysql -uroot -p123456
看到 mysql> 提示符就说明数据库好了，输入 exit 退出。
**【警告】**上面的密码 123456 只适合自己本地练手。生产环境请用强密码，并且不要写在命令行里，用 -e 从环境变量或密钥管理工具读。
### 9.2 实战：跑一个 Redis
Redis 是超常用的缓存数据库，启动很简单：
docker run -d --name redis7 -p 6379:6379 -v redis-data:/data redis:7
验证：进入容器，用 redis-cli ping 一下，返回 PONG 就是通了：
docker exec -it redis7 redis-cli ping
需要密码的话，启动命令后面追加一段参数（把密码告诉 redis-server）：
docker run -d --name redis7 -p 6379:6379 \
  -v redis-data:/data \
  redis:7 redis-server --requirepass 123456
### 9.3 实战：Nginx 反向代理
反向代理是什么？大白话：Nginx 站在最前面当“前台接待”，你说“我要看网页”，前台就把请求转给后面的真正干活的服务器（web1、web2）。
第一步：建一个自定义网络，把两个网页容器和一个 nginx 都放进去：
docker network create webnet
docker run -d --name web1 --network webnet nginx
docker run -d --name web2 --network webnet nginx
第二步：准备一个 nginx 配置文件 nginx.conf，把请求全部转发给 web1：
server {
    listen 80;
    server_name _;
    location / {
        proxy_pass http://web1:80;
        proxy_set_header Host $host;
    }
}
第三步：启动反向代理容器，把配置文件挂载进去（:ro 表示只读挂载）：
docker run -d --name nginx-proxy -p 80:80 --network webnet \
  -v D:\nginx\nginx.conf:/etc/nginx/conf.d/default.conf:ro \
  nginx
现在浏览器访问 http://localhost，看到的就是 web1 的内容。以后想换后端，改配置文件重启代理即可。
**【技巧】**反向代理是上班后最常碰到的场景之一：一个域名 + 一个 nginx，背后挂好几个服务，靠路径或端口分流。理解了这个例子，就理解了一半的部署架构。
### 9.4 实战：Portainer 图形化管理面板
嫌命令行麻烦？可以给 Docker 装一个图形界面，叫 Portainer。一条命令搞定：
docker run -d -p 9000:9000 --name portainer \
  --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer-data:/data \
  portainer/portainer-ce
然后浏览器打开 http://localhost:9000，第一次打开会让你设置管理员密码。进去之后，镜像、容器、网络、卷，全都变成网页上的按钮，点点鼠标就能管理。
**【提示】**/var/run/docker.sock 是 Docker 的“控制开关”，把它挂给 Portainer，Portainer 才能替你管理 Docker。这个挂载很强大，只给可信的工具用。
## 第10章 排错与清理
### 10.1 常见问题与解决
学 Docker 的过程，其实就是“报错 → 查错 → 解决”的过程。把最常见的几个坑提前给你，遇到别慌。
#### 问题 1：端口被占用
现象：docker run 报错，里面有 Ports are not available 或 bind: address already in use。
原因：你映射的电脑端口已经被别的程序占了。
解决：查谁占了端口，然后杀掉它，或者换个端口。Windows 查端口占用：
netstat -ano | findstr 8080
看到最后一列是占用程序的 PID（进程号），再杀掉它：
taskkill /PID 1234 /F
Mac / Linux 用户：
lsof -i:8080
kill -9 1234
**【技巧】**懒得查就换端口：把 -p 8080:80 改成 -p 8081:80 再跑一次，最快。
#### 问题 2：镜像拉不下来 / 一直卡住
现象：docker pull 半天不动，或者报网络超时。
原因：默认连的是国外的 Docker Hub，网络不通或太慢。
解决：配置国内镜像加速源（第 2 章 2.3 节），改完重启 Docker 再拉。
#### 问题 3：容器一启动就退出（秒退）
现象：docker ps 看不到它，docker ps -a 里显示 Exited。
原因：容器里的主程序跑完就结束了，或者程序启动时报错退出。注意：容器不是“常驻的虚拟机”，它只在主程序活着的时候活着。
解决：先看日志，报错一目了然：
docker logs mynginx
常见原因举例：CMD 里写的命令执行完就退出（比如 CMD ["echo", "hi"] 打印完就结束）；程序连不上数据库报错退出；配置写错。对症下药即可。
#### 问题 4：进不去容器
现象：docker exec -it 容器名 bash 报 no such file or directory。
原因：这个精简镜像里没有 bash，只有 sh（比如 alpine 系列）。
解决：把 bash 换成 sh：
docker exec -it 容器名 sh
#### 问题 5：容器时间不对（时区问题）
现象：容器里日志时间比北京时间慢 8 小时。
原因：默认是 UTC 时区。
解决：启动时传时区环境变量：
docker run -d -e TZ=Asia/Shanghai nginx
### 10.2 docker stats：实时看资源
像任务管理器一样，实时看每个容器吃了多少 CPU 和内存：
docker stats
只看一次、退出：
docker stats --no-stream
如果某个容器内存一直疯涨，多半是程序有内存泄漏，赶紧排查。
### 10.3 docker system df：看磁盘被谁占了
Docker 用久了，磁盘会悄悄变大（镜像、容器、卷、构建缓存）。df 帮你盘点：
docker system df
输出里 TYPE 有 Images（镜像）、Containers（容器）、Local Volumes（数据卷）、Build Cache（构建缓存）；RECLAIMABLE 列表示“可以清理掉的部分”。
### 10.4 docker system prune：一键清理
清理“停止的容器、没人用的网络、悬空镜像、构建缓存”：
docker system prune
更彻底一点，把没被任何容器使用的镜像也删掉（会提示确认，输入 y）：
docker system prune -a
连数据卷一起清（最彻底，也最危险）：
docker system prune -a --volumes
**【警告】**prune -a --volumes 会把“所有没在使用的镜像和数据卷”全删掉，删了就没法恢复！执行前先 docker system df 和 docker volume ls 看清楚，确认没有需要保留的数据再动手。
## 第11章 安全与生产技巧
### 11.1 非 root 运行
默认情况下，容器里用的是 root 用户，权限很大。万一容器被攻破，攻击者拿到的是 root 权限，后果严重。
生产环境的原则：能不用 root 就不用。两种做法：
做法一：Dockerfile 里切用户：
FROM nginx:alpine
RUN adduser -D appuser
USER appuser
做法二：docker run 时指定用户（用 UID 更通用）：
docker run -d --user 1000:1000 nginx
**【技巧】**结合数据卷使用时注意：挂载目录的权限要和你指定的用户匹配，否则容器里会“没权限写文件”。
### 11.2 只读文件系统 --read-only
如果程序运行中根本不需要写文件，可以把整个文件系统设成只读，攻击者想往里写东西都写不了：
docker run -d --name ro-nginx --read-only --tmpfs /tmp nginx
--read-only 让文件系统只读；--tmpfs /tmp 单独给 /tmp 开一块可写内存盘，因为很多程序要临时写点东西。
验证一下：进容器尝试写文件会失败：
docker exec ro-nginx touch /abc.txt
会看到 Read-only file system 的报错——这正是我们要的效果。
### 11.3 HEALTHCHECK 健康检查
怎么知道一个容器“活着但其实是坏的”（比如程序卡死但进程还在）？健康检查就是定期去探一下服务的“脉搏”。
方式一：Dockerfile 里写：
FROM nginx:alpine
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -q --spider http://localhost/ || exit 1
构建后运行，查看健康状态：
docker inspect --format "{{.State.Health.Status}}" mynginx
输出 healthy 表示健康，unhealthy 表示已经挂了。
方式二：compose 里写：
services:
  web:
    image: mypyapp:v1
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000"]
      interval: 30s
      timeout: 3s
      retries: 3
**【重点】**编排系统（比如后面可能接触的 Kubernetes）会根据健康检查结果自动重启坏掉的容器，所以健康检查写得越准，服务越稳。
### 11.4 资源限制
生产环境一定要给容器限资源，防止一个容器把整台机器吃垮：
docker run -d --name mynginx \
  --cpus 0.5 \
  --memory 512m \
  --pids-limit 100 \
  nginx
--cpus 0.5 最多用半个 CPU 核；--memory 512m 最多用 512MB 内存（超出会被杀）；--pids-limit 100 最多创建 100 个进程（防 fork 炸弹）。
已经运行的容器也能改：
docker update --cpus 0.3 --memory 256m mynginx
查看容器当前的资源限制：
docker inspect mynginx | findstr /C:"Memory" /C:"NanoCpus"
### 11.5 日志大小限制
默认情况下容器日志会一直往磁盘写，日志多了能把磁盘写满。给日志加上限：
docker run -d --name mynginx \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  nginx
意思是：每个日志文件最大 10MB，最多保留 3 个文件。compose 里这样写：
services:
  web:
    image: nginx
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"
**【技巧】**上线新服务前，先把日志限制配上，等于给磁盘上了保险。
## 附录
### 附录A 命令速查总表
把全书命令汇总成一张大表，命令里的 <尖括号> 内容要替换成你自己的。复制粘贴时注意参数顺序。

| 命令 | 作用 | 例子 |
| --- | --- | --- |
| docker search <名字> | 搜索镜像 | docker search nginx |
| docker pull <镜像名> | 下载镜像 | docker pull nginx |
| docker pull <镜像名>:<标签> | 下载指定版本 | docker pull redis:7-alpine |
| docker images | 查看本地镜像列表 | docker images |
| docker image ls | 查看本地镜像列表（等价写法） | docker image ls |
| docker tag <旧名> <新名> | 给镜像打标签 | docker tag nginx:latest mynginx:v1 |
| docker rmi <镜像名> | 删除镜像 | docker rmi mynginx:v1 |
| docker rmi -f <镜像名> | 强制删除镜像 | docker rmi -f nginx |
| docker build -t <名字> . | 用 Dockerfile 构建镜像 | docker build -t myapp:v1 . |
| docker build --no-cache -t <名字> . | 不用缓存重新构建 | docker build --no-cache -t myapp:v1 . |
| docker push <名字> | 推送镜像到仓库 | docker push 你的账号/myapp:v1 |
| docker login | 登录镜像仓库 | docker login |
| docker history <镜像名> | 看镜像构建历史 | docker history nginx |
| docker run <镜像名> | 运行容器 | docker run hello-world |
| docker run -d <镜像名> | 后台运行容器 | docker run -d nginx |
| docker run -p 8080:80 <镜像名> | 端口映射（左外右内） | docker run -d -p 8080:80 nginx |
| docker run --name <名字> <镜像名> | 指定容器名 | docker run -d --name mynginx nginx |
| docker run -e 变量=值 <镜像名> | 传环境变量 | docker run -d -e MYSQL_ROOT_PASSWORD=123456 mysql:8 |
| docker run -v 卷:路径 <镜像名> | 挂载数据卷 | docker run -d -v mydata:/data nginx |
| docker run -it <镜像名> bash | 交互式进入容器 | docker run -it ubuntu bash |
| docker run --rm <镜像名> | 退出自动删除容器 | docker run --rm hello-world |
| docker run --restart always <镜像名> | 开机自启+崩溃重启 | docker run -d --restart always nginx |
| docker run --cpus 0.5 <镜像名> | 限制 CPU | docker run -d --cpus 0.5 nginx |
| docker run --memory 512m <镜像名> | 限制内存 | docker run -d --memory 512m nginx |
| docker ps | 查看运行中的容器 | docker ps |
| docker ps -a | 查看所有容器 | docker ps -a |
| docker ps -aq | 只显示所有容器 ID | docker ps -aq |
| docker start <容器名> | 启动已停止的容器 | docker start mynginx |
| docker stop <容器名> | 停止容器 | docker stop mynginx |
| docker restart <容器名> | 重启容器 | docker restart mynginx |
| docker kill <容器名> | 强制杀掉容器 | docker kill mynginx |
| docker rm <容器名> | 删除已停止的容器 | docker rm mynginx |
| docker rm -f <容器名> | 强制删除容器 | docker rm -f mynginx |
| docker rm -f $(docker ps -aq) | 删除所有容器 | docker rm -f $(docker ps -aq) |
| docker exec -it <容器名> bash | 进入容器执行命令 | docker exec -it mynginx bash |
| docker logs <容器名> | 查看容器日志 | docker logs mynginx |
| docker logs -f <容器名> | 实时跟踪日志 | docker logs -f mynginx |
| docker logs --tail 50 <容器名> | 只看最后 50 行日志 | docker logs --tail 50 mynginx |
| docker cp 容器:路径 本机路径 | 容器文件拷到本机 | docker cp mynginx:/etc/nginx/nginx.conf ./n.conf |
| docker cp 本机路径 容器:路径 | 本机文件拷进容器 | docker cp ./index.html mynginx:/usr/share/nginx/html/ |
| docker top <容器名> | 查看容器内进程 | docker top mynginx |
| docker stats | 实时查看资源占用 | docker stats |
| docker stats --no-stream | 只看一次资源占用 | docker stats --no-stream |
| docker inspect <容器名> | 查看容器详细信息 | docker inspect mynginx |
| docker network ls | 查看网络列表 | docker network ls |
| docker network create <名字> | 创建自定义网络 | docker network create mynet |
| docker network rm <名字> | 删除网络 | docker network rm mynet |
| docker network inspect <名字> | 查看网络详情 | docker network inspect mynet |
| docker network connect <网络> <容器> | 把容器加入网络 | docker network connect mynet web1 |
| docker volume ls | 查看数据卷 | docker volume ls |
| docker volume create <名字> | 创建数据卷 | docker volume create mydata |
| docker volume inspect <名字> | 查看数据卷详情 | docker volume inspect mydata |
| docker volume rm <名字> | 删除数据卷 | docker volume rm mydata |
| docker volume prune | 清理无用数据卷 | docker volume prune |
| docker compose up -d | 后台启动所有服务 | docker compose up -d |
| docker compose ps | 查看服务状态 | docker compose ps |
| docker compose logs -f <服务> | 查看某服务日志 | docker compose logs -f web |
| docker compose exec <服务> bash | 进入某服务容器 | docker compose exec web bash |
| docker compose down | 停止并删除容器 | docker compose down |
| docker compose down -v | 连数据卷一起删 | docker compose down -v |
| docker version | 查看版本 | docker version |
| docker info | 查看系统信息 | docker info |
| docker system df | 查看磁盘占用 | docker system df |
| docker system prune | 清理无用资源 | docker system prune |
| docker system prune -a | 全量清理镜像 | docker system prune -a |
| docker update --cpus 0.3 <容器名> | 修改运行中容器的资源限制 | docker update --cpus 0.3 mynginx |

### 附录B 常见坑清单
遇到问题先来这里对号入座。

| 坑 | 现象 | 解决 |
| --- | --- | --- |
| 端口被占用 | 报错 Ports are not available / bind: address already in use | netstat 查占用，杀掉进程或换 -p 端口 |
| 镜像拉不下来 | docker pull 一直卡住或超时 | 配置国内镜像加速源（第 2 章），重启 Docker 再拉 |
| 容器秒退 | docker ps 看不到，ps -a 显示 Exited | docker logs <容器名> 看报错，多半是程序没前台进程或配置错 |
| 进不去容器 | 报 exec: no such file or directory | 容器里没有 bash，改用 sh：docker exec -it <容器名> sh |
| 数据没了 | 删容器后数据库数据消失 | 用数据卷 -v 挂载（第 5 章），容器可以随便删 |
| 端口映射不生效 | 浏览器打不开页面 | -p 左边写电脑端口、右边写容器端口，看 docker ps 的 PORTS 列 |
| 忘了容器名 | 不知道操作哪个容器 | docker ps -a 查看 NAMES 列 |
| 容器里改的东西重启就没了 | 重启后配置恢复原样 | 把改动写进 Dockerfile 重新构建，或挂载数据卷 |
| 时间不对 | 容器日志比北京时间慢 8 小时 | 启动时加 -e TZ=Asia/Shanghai |
| 挂载目录没权限 | 容器里写文件报 Permission denied | 检查 -v 目录权限，或用 --user 指定与目录匹配的用户 |
| yaml 解析报错 | docker compose up 报 YAML 错误 | 缩进用空格不要用 Tab，冒号后要有空格 |
| docker build 很慢 | 每次构建都重装依赖 | 先 COPY 依赖文件再装依赖（利用缓存），或换国内 pip 源 |
| rmi 删不掉镜像 | 报 image is being used by container | 先删使用该镜像的容器，再删镜像 |
| 磁盘越来越满 | /var/lib/docker 占用巨大 | docker system df 查看，docker system prune 清理 |
| 容器连不上数据库 | 程序连 localhost 报拒绝连接 | 容器之间用服务名/容器名访问，不要用 localhost（localhost 指容器自己） |
| Docker Desktop 起不来 | 引擎一直 starting | 确认 WSL2 已开启、BIOS 虚拟化已打开，重启 Docker Desktop |

## 相关笔记

- [[Linux系统使用技巧]]
- [[程序员知识库]]
- [[网络运维知识大全]]
