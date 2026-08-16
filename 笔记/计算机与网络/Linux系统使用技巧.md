# Linux系统使用技巧

> 科目：计算机与网络 ｜ 收录日期：2026-08-16 ｜ 原文：《Linux系统使用技巧（小白版）.docx》

（上班/开发实用大全 · 小白版）
—— 给完全零基础的同学：从"什么是 Linux"到"上班排查故障"，一步一步带你入门。
本手册配套说明：本文档为教学资料，文中所有命令均以 Ubuntu/Debian 系为主要演示环境（CentOS/Rocky 系命令会单独标注）。
## 写在前面：这份文档怎么用
你好，欢迎来到 Linux 世界！这份文档是专门给"完全没接触过 Linux 的小白"写的。你不用有任何基础，只要会开电脑、会用键盘，就能跟着学。在开始之前，请先花两分钟看看下面几条"使用说明"，会让你的学习效率高很多：
- 建议从头按顺序读。第 1、2 章是背景和装环境，第 3 章开始才是真刀真枪敲命令，第 4 章《文件与目录》是重中之重，值得反复看。
- 看到灰色的"代码块"，不要只读，要动手敲一遍。命令这东西，看一百遍不如敲一遍记得牢。
- 代码块里出现的"xxx""你的用户名"这类占位词，要换成你自己的内容。比如把 IP 地址换成你自己服务器的 IP。
- 带【警告】标签的提示框，一定要认真看——里面讲的是可能造成数据丢失或严重后果的操作。
- 不用强求一次记住所有命令。常用命令每天用，自然就记住了；记不住的，翻附录A《命令速查总表》就行。
- 遇到报错先别慌：第 15 章专门总结了最常见的报错和解决办法，先翻翻那里。
好了，我们正式开始。先回答一个最基础的问题：Linux 到底是什么？
## 目录
- 第1章　Linux 到底是什么
- 第2章　怎么开始用
- 第3章　终端第一课
- 第4章　文件与目录（重点，最常用）
- 第5章　权限与用户
- 第6章　看系统看进程
- 第7章　文本三剑客
- 第8章　压缩打包
- 第9章　安装软件
- 第10章　vim
- 第11章　Shell 脚本
- 第12章　systemd
- 第13章　网络
- 第14章　上班实战组合技
- 第15章　常见报错
- 附录A　命令速查总表
- 附录B　学习路线建议
## 第1章　Linux 到底是什么
### 1.1 操作系统 = 电脑的大管家
先打个比方。一台电脑由两部分组成：硬件和操作系统。硬件是看得见摸得着的东西——CPU（大脑）、内存（工作台）、硬盘（仓库）、键盘鼠标屏幕（手脚眼）。但硬件本身是"死"的，它不知道自己该干什么。这时候就需要一个"大管家"来指挥它，这个大管家就是操作系统。
大管家的工作包括：哪个程序该用 CPU、内存分给谁、文件存在硬盘的哪个角落、你按一下键盘它该把这件事告诉哪个程序。没有管家，你让电脑干活，它根本不知道该听谁的。
你平时用的 Windows、手机里的 Android 和 iOS，都是操作系统。Linux 是另一个操作系统，干的活儿和 Windows 一样，只是长得不一样、习惯不一样。你在 Windows 上点鼠标，在 Linux 上更多是敲命令——就像 Windows 是"用遥控器看电视"，Linux 是"直接拿螺丝刀修电视"，更直接，也更强大。
**【重点】**操作系统不是某个软件，而是"电脑上所有软件运行的底座"。Linux、Windows、macOS 都是操作系统。
### 1.2 Linux 与 Windows 的区别
把两者放在一起对比，你就明白 Linux 的定位了：

| 对比项 | Windows | Linux |
| --- | --- | --- |
| 价格 | 正版要花钱买授权 | 免费、开源，随便装多少台 |
| 主要用在哪 | 个人电脑、办公、游戏 | 服务器、云主机、手机(安卓底层)、路由器 |
| 操作方式 | 鼠标点图形界面为主 | 命令行为主，图形界面可选装 |
| 稳定性 | 一般，偶尔蓝屏 | 极稳，服务器常年不重启 |
| 安全性 | 病毒、木马多 | 权限管理严格，病毒少 |
| 可定制性 | 封闭，改不动 | 开源，源码随便看随便改 |
| 典型场景 | 日常办公娱乐 | 网站、数据库、App 后端都在它上面跑 |

### 1.3 为什么服务器和公司都用它
你去上班后会发现，公司里的服务器（就是那些 24 小时不关机、托管着网站和数据的电脑）几乎全是 Linux。原因可以总结成五条：
- 免费：服务器软件要按"台数"收版权费，公司动辄几百台服务器，用 Linux 能省下一大笔钱。
- 稳定：Linux 服务器经常一跑就是一两年不重启，不像家用电脑动不动蓝屏死机。
- 安全：Linux 的权限模型非常严格（第 5 章细讲），而且代码开源，全世界的安全专家一起盯着，漏洞发现得早、修得快。
- 轻量：没有花哨的图形界面，一个命令行系统只占很少的内存，老机器也能带得动。
- 生态：互联网公司用的 Nginx、MySQL、Docker、Kubernetes 这些核心软件，都是先支持 Linux。你想做后端开发、运维，绕不开它。
**【重点】**一句话总结：在公司里，"服务器"和"Linux"几乎可以画等号。学 Linux 就是学怎么管理服务器。
### 1.4 常见发行版怎么选
Linux 有很多"版本"，专业说法叫"发行版"。你可以把 Linux 内核想象成一台发动机，不同的发行版就是装上不同外壳和配置的整车。发动机都一样，但车子的内饰、配件不同。常见的有这几个：

| 发行版 | 特点 | 适合谁 |
| --- | --- | --- |
| Ubuntu | 新手最友好，资料最多，桌面服务器通吃，用 apt 装软件 | 学习练手首选，很多云服务器的默认系统 |
| CentOS | 老牌服务器系统，但官方已停止维护，不建议新项目再用 | 老项目可能还在用，遇到要会看 |
| Rocky Linux | CentOS 的"接班人"，用法几乎一模一样，用 yum/dnf | 公司生产服务器常见 |
| Debian | 极稳、极省资源，Ubuntu 的"爹"，用 apt | 追求稳定、喜欢折腾的老手 |

给你一个最简单的选择公式：自己学习练手 → 装 Ubuntu；公司生产服务器 → 用 Rocky 或 Debian；买云服务器 → 厂商默认给什么就用什么（一般是 Ubuntu 或 CentOS 系）。
**【提示】**各发行版的命令九成是通用的，区别主要在"装软件的命令"（apt 还是 yum）。放心学，换系统不用重新学。
## 第2章　怎么开始用
### 2.1 三种入门方式，先选一个
纸上谈兵没意思，我们得真有一个 Linux 环境来敲命令。对新手来说有三种方式，各有优缺点：

| 方式 | 适合谁 | 优点 | 缺点 |
| --- | --- | --- | --- |
| 虚拟机装 Ubuntu | 纯新手练手 | 免费、随便折腾、弄坏了重装就行 | 占内存和硬盘，配置略麻烦 |
| WSL2（推荐） | Windows 用户、上班族 | Windows 自带、启动快、和 Windows 文件互通 | 和真实服务器有细微差别 |
| 云服务器 | 想体验真实工作 | 真服务器，能搭网站给别人访问 | 要花钱（一般有免费试用） |

如果你用的是 Windows 电脑，我强烈推荐先用 WSL2——它是微软官方出的，装好后打开一个窗口就能敲 Linux 命令，上班最方便。下面三种方式都讲一遍，你按自己的情况选一种。
### 2.2 方式一：虚拟机装 Ubuntu
虚拟机 = 在你现在的电脑里"模拟"出一台全新的电脑。步骤大致如下：
- 第 1 步：下载虚拟机软件 VirtualBox（免费，官网 virtualbox.org）。
- 第 2 步：下载 Ubuntu 的安装镜像 ISO 文件（官网 ubuntu.com，选 LTS 长期支持版，比如 22.04 或 24.04）。
- 第 3 步：打开 VirtualBox，点"新建"，名字随便起（比如 ubuntu），类型选 Linux，内存分 2~4GB，硬盘分 20~40GB。
- 第 4 步：启动虚拟机，选择刚才下载的 ISO 文件，进入安装界面。
- 第 5 步：一路"下一步"，语言选简体中文，时区选上海，创建一个用户名和密码，等它装完重启。
装完之后你就拥有了一个完整的 Ubuntu 系统，想怎么折腾都行，弄坏了删掉重装，反正不影响你本机。
### 2.3 方式二：WSL2（Windows 自带，上班最方便）
WSL 的全称是 Windows Subsystem for Linux，意思是"Windows 里的 Linux 子系统"。装好之后，你可以在 Windows 里直接打开一个 Linux 终端，就像打开一个普通程序一样。安装步骤：
- 第 1 步：以"管理员身份"打开 PowerShell（开始菜单搜索 PowerShell，右键"以管理员身份运行"）。
- 第 2 步：输入下面这条命令，然后回车，等待下载完成：
wsl --install
- 第 3 步：重启电脑。重启后系统会让你设置 Linux 的用户名和密码，设完就进入 Linux 终端了。
- 第 4 步：以后想用，直接在开始菜单搜索"Ubuntu"打开就行。
常用管理命令：
wsl -l -v              # 查看已安装的发行版和版本
wsl --set-default-version 2   # 确保用 WSL2
wsl --shutdown                # 关闭 WSL（想彻底重启时用）
**【技巧】**WSL2 里的文件就存在你电脑上，路径是 \\wsl.localhost\Ubuntu\home\你的用户名（在 Windows 资源管理器地址栏输入就能访问），两边文件可以互相拷贝。
**【提示】**WSL2 里的命令和真实 Linux 一模一样，公司上班练手，用它就够了，不用折腾虚拟机。
### 2.4 方式三：云服务器
云服务器就是在阿里云、腾讯云、华为云、AWS 这些平台上"租"一台永远开着的电脑。买的时候你会拿到三样东西：公网 IP（一台服务器的门牌号）、用户名（一般是 root 或 ubuntu）、密码。
买完之后第一件事：去控制台的"安全组"或"防火墙"里，确认放行了 22 端口（SSH 远程登录用的端口）。不放行的话，下面教你的远程连接会连不上。新手建议先用免费试用套餐练手。
### 2.5 远程连接工具：Xshell / FinalShell
服务器在云端，你怎么操作它？答案是远程连接。Windows 上常用的两个工具：
- Xshell：老牌免费工具，稳定，很多公司都在用。
- FinalShell：国产免费，自带中文界面和图形化的 CPU/内存监控，对新手更友好。
连接步骤都一样：新建会话 → 填三样东西（主机 IP、端口 22、用户名）→ 连接后输密码。也可以用命令行直接连（这个后面第 13 章细讲）：
ssh root@你的服务器IP地址
**【重点】**注意：服务器的操作几乎全在这个"黑窗口"里完成，没有鼠标可点。所以学会命令行是必须的，这正是第 3 章开始教的内容。
## 第3章　终端第一课
### 3.1 提示符长什么样
打开终端，你会看到屏幕上有一行类似这样的文字，它叫"提示符"，意思是"我准备好了，请下命令"：
user@my-server:~$
别怕，这串符号拆开看特别简单：
- user：当前登录的用户名（换成你的是 zhangsan 就显示 zhangsan）。
- my-server：这台电脑的主机名。
- ~：当前所在的目录。~ 是"家目录"的简写（第 4 章细讲）。
- $：表示你现在是普通用户。如果显示的是 #，说明你是 root 超级管理员——权限大，责任也大。
光标就在 $ 后面闪烁，你敲什么它就显示什么，敲完按回车，命令开始执行。
### 3.2 命令 = 命令 + 空格 + 参数
一条命令的结构是固定的，就像填表格：先写"命令名"（要干什么），再写"选项"（怎么干，通常以 - 开头），再写"参数"（对谁干），中间用空格隔开。看例子：
ls -l /home
这条命令拆开是：
- ls：命令名，意思是"列出文件"（list）。
- -l：选项，意思是"用详细方式列出"（long）。
- /home：参数，告诉它"列哪个目录"。
选项可以合并写，比如 ls -l -a 可以写成 ls -la；参数可以有多个，比如 cp a.txt b.txt 就是把 a.txt 复制成 b.txt。
**【提示】**命令和参数之间必须有空格，写错了系统会提示 command not found（找不到命令）。
### 3.3 四个救命操作：Tab、上下箭头、Ctrl+C、Ctrl+L
先学这四个，能让你少打很多字、少踩很多坑：
- Tab 自动补全：敲 cd /e 然后按 Tab 键，系统自动帮你补全成 cd /etc。如果有多个可能，连按两次 Tab，系统会把所有可能列出来。
- 上下箭头：按 ↑ 键翻出之前敲过的命令，不用重新打字。按 ↓ 往下翻。
- Ctrl+C：中止当前正在运行的命令。比如你 ping 一个地址停不下来，按 Ctrl+C 就停了。
- Ctrl+L：清屏，让屏幕干净一点（等价于敲 clear 命令）。
**【技巧】**Ctrl+C 是"中止"，不是"复制"。在终端里复制粘贴的快捷键是鼠标右键或 Ctrl+Shift+C / Ctrl+Shift+V，别搞混了。
### 3.4 查帮助：man 和 --help
命令太多记不住？系统自带"说明书"。两种查法：
man ls          # 打开 ls 的完整说明书（手册）
ls --help       # 快速看 ls 的用法摘要
man 打开的说明书里：空格键翻下一页，b 键翻上一页，输入 /关键字 可以搜索，按 q 键退出。几乎所有命令都支持 --help 这种"快捷帮助"。
**【技巧】**忘了某个命令怎么用，先敲"命令 --help"看摘要，看不懂再"man 命令"看全文。这是每个 Linux 老手的第一反应。
## 第4章　文件与目录（重点，最常用）
这一章是全书最重要的章节。在 Linux 上干活，八成时间都在和文件、目录打交道。学完这一章，你就已经能独立完成很多日常工作了。
### 4.1 Linux 的目录结构：一棵倒着长的大树
Linux 把所有东西都组织成一棵"树"：最顶上（树根）是一个目录，叫 /（读作"根"）。/ 下面分出很多子目录，子目录里又有子目录……任何一个文件的完整路径，都是从 / 开始的。
和 Windows 最大的不同：Windows 有 C 盘、D 盘好几个"树根"，而 Linux 永远只有一根树，所有硬盘都要"挂"到这棵树的某个目录下面。先认识这几个最常打交道的目录：

| 目录 | 存放什么 | 常用例子 |
| --- | --- | --- |
| / | 根目录，一切从这里开始 | cd / |
| /home | 普通用户的家目录，每个用户一个小窝 | cd ~ 等价于 cd /home/你的用户名 |
| /root | root 超级管理员的家目录 | cd /root |
| /etc | 系统配置文件所在地 | cat /etc/hosts |
| /var | 经常变化的文件：日志、缓存 | tail -f /var/log/syslog |
| /tmp | 临时文件，重启可能被清空 | cd /tmp |
| /usr | 安装的软件和程序（类似 Windows 的 Program Files） | ls /usr/bin | head |
| /bin /sbin | 系统命令存放处 | which ls |

记住两个概念：绝对路径是从 / 开始写的完整路径，比如 /etc/hosts；相对路径是相对于"当前所在目录"写的，比如你在 /home 下，写 zhangsan 就是指 /home/zhangsan。家目录 ~ 永远指"当前用户的小窝"。
### 4.2 pwd：我现在在哪
pwd（print working directory）显示你当前所在的目录全路径。迷路了就敲它：
pwd
# 输出示例：
# /home/zhangsan
**【技巧】**记住这个习惯：新登录一台服务器，先敲 pwd 看看自己在哪，再开始干活。
### 4.3 ls：列出文件
ls（list）是使用频率最高的命令，作用是把当前目录里的东西列出来。几个常用变体：
ls              # 简单列出
ls -l           # 详细列出（权限、属主、大小、时间）
ls -a           # 列出所有文件，包括隐藏文件（名字以 . 开头的）
ls -lh          # 人性化大小，自动显示 K/M/G
ls -R           # 递归列出所有子目录的内容
看个例子：
ls -lh
# 输出示例：
# -rw-r--r-- 1 root root 4.0K Apr 10 10:00 test.txt
# drwxr-xr-x 2 root root 4.0K Apr 10 09:30 mydir
第一列最开头的 d 表示这是一个目录（directory），- 表示普通文件。这一大串权限信息，第 5 章会逐字段讲解，先混个眼熟。
### 4.4 cd：切换目录
cd（change directory）就是"进入某个目录"，相当于 Windows 里双击文件夹。最常用写法：
cd /etc        # 进入 /etc（绝对路径）
cd ~           # 回到自己的家目录
cd             # 什么都不写，也是回家里
cd ..          # 回到上一级目录
cd ../..       # 往上跳两级
cd -           # 回到上一个待过的目录（来回切换神器）
cd /           # 回到根目录
**【重点】**Windows 路径用反斜杠 \ 分隔，Linux 全部用正斜杠 /，千万别混。
### 4.5 mkdir 和 touch：新建目录和文件
mkdir（make directory）建目录，touch 建空文件（或更新已有文件的时间戳）：
mkdir test              # 创建名为 test 的目录
mkdir -p a/b/c          # 一次创建多层目录（-p 自动补中间层）
touch a.txt             # 创建一个空文件 a.txt
touch a.txt             # a.txt 已存在时，只更新它的修改时间
### 4.6 cp、mv、rm：复制、移动、删除
这三个是日常三大件，先看复制和移动：
cp a.txt b.txt          # 把 a.txt 复制成 b.txt
cp -r mydir mydir2      # 复制整个目录（必须加 -r，递归）
mv a.txt b.txt          # 把 a.txt 改名为 b.txt
mv a.txt /tmp/          # 把 a.txt 移动到 /tmp 目录
再看删除——请睁大眼睛看警告：
rm a.txt                # 删除文件 a.txt
rm -r mydir             # 删除目录（-r 递归）
rm -rf mydir            # 强制递归删除，不询问
**【警告】**Linux 删除文件没有"回收站"，rm -rf 删掉的东西找不回来！尤其是 rm -rf /、rm -rf *、rm -rf ~ 这三条，千万别在家目录或根目录下乱敲。生产服务器上敲错 = 事故。
**【技巧】**实在怕删错，可以先 mv 到 /tmp 观察几天，确认没问题再删。这是很多老手的习惯。
### 4.7 看文件内容：cat、less、head、tail
看文件内容有四种姿势，按文件大小和目的选：
cat /etc/hosts           # cat 适合看短文件，一下全打印
less /var/log/syslog     # less 适合长文件：空格翻页，q 退出，/关键字搜索
head -n 5 app.log        # 只看文件开头 5 行
tail -n 10 app.log       # 只看文件末尾 10 行
tail -f app.log          # 实时跟随文件末尾，新增内容自动滚出来
重点说说 tail -f：这是运维和开发的"神器"。程序在运行时会不断往日志文件里写内容，tail -f 能让新内容实时滚出来，你就能盯着日志看程序干了什么。按 Ctrl+C 停止跟随。
### 4.8 查找：find、grep、which、file、stat
文件多了找不到？四个查找命令分工不同：
find /home -name "*.log"               # 按名字找文件
find / -name "nginx.conf" 2>/dev/null   # 全盘找，报错丢黑洞
find /home -type f -size +100M          # 找超过 100M 的大文件
grep "error" app.log                    # 在文件里搜含 error 的行
which python3                           # 查命令安装在哪个路径
file a.txt                              # 看文件真实类型
stat a.txt                              # 看文件的详细信息（大小/权限/时间）
find 是按"文件名/大小/时间"找文件；grep 是按"内容"找行（第 7 章细讲）；which 是查命令在哪。三兄弟各管一摊。
### 4.9 通配符：*、?、[ ]
通配符就是"模糊匹配"，shell 会帮你自动展开成多个文件，特别适合批量操作：
ls *.txt          # * 匹配任意多个字符：列出所有 .txt 结尾的文件
ls file?.log      # ? 匹配任意一个字符：file1.log、fileA.log 都能匹配
ls file[123].txt  # [ ] 匹配括号里任意一个：file1.txt、file2.txt、file3.txt
rm -rf *.log      # 危险示例：删掉所有 .log 文件，慎用
**【技巧】**通配符是"shell 帮你展开的"——你敲 ls *.txt，shell 先把 *.txt 换成所有匹配的文件名，再交给 ls 执行。
### 4.10 实战一：实时看日志
场景：Nginx 网站日志在 /var/log/nginx/access.log，你想看现在有没有人访问：
tail -f /var/log/nginx/access.log
# 每来一个请求，自动刷出一行访问记录
# 按 Ctrl+C 退出
再配合 grep 过滤：只想看访问出错的请求，可以开两个终端，或者用管道（第 7 章）组合：
tail -f /var/log/nginx/access.log | grep ' 404 '
### 4.11 实战二：找大文件、看目录大小
场景：磁盘快满了，想知道谁占的地方最多（第 14 章还会系统讲）：
find / -type f -size +500M 2>/dev/null | head -20   # 全盘找大于 500M 的文件
du -sh /home/* | sort -rh | head -10                    # 家目录下每个子目录大小，从大到小排
**【技巧】**2>/dev/null 的意思是"把错误信息扔进黑洞（/dev/null）"，这样没有权限读的目录报错就不会刷屏，只留下有效结果。
练一练：打开终端，依次执行 pwd、ls -l、mkdir mytest、cd mytest、touch hello.txt、cd ..、rm -r mytest，把这一串走一遍，你就掌握了本章八成的内容。
## 第5章　权限与用户
### 5.1 rwx：文件的门禁卡
再打个比方：每个文件和目录都挂着一张"门禁卡"，上面写着三类人分别能干什么：
- r（read，读）：能不能看内容。对应数字 4。
- w（write，写）：能不能改内容。对应数字 2。
- x（execute，执行）：文件能不能当程序运行、目录能不能进去。对应数字 1。
把这三个数字加起来，就是权限的数字表示。比如 rwx = 4+2+1 = 7，rw- = 4+2 = 6，r-x = 4+1 = 5，r-- = 4。一张门禁卡上有三组权限：文件主人（属主）一组、同组的用户一组、其他人一组。
### 5.2 ls -l 的输出，逐字段看懂
用 ls -l 看到的每一行，都是一张完整的"门禁卡 + 名片"，我们拆开看：
-rw-r--r-- 1 root root 4096 Apr 10 10:00 test.txt

| 字段 | 例子 | 含义 |
| --- | --- | --- |
| 第1个字符 | - | 文件类型：- 普通文件，d 目录，l 链接 |
| 第2~4个字符 | rw- | 属主权限：能读能写，不能执行 |
| 第5~7个字符 | r-- | 同组用户权限：只能读 |
| 第8~10个字符 | r-- | 其他人权限：只能读 |
| 第2列 | 1 | 硬链接数（暂时忽略） |
| 第3列 | root | 属主（文件的主人） |
| 第4列 | root | 属组（属于哪个组） |
| 第5列 | 4096 | 文件大小（字节） |
| 第6~8列 | Apr 10 10:00 | 最后修改时间 |
| 第9列 | test.txt | 文件名 |

数字和字母的对应关系背下来：7=rwx，6=rw-，5=r-x，4=r--，0=---。后面 chmod 全靠它。
### 5.3 chmod：改权限（数字法和字母法）
chmod（change mode）修改权限。先看数字法——三个数字分别代表属主、组、其他人的权限：
chmod 755 run.sh    # 属主 rwx(7)，组 r-x(5)，其他人 r-x(5) —— 最常用的可执行文件权限
chmod 644 a.txt     # 属主 rw-(6)，组 r--(4)，其他人 r--(4) —— 最常用的普通文件权限
chmod 600 key.pem   # 属主 rw-，其他人啥都不能干 —— 私密文件权限
再看字母法——用 u（属主）、g（组）、o（其他人）、a（所有人）加上 + 或 - 来增减权限：
chmod u+x run.sh     # 给属主加执行权限（最常用）
chmod g-w a.txt     # 去掉同组用户的写权限
chmod o-r a.txt     # 去掉其他人的读权限
chmod +x run.sh     # 给所有人加执行权限
**【重点】**目录的 x 权限 = "能不能进入这个目录"。所以目录一般至少是 755，否则别人连进去都进不去。
**【提示】**改权限前先 ls -l 看清楚现在是什么权限，别闭着眼 chmod 777（所有人都能改，很危险）。
### 5.4 chown：换主人
chown（change owner）修改文件的主人（属主）和属组。一般要加 sudo：
sudo chown zhangsan a.txt        # 把 a.txt 的属主改成 zhangsan
sudo chown zhangsan:dev a.txt    # 属主改成 zhangsan，属组改成 dev
sudo chown -R zhangsan:dev /var/www   # -R 递归：整个目录及其内容一起改
典型场景：网站代码目录 /var/www 的属主是 root，你改不了文件，一条命令把整个目录交给你：sudo chown -R $USER:$USER /var/www。
### 5.5 用户管理：useradd、passwd、su、sudo
一台服务器上可以有很多用户，一人一个账号，谁干了什么一查便知。常用命令：
sudo useradd tom          # 新建用户 tom
sudo passwd tom           # 给 tom 设置密码
su tom                    # 切换到 tom（su = switch user）
su - root                 # 切换到 root（带 - 会加载环境变量）
whoami                    # 显示当前是谁
sudo 要单独讲：它是"临时用 root 身份执行某一条命令"，要求你当前账号在 sudo 组里（Ubuntu 安装时创建的用户默认就在）。好处是不用一直用 root，安全得多：
sudo apt update          # 以管理员身份执行 apt update
sudo vim /etc/hosts      # 以管理员身份改系统文件
**【提示】**$ 提示符下敲 sudo，会提示输入"你自己的密码"（不是 root 的密码），输入时不显示任何字符，正常输完回车即可。
### 5.6 Permission denied 排查套路
Permission denied（权限被拒绝）是最常见的报错之一。记住排查三步：先看权限，再想是谁缺了什么。举个最常见的例子：
$ ./run.sh
bash: ./run.sh: Permission denied
$ ls -l run.sh          # 第 1 步：看权限
-rw-r--r-- 1 root root 100 run.sh   # 没有 x！任何人都不能执行
$ chmod +x run.sh       # 第 2 步：加上执行权限
$ ./run.sh              # 第 3 步：再执行，成功
其他几种情况对照：
- 能读不能改 → 你不是属主也没有写权限 → 用 sudo 或 chown 换属主。
- 目录进不去 → 目录缺 x 权限 → chmod 755 目录。
- 服务起不来 → 日志目录属主不对，程序写不了日志 → chown 给对属主。
**【技巧】**遇到 Permission denied，第一反应永远是 ls -l 看权限，然后问自己："是哪个用户、缺哪个字母（r/w/x）"。
## 第6章　看系统看进程
### 6.1 ps：查看进程
进程（process）就是"正在运行的程序"。一个程序可以开很多进程。ps（process status）用来查看当前系统里的进程：
ps -ef    # 查看所有进程
ps aux    # 另一种风格，效果类似
ps -ef 输出的每一行是一个进程，主要字段：
- UID：这个进程是哪个用户启动的。
- PID：进程号，进程的唯一身份证，杀进程就靠它。
- PPID：父进程号，是谁生出来的它。
- CMD：启动这个进程的命令。
进程太多看不过来？用管道 + grep 过滤（第 7 章细讲）：
ps -ef | grep nginx    # 只看和 nginx 有关的进程
### 6.2 top / htop：实时监控
top 是"实时版 ps"，每秒刷新，能看到整个系统的负载情况：
top    # 进入实时监控界面
top 界面重点看这几块：
- 第一行 load average：系统负载，三个数字分别代表过去 1/5/15 分钟的平均负载，大致小于 CPU 核心数就算正常。
- 第三行 %CPU：us 是用户程序占的 CPU，sy 是系统占的，id 是空闲的。
- 进程列表：%CPU 和 %MEM 是每个进程吃掉的 CPU 和内存百分比。
top 里面的操作：按 q 退出，按 M 按内存排序，按 P 按 CPU 排序。htop 是 top 的加强版，彩色、可以鼠标操作，装一下更舒服：
sudo apt install htop    # 安装
htop                      # 运行
### 6.3 kill：结束进程
进程不听话了怎么办？先找到它的 PID，再 kill 它：
ps -ef | grep nginx    # 第 1 步：找到进程，记住 PID（第二列数字）
kill 12345              # 第 2 步：温和地结束 PID 为 12345 的进程
kill -9 12345           # 第 3 步（终极手段）：强制杀死
kill 是发"请停止"的请求，进程可以优雅地保存退出；kill -9 是直接"掐死"，进程来不及做任何事。
**【警告】**kill -9 慎用！数据库这类有状态的服务，被 -9 强杀可能损坏数据。先试普通 kill，实在不行再上 -9。
### 6.4 内存和磁盘：free、df、du
看内存：
free -h    # 人性化显示内存使用情况
# total 总内存，used 已用，free 空闲，available 真正可用
看磁盘：
df -h      # 每个分区的使用情况，Use% 一列满了就危险
du -sh /home    # 某个目录总共占了多少空间
du -sh /home/* | sort -rh | head -5   # 家目录下谁占得最多
**【重点】**df 看的是"整个硬盘分区"，du 看的是"某个目录"。df 显示 Use% 到 100% 时，就会报 No space left on device（第 15 章细讲）。
### 6.5 系统信息：uname、uptime、date
uname -a    # 内核版本、系统架构等信息
uptime      # 开机多久了、几个用户、负载
date        # 当前时间
这三条都是"一句话信息"，排查问题、写报告时经常用到。
## 第7章　文本三剑客
Linux 上的一切几乎都是文本：日志是文本、配置文件是文本、命令输出是文本。所以"处理文本"的能力决定你的效率。grep、sed、awk 被称为文本三剑客，加上管道和重定向，就是 Linux 老手的看家本领。
### 7.1 grep：按内容搜
grep 的作用：在文件（或一堆文本）里找出"包含指定关键字"的行。用法：grep [选项] 关键字 文件：
grep "error" app.log            # 找出所有包含 error 的行
grep -i error app.log           # -i 忽略大小写（Error、ERROR 都能匹配）
grep -v "#" /etc/ssh/sshd_config  # -v 反选：找出所有不含 # 的行（去掉注释）
grep -n "listen" nginx.conf     # -n 顺便显示行号
grep -r "TODO" /home/user/code/  # -r 递归搜索整个目录
grep 还支持正则表达式（用规则匹配文本）。先记三个最常用的符号：
- ^：行首。grep "^root" /etc/passwd 找以 root 开头的行。
- $：行尾。grep "false$" file 找以 false 结尾的行。
- .：任意一个字符。grep "a.c" 能匹配 abc、a1c。
**【提示】**正则记不住没关系，先把"搜关键字"用熟，用到再查。
### 7.2 sed：流式替换
sed 最常用的功能是"替换"。格式：sed 's/旧内容/新内容/g' 文件。看例子：
sed 's/8080/80/g' nginx.conf       # 把 8080 全部换成 80，结果打印到屏幕（不改原文件）
sed -i 's/8080/80/g' nginx.conf    # -i 直接改原文件（小心！）
sed -n '5,10p' app.log             # 只打印第 5 到 10 行
**【技巧】**不带 -i 的 sed 只是"打印预览"，不会动原文件。改重要配置文件前，先跑一遍不带 -i 的预览，确认没问题再加 -i。
**【警告】**sed -i 是危险操作，改之前最好先 cp 备份一份：cp nginx.conf nginx.conf.bak。
### 7.3 awk：按列处理
awk 擅长"按列"处理文本。默认以空格（连续空格也算）把一行拆成多列：$1 是第一列，$2 是第二列，$0 是整行。看例子：
awk '{print $1}' access.log        # 只打印第一列（通常是访问者的 IP）
awk -F: '{print $1}' /etc/passwd    # -F: 用冒号分割，取第一列（用户名）
awk '{print NR, $0}' file           # NR 是行号，打印"行号 + 整行"
awk '$3 > 100 {print $1, $3}' file  # 条件：第3列大于100才打印
经典组合拳：统计访问日志里访问量最高的前 10 个 IP：
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10
这条命令的意思是：取第一列（IP）→ 排序 → 去重并计数 → 按次数从大到小排 → 取前 10 行。这就是管道的力量，下面马上讲。
### 7.4 管道 | 与重定向 > >> 2>&1
管道（|）是 Linux 最迷人的设计。打个比方：它就像流水线，第一条命令的输出是"水"，通过 | 这根"水管"流进第二条命令当输入，第二条的输出再流给第三条……一级一级加工：
ps -ef | grep nginx          # 进程列表里过滤出 nginx
cat app.log | grep "404" | wc -l   # 统计日志里 404 出现了多少次
df -h | head -3                    # 磁盘信息只看前 3 行
重定向是把输出"写进文件"而不是"显示在屏幕"：
echo "hello" > a.txt     # > 把内容写进 a.txt（覆盖原内容）
echo "world" >> a.txt    # >> 追加到 a.txt 末尾
sh run.sh > out.log 2>&1  # 正常输出和错误都写进 out.log（2>&1 的意思）
sh run.sh 2>/dev/null     # 把错误信息丢进黑洞，只看正常输出
解释两个符号：2 代表"错误输出"，1 代表"正常输出"，> 是重定向。2>&1 就是把错误也塞进正常输出流，一起进文件。>/dev/null 是丢进黑洞。
**【重点】**管道和重定向是 shell 的两大神器。看到别人一行命令搞定你 10 步操作，多半就是用了它们。
练一练：用一条命令，统计 /var/log/syslog 里出现 "error" 的行数（提示：grep + wc，中间用 | 连接）。
## 第8章　压缩打包
### 8.1 为什么要压缩
三个理由：传输省流量（压缩包比原目录小得多）、备份省空间、把一堆文件"打包"成一个文件方便拷贝和上传。服务器之间传文件，压缩包是最靠谱的方式。
### 8.2 tar：打包 + 压缩一步到位
tar 是 Linux 最常用的打包工具。它先"打包"（把一堆文件合成一个），再"压缩"（把包变小）。完整命令：
tar -czvf backup.tar.gz /home/user/data    # 打包并压缩
tar -xzvf backup.tar.gz                     # 解压到当前目录
tar -xzvf backup.tar.gz -C /tmp             # 解压到指定目录 /tmp
tar -tzvf backup.tar.gz                     # 只看包里有啥，不解压
把参数拆开背：
- c：创建打包（create）。
- x：解包（extract）。
- z：用 gzip 压缩/解压。
- v：显示过程（verbose，看到文件列表）。
- f：后面跟文件名（file），必须放在最后。
习惯上压缩包后缀写成 .tar.gz 或 .tgz。
### 8.3 zip / unzip
如果你要和 Windows 同事互传文件，用 zip 更通用：
zip -r backup.zip /home/user/data    # -r 压缩整个目录
unzip backup.zip                        # 解压到当前目录
unzip backup.zip -d /tmp/out            # 解压到指定目录
**【提示】**记住口诀：打包压缩用 tar -czvf，解压用 tar -xzvf；和 Windows 打交道用 zip。
## 第9章　安装软件
### 9.1 三种安装方式
在 Linux 上装软件有三种方式，优先顺序是：
- 包管理器（推荐）：一行命令装好，自动处理依赖，升级卸载都方便。
- 源码编译：没有包、只能自己编译时才用，麻烦且容易踩坑。
- 直接解压：有些软件是"绿色版"，解压就能用。
先认准你系统的包管理器：Debian/Ubuntu 系用 apt，CentOS/Rocky 系用 yum 或 dnf。
### 9.2 apt：Ubuntu/Debian 系
最常用四条：
sudo apt update          # 更新软件列表（装新软件前先跑一次）
sudo apt install nginx   # 安装 nginx
sudo apt remove nginx    # 卸载 nginx
sudo apt search mysql    # 搜索软件
sudo apt upgrade         # 升级所有已安装的软件
国内服务器下载慢？换国内源（把软件下载地址换成阿里云/清华的镜像）。以 Ubuntu 为例：
# 第 1 步：备份原配置（好习惯）
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
# 第 2 步：把官方地址替换成阿里云镜像地址
sudo sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
sudo sed -i 's/security.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
# 第 3 步：重新更新，让新源生效
sudo apt update
**【提示】**不同发行版、不同版本的源文件内容不一样。最稳妥的办法：去"清华 TUNA 镜像站"或"阿里云镜像站"官网，找到你系统对应的整段配置，复制替换。
### 9.3 yum / dnf：CentOS/Rocky 系
sudo yum install -y nginx    # 安装（-y 表示自动回答 yes）
sudo yum remove nginx        # 卸载
sudo dnf install -y nginx    # dnf 是 yum 的新一代，命令一样
### 9.4 源码编译：./configure && make && make install
有些软件没有现成的包，只能自己编译。三步走：
wget https://example.com/soft.tar.gz   # 下载源码包
tar -xzvf soft.tar.gz                    # 解压
cd soft                                  # 进入源码目录
./configure --prefix=/usr/local/soft     # 第 1 步：检查环境、生成配置
make                                     # 第 2 步：编译成程序
sudo make install                        # 第 3 步：安装到系统
三步含义：configure 是"量体裁衣"，检查你的系统并生成配置；make 是"开工生产"，把源码编译成可执行程序；make install 是"搬进新家"，把编译好的程序放到系统目录。
**【提示】**编译需要装 gcc、make 等工具，还容易缺各种依赖库。除非包管理器里实在找不到，否则别折腾源码编译。
### 9.5 查软件装到哪了
which nginx        # 查 nginx 命令的路径
whereis nginx      # 查命令、源码、文档的位置
dpkg -l | grep nginx    # Debian 系：查已安装的软件包
rpm -qa | grep nginx    # RHEL 系：查已安装的软件包
## 第10章　vim
### 10.1 为什么必须学 vim
服务器上没有图形界面、没有鼠标，改配置文件只能靠命令行编辑器。vim 是所有 Linux 都自带的编辑器，学一次，走遍所有服务器都不怕。刚上手会觉得别扭，但就像骑自行车，学会就忘不掉。
### 10.2 三种模式
vim 和记事本最大的不同：它有三种"模式"，同一些按键在不同模式下含义完全不同。新手最容易懵的就是这个，先背下表：

| 模式 | 怎么进入 | 怎么退出 | 能干什么 |
| --- | --- | --- | --- |
| 普通模式 | 打开文件默认就在这 | （按 Esc 回到这里） | 按按键执行命令：复制、删除、跳转 |
| 插入模式 | 按 i 键 | 按 Esc | 像记事本一样打字 |
| 命令模式 | 按 :（冒号） | 按 Esc | 输入保存、退出、搜索、替换等命令 |

### 10.3 入门操作：先记住这三个就够了
vim /etc/hosts     # 打开文件（进入普通模式）
i                  # 按 i 进入插入模式，开始打字
Esc                # 打完按 Esc 回到普通模式
:wq                # 输入 :wq 保存并退出（w=write 保存，q=quit 退出）
如果改坏了不想保存：按 Esc 然后输入 :q! 强制不保存退出。新手最常问的还有：
:set nu        # 显示行号（改配置找位置神器）
u              # 撤销（后悔药）
dd             # 删除光标所在的那一行
yy             # 复制光标所在的那一行
p              # 粘贴到光标下面
/error         # 搜索 error，按 n 跳到下一个，N 跳上一个
:%s/8080/80/g  # 全文把 8080 替换成 80（和 sed 一个套路）
### 10.4 vim 常用按键速查表

| 按键 | 作用 |
| --- | --- |
| i | 进入插入模式（在光标前打字） |
| a | 进入插入模式（在光标后打字） |
| Esc | 回到普通模式 |
| :w | 只保存不退出 |
| :q | 退出（没保存会提示） |
| :wq | 保存并退出 |
| :q! | 不保存强制退出 |
| :set nu | 显示行号 |
| u | 撤销上一步 |
| dd | 删除光标所在行 |
| yy | 复制光标所在行 |
| p | 粘贴 |
| gg | 跳到文件第一行 |
| G | 跳到文件最后一行 |
| /关键字 | 搜索，n 下一个 |
| :%s/旧/新/g | 全文替换 |
| x | 删除光标处的字符 |
| v | 进入可视模式（配合方向键选中，y 复制，d 删除） |

**【技巧】**刚开始手会抖，就死记三个：i 进入、Esc 退出、:wq 保存。其他按键用到再查这张表。
## 第11章　Shell 脚本
### 11.1 什么是 Shell 脚本
如果你每天都要敲同样一串命令，为什么不把它们写进一个文件，一次执行？这个文件就叫 Shell 脚本。打个比方：脚本就是"菜谱"，把做菜的每一步写下来，照着做就能做出菜。脚本帮你把重复劳动自动化，这是"上班效率"的分水岭。
### 11.2 第一个脚本
用 vim 新建一个文件 hello.sh，写入下面内容：
#!/bin/bash
# 这是注释，以 # 开头，不执行
echo "大家好"
name="小明"
echo "你好, $name"
echo "第一个参数是: $1
逐行解释：
- #!/bin/bash：第一行固定写法，告诉系统"用 bash 这个解释器来执行本文件"。
- echo：把后面的文字打印出来。
- name="小明"：定义一个变量，等号两边不能有空格。
- $name：取变量的值。
- $1：脚本运行时传入的第一个参数。
执行脚本有两种方式：
bash hello.sh 张三    # 方式一：直接用 bash 执行（参数是"张三"）
chmod +x hello.sh      # 方式二：先加执行权限
./hello.sh 张三        # 再直接执行
### 11.3 判断：if
脚本要会"看情况办事"。if 的语法：if 条件; then 做A; else 做B; fi（fi 是 if 倒过来写，表示结束）：
#!/bin/bash
if [ -f /etc/hosts ]; then
  echo "文件存在"
else
  echo "文件不存在"
fi
常用条件写法：
- -f 文件：是文件吗？-d 目录：是目录吗？-e：存在吗？
- -gt 大于，-lt 小于，-eq 等于（比较数字）。
- = 相等，!= 不相等（比较字符串）。
一个实用例子：检查参数个数，不够就提示用法并退出：
#!/bin/bash
if [ $# -lt 1 ]; then
  echo "用法: $0 参数"
  exit 1
fi
echo "参数是: $1
这里 $# 是参数个数，$0 是脚本本身的名字，exit 1 是"带着错误码退出"。
### 11.4 循环：for 和 while
要重复做一件事，用 for：
for i in 1 2 3 4 5; do
  echo "第 $i 次"
done
# 更实用的：处理目录下所有 .log 文件
for f in *.log; do
  echo "处理 $f"
  tail -n 3 "$f"
done
不知道要循环几次时用 while：
count=1
while [ $count -le 5 ]; do
  echo "当前: $count"
  count=$((count + 1))
done
**【重点】**shell 的 for 语法是"for 变量 in 列表; do ...; done"，分号和 do/done 一个都不能少。
### 11.5 函数
把一段常用逻辑包成函数，起个名字，随时调用：
#!/bin/bash
say_hello() {
  echo "你好, $1"
}
say_hello "小明"
say_hello "小红"
# 输出：
# 你好, 小明
# 你好, 小红
函数里的 $1 是"传给函数的第一个参数"，和脚本的 $1 不是一回事。
### 11.6 crontab：定时任务（五段格式详解）
上班最常用的自动化：让系统定时执行你的脚本，比如每天凌晨备份。编辑定时任务：
crontab -e    # 编辑当前用户的定时任务（第一次会让你选编辑器）
每行一个任务，格式是：五段时间 + 要执行的命令。五段分别是：

| 位置 | 取值范围 | 含义 |
| --- | --- | --- |
| 第1段 | 0-59 | 分钟 |
| 第2段 | 0-23 | 小时 |
| 第3段 | 1-31 | 日期（几号） |
| 第4段 | 1-12 | 月份 |
| 第5段 | 0-7 | 星期（0 和 7 都代表周日） |

* 表示"任意"，*/5 表示"每 5 个单位"。看例子：
*/5 * * * * /root/check.sh          # 每 5 分钟执行一次
30 2 * * * /root/backup.sh            # 每天凌晨 2:30 执行
0 0 * * 1 /root/weekly.sh             # 每周一 0 点执行
0 3 1 * * /root/monthly.sh            # 每月 1 号 3 点执行
0 0 1 1 * /root/yearly.sh             # 每年 1 月 1 日执行
管理命令：
crontab -l    # 查看当前有哪些定时任务
crontab -r    # 清空所有定时任务（慎用）
**【技巧】**定时任务里的输出一定要重定向到文件，否则报错了你根本不知道：30 2 * * * /root/backup.sh >> /var/log/backup.log 2>&1
**【提示】**改完 crontab 立即生效，不用重启任何服务。
练一练：写一个脚本，把 /home 打包成 /backup/home_日期.tar.gz（提示：date +%Y%m%d 能拿到当天日期），然后用 crontab 让它每天凌晨 2 点跑。第 14 章有完整答案。
## 第12章　systemd
### 12.1 systemd 是什么
systemd 是现在几乎所有 Linux 都用的"服务大总管"。开机后它第一个跑起来，负责：把该启动的服务都启动、服务崩了帮它重启、记录每个服务的日志。所谓"服务"，就是一直运行的程序，比如 nginx（网页服务器）、mysql（数据库）、ssh（远程登录）。
### 12.2 systemctl：管理服务的命令
管理服务全靠 systemctl，格式：systemctl 动作 服务名。最常用的动作：

| 命令 | 作用 |
| --- | --- |
| systemctl start 服务 | 启动服务 |
| systemctl stop 服务 | 停止服务 |
| systemctl restart 服务 | 重启服务（改完配置最常用） |
| systemctl status 服务 | 查看运行状态和最近日志 |
| systemctl enable 服务 | 设为开机自启 |
| systemctl disable 服务 | 取消开机自启 |
| systemctl reload 服务 | 平滑重载配置（不中断服务） |
| systemctl list-units --type=service | 列出所有服务 |

看个例子：
systemctl status nginx     # nginx 现在什么状态？
systemctl restart nginx    # 改完配置，重启 nginx 生效
status 输出里，绿色 active (running) 表示运行中，红色 failed 表示挂了（这时候去看日志，见 12.4 节）。
### 12.3 开机自启：enable / disable
enable 不是"立即启动"，而是"开机时自动启动"。想要"现在启动 + 以后开机自启"一步到位，加 --now：
systemctl enable nginx        # 开机自启
systemctl enable --now nginx  # 开机自启 + 立即启动
systemctl disable nginx       # 取消开机自启
systemctl list-unit-files --type=service | grep enabled   # 看哪些服务开了自启
### 12.4 journalctl：看服务日志
服务出问题，第一反应就是看日志。journalctl（journal control）是 systemd 自带的日志查看器：
journalctl -u nginx                  # 看 nginx 这个服务的日志
journalctl -u nginx -n 50            # 只看最后 50 行
journalctl -u nginx -f               # 实时跟随（和 tail -f 一个感觉）
journalctl -u nginx --since "10 minutes ago"   # 看最近 10 分钟的
journalctl --vacuum-size=200M        # 清掉旧日志，腾出 200M 空间
**【重点】**记住这个习惯：服务起不来 → journalctl -u 服务名 -n 50 看日志，报错信息基本都在里面。
### 12.5 认识一下服务的配置文件
每个服务对应一个 .service 文件，放在 /etc/systemd/system/ 或 /lib/systemd/system/ 目录。里面关键的一行是 ExecStart=，写着"启动这个服务时执行什么命令"。知道在哪看就行，暂时不用会写：
cat /lib/systemd/system/nginx.service | grep ExecStart
## 第13章　网络
### 13.1 查看 IP：ip addr
ip addr    # 查看本机所有网卡的 IP 地址
输出里找 inet 开头的那行，后面跟的就是 IP 地址。127.0.0.1 是"本机自己"（回环地址），不是你的真实 IP；你要找的是 192.168.x.x（内网）或公网 IP。老命令 ifconfig 也有同样作用（需要装 net-tools）。
### 13.2 测连通：ping
ping -c 4 www.baidu.com    # 发 4 个包测试能不能连外网
能收到回复（有 time= 字样）说明网络通；一直 timeout 说明连不出去。ping 会一直发，用 -c 指定次数，或者 Ctrl+C 手动停。
### 13.3 查端口：ss / netstat
端口（port）是服务器上"服务的大门"，比如网页服务默认走 80 端口，SSH 走 22 端口。查谁在监听哪个端口：
ss -tlnp              # 查看所有监听中的 TCP 端口
ss -tlnp | grep :80   # 谁在监听 80 端口
netstat -tlnp         # 老命令，效果类似
lsof -i:8080          # 查 8080 端口被哪个进程占用（需安装 lsof）
参数拆解：t 只看 TCP，l 只看"正在监听"的（listen），n 用数字显示不解析域名，p 显示进程 PID 和名字。输出里重点看两列：Local Address（本地地址:端口）和 Process（进程）。
**【技巧】**"端口被占用""服务没起来"，第一反应就是 ss -tlnp | grep 端口号。
### 13.4 请求和下载：curl / wget
curl -I http://localhost:8080              # 只看响应头（网站通不通）
curl http://example.com/api/users        # 看返回内容
curl -X POST -d "name=test" http://example.com/api   # 发 POST 请求
wget https://example.com/file.tar.gz     # 下载文件
curl 是"发请求看结果"，调试接口必备；wget 是"下载文件"。
### 13.5 远程登录和传文件：ssh / scp
ssh root@192.168.1.10              # 登录服务器（默认 22 端口）
ssh -p 2222 user@192.168.1.10      # 指定端口登录
scp local.txt user@192.168.1.10:/tmp/    # 把本地文件上传到服务器
scp -r mydir user@192.168.1.10:/tmp/     # 上传整个目录
scp user@192.168.1.10:/tmp/remote.txt .  # 从服务器下载到当前目录
scp（secure copy）和 ssh 同一个套路：用户名@地址:路径。第一次连接会问你"确认主机指纹"，输入 yes 回车即可。
**【技巧】**传大量小文件很慢，先 tar 打包再传，速度快得多：tar -czvf - mydir | ssh user@IP "tar -xzvf - -C /tmp"。
### 13.6 网络排查的顺序
网站打不开，按这个顺序查：
ping 服务器IP           # ① 基础连通性：通不通？
ss -tlnp | grep :80     # ② 端口在听吗？服务起来了吗？
curl http://localhost   # ③ 本机自己访问自己，通不通？
# ④ 如果本机通、外面不通：查防火墙和安全组有没有放行端口
**【提示】**云服务器还要检查控制台的"安全组"——那是云平台层面的一道防火墙，忘了放行端口，外面永远连不上。
## 第14章　上班实战组合技
这一章把前面学的串起来，模拟四个上班最常见的场景。每个场景都是一套固定"打法"，学会了就能独立干活。
### 14.1 场景一：服务起不来，四步排查法
比如你重启了 nginx，结果网站挂了。别慌，按顺序走这四步：
# ① 看状态：服务到底什么状态？有没有报错？
systemctl status nginx
# ② 看日志：报错原因基本都在这里
journalctl -u nginx -n 50
# ③ 看端口：是不是端口被别的进程占了？
ss -tlnp | grep :80
# ④ 看权限：配置/日志目录属主对不对？配置语法对吗？
ls -l /etc/nginx /var/log/nginx
nginx -t
对应结论：① 状态是 failed，看具体报错；② 日志里一般写着"哪个文件第几行出了什么问题"；③ 端口被占就找到占用的进程处理（见 14.3）；④ 权限不对就 chown/chmod，配置语法不对就改配置。
**【重点】**记住口诀：状态 → 日志 → 端口 → 权限。四步走完，八成问题都能定位。
### 14.2 场景二：磁盘满了
现象：写文件报 No space left on device。处理流程：
df -h                          # ① 哪个分区满了？（看 Use% 一列）
du -sh /var/log/* | sort -rh | head -5   # ② 层层下钻，找占空间的大户
journalctl --vacuum-size=200M  # ③ 清 systemd 日志
: > /var/log/nginx/access.log  # ④ 清空日志文件内容（不删文件本身）
find / -xdev -type f -size +1G 2>/dev/null   # ⑤ 全盘找大于 1G 的文件
第 4 行解释：: > 文件 是"把文件内容清空"的写法，比直接 rm 再让程序重建更稳（程序不会因为文件被删而异常）。
**【警告】**删文件前一定先确认是什么文件。生产环境删错文件 = 事故，拿不准就先问。
### 14.3 场景三：端口被占用
现象：启动服务报"address already in use"（地址已被占用）。处理：
ss -tlnp | grep :8080   # ① 谁占用了 8080 端口？记下 PID
ps -ef | grep 12345     # ② 这个 PID 是什么程序？确认是不是能杀的
kill 12345              # ③ 确认无误后结束它
如果占用的程序是别人的服务，别乱杀——先沟通，或者干脆让你的服务换个端口。
### 14.4 场景四：写一个定时备份脚本（完整例子）
需求：每天凌晨 2 点备份 /home 和 /etc 两个目录，只保留最近 7 天的备份。完整脚本如下：
#!/bin/bash
# backup.sh —— 自动备份脚本
BACKUP_DIR=/backup
DATE=$(date +%Y%m%d_%H%M)
mkdir -p "$BACKUP_DIR"
# 打包压缩两个目录
tar -czf "$BACKUP_DIR/home_$DATE.tar.gz" /home
tar -czf "$BACKUP_DIR/etc_$DATE.tar.gz" /etc
# 删除 7 天以前的备份（-mtime +7 = 修改时间超过 7 天）
find "$BACKUP_DIR" -name "*.tar.gz" -mtime +7 -delete
# 写一条日志，方便以后查
echo "$(date) 备份完成" >> /var/log/backup.log
部署步骤：
vim /root/backup.sh            # ① 把上面内容写进文件
chmod +x /root/backup.sh        # ② 加执行权限
/root/backup.sh                 # ③ 先手动执行一次，确认能跑通！
ls -l /backup                   # ④ 检查备份文件生成了没
crontab -e                      # ⑤ 编辑定时任务，加这一行：
# 0 2 * * * /root/backup.sh >> /var/log/backup.log 2>&1
**【重点】**新写的定时任务，一定先手动执行一次确认没问题，再挂到 crontab 上。直接上 cron，失败了都不知道。
**【提示】**备份文件别和源数据放在同一个磁盘，否则磁盘坏了备份也没了。有条件就传到另一台机器或对象存储。
练一练：把 14.4 的备份脚本完整走一遍，再用第 7 章的知识，统计一下 /var/log/backup.log 里"备份完成"出现了多少次。
## 第15章　常见报错
报错不可怕，可怕的是不会看报错。这一章把新手最常见的报错整理成"现象 → 原因 → 解决"三段式，遇到问题直接对号入座。
### 15.1 command not found
$ nginx
bash: nginx: command not found
原因：系统里没有这个命令——要么没安装，要么拼写错了，要么命令不在搜索路径里。排查与解决：
which nginx            # 确认系统里到底有没有
sudo apt install nginx  # 没装就装一个
# 如果装了还在 /usr/local/bin 下，用绝对路径直接调用：
/usr/local/bin/nginx
### 15.2 Permission denied
$ ./run.sh
bash: ./run.sh: Permission denied
原因：当前用户对这个文件没有执行权限，或者文件不是你的。解决：
ls -l run.sh        # 看权限：有没有 x
chmod +x run.sh     # 没有就加上执行权限
# 如果是别人的文件且改不了，用 sudo 执行：
sudo ./run.sh
### 15.3 No space left on device
$ echo test > /var/log/a.log
bash: echo: write error: No space left on device
原因：磁盘满了（也可能是 inode 用完了）。解决流程：
df -h       # 看哪个分区 Use% 到 100%
df -i       # 顺便看 inode（小文件太多也会满）
du -sh /var/log/* | sort -rh | head   # 找大户
journalctl --vacuum-size=200M         # 清 systemd 日志
rm -rf /tmp/旧文件                     # 删确认过的无用文件
### 15.4 Connection refused
$ curl http://192.168.1.10:8080
curl: (7) Failed to connect ... Connection refused
原因：目标端口没人监听——服务没启动、端口写错、或者防火墙把端口挡了。按顺序查：
systemctl status nginx      # 服务起来了吗？
ss -tlnp | grep :8080       # 端口在听吗？
curl http://127.0.0.1:8080  # 本机自己访问呢？
# 本机通、外面不通 → 查防火墙 / 云安全组是否放行
### 15.5 其他高频小坑
坑一：在 Windows 上编辑的脚本拿到 Linux 运行，报 $'\r' 找不到命令（报错原文类似 $'\r': command not found）。原因是 Windows 的换行符和 Linux 不一样。解决：
sed -i 's/\r$//' script.sh   # 把行尾的 \r 删掉
# 或者装个工具一次搞定：
dos2unix script.sh
坑二：apt 报 lock 错误（E: Could not get lock /var/lib/dpkg/lock）。原因：另一个 apt 正在运行。解决：等它结束；确认没有 apt 在跑后，可以删掉锁文件（慎用）：
ps -ef | grep apt    # 确认没有其他 apt 在跑
sudo rm /var/lib/dpkg/lock   # 慎用！确认后再删
坑三：sudo: command not found。说明系统里没有 sudo 命令（某些精简系统），用 root 直接执行：
su - root            # 切到 root
apt install sudo     # 或直接装一个 sudo
**【技巧】**报错信息里 90% 都写着"原因"。养成习惯：把报错原文复制到搜索引擎（带上你的系统版本），先自己查 10 分钟。
## 附录A　命令速查总表
把全文出现的命令汇总成一张大表，上班时贴在手边随时查。格式：命令 | 作用 | 常用例子。
**文件与目录类：**

| 命令 | 作用 | 常用例子 |
| --- | --- | --- |
| pwd | 查看当前所在目录 | pwd |
| ls | 列出目录内容 | ls -lh /home |
| cd | 切换目录 | cd /etc |
| mkdir | 创建目录 | mkdir -p a/b/c |
| touch | 新建空文件或更新时间 | touch a.txt |
| cp | 复制文件或目录 | cp -r dir dir2 |
| mv | 移动或改名 | mv a.txt b.txt |
| rm | 删除文件或目录 | rm -rf /tmp/cache |
| cat | 查看小文件内容 | cat /etc/hosts |
| less | 翻页查看大文件 | less app.log |
| head | 查看文件开头 | head -n 5 file |
| tail | 查看文件结尾 | tail -f app.log |
| find | 查找文件 | find / -name "*.log" |
| grep | 在文件里搜索关键字 | grep error app.log |
| which | 查找命令的安装位置 | which python3 |
| file | 查看文件真实类型 | file a.txt |
| stat | 查看文件详细信息 | stat a.txt |
| tree | 以树形显示目录结构 | tree -L 2 /home |
| ln | 创建链接 | ln -s /opt/app /usr/local/app |

**权限与用户类：**

| 命令 | 作用 | 常用例子 |
| --- | --- | --- |
| chmod | 修改文件权限 | chmod 755 run.sh |
| chown | 修改文件属主/属组 | sudo chown user:group file |
| useradd | 新建用户 | sudo useradd tom |
| passwd | 设置/修改密码 | sudo passwd tom |
| su | 切换用户 | su - root |
| sudo | 用管理员权限执行 | sudo apt update |
| whoami | 显示当前用户名 | whoami |
| id | 显示当前用户信息 | id |

**进程与系统类：**

| 命令 | 作用 | 常用例子 |
| --- | --- | --- |
| ps | 查看进程 | ps -ef | grep nginx |
| top | 实时查看进程和负载 | top |
| htop | 更友好的进程监控 | htop |
| kill | 结束进程 | kill -9 12345 |
| killall | 按名字结束进程 | killall nginx |
| free | 查看内存使用 | free -h |
| df | 查看磁盘分区使用 | df -h |
| du | 查看目录占用大小 | du -sh /home |
| uname | 查看系统内核信息 | uname -a |
| uptime | 查看开机时长和负载 | uptime |
| date | 查看/设置时间 | date |
| lsblk | 查看磁盘和分区 | lsblk |

**文本处理类：**

| 命令 | 作用 | 常用例子 |
| --- | --- | --- |
| grep | 按内容搜索行 | grep -i error app.log |
| sed | 流式替换文本 | sed -i 's/旧/新/g' file |
| awk | 按列处理文本 | awk '{print $1}' file |
| sort | 排序 | sort -rn file |
| wc | 统计行数/字数 | wc -l file |
| uniq | 去重（配合 sort） | sort file | uniq -c |
| echo | 输出文字 | echo hello |

**压缩与软件类：**

| 命令 | 作用 | 常用例子 |
| --- | --- | --- |
| tar | 打包并压缩 | tar -czvf a.tar.gz dir |
| tar | 解压 | tar -xzvf a.tar.gz -C /tmp |
| zip | 压缩成 zip | zip -r a.zip dir |
| unzip | 解压 zip | unzip a.zip -d /tmp |
| apt install | 安装软件（Debian系） | sudo apt install nginx |
| apt update | 更新软件源列表 | sudo apt update |
| apt remove | 卸载软件 | sudo apt remove nginx |
| yum install | 安装软件（RHEL系） | sudo yum install -y nginx |

**编辑、任务与日志类：**

| 命令 | 作用 | 常用例子 |
| --- | --- | --- |
| vim | 命令行编辑器 | vim /etc/hosts |
| crontab -e | 编辑定时任务 | crontab -e |
| crontab -l | 查看定时任务 | crontab -l |
| systemctl | 管理服务 | systemctl status nginx |
| journalctl | 查看服务日志 | journalctl -u nginx -n 50 |
| history | 查看历史命令 | history |
| clear | 清屏 | clear |
| man | 查看命令手册 | man ls |
| nohup | 后台运行不中断 | nohup java -jar app.jar & |

**网络类：**

| 命令 | 作用 | 常用例子 |
| --- | --- | --- |
| ip addr | 查看 IP 地址 | ip addr |
| ping | 测试网络连通性 | ping -c 4 www.baidu.com |
| ss | 查看端口监听 | ss -tlnp |
| netstat | 查看端口监听（老命令） | netstat -tlnp |
| curl | 发送 HTTP 请求 | curl -I http://localhost:80 |
| wget | 下载文件 | wget http://x.com/f.tar.gz |
| ssh | 远程登录服务器 | ssh root@192.168.1.10 |
| scp | 远程复制文件 | scp a.txt user@IP:/tmp/ |

**【重点】**速查口诀：找文件用 find，搜内容用 grep，看日志用 tail -f，查进程用 ps，杀进程用 kill，查端口用 ss，服务问题用 systemctl + journalctl。
## 附录B　学习路线建议
### B.1 分阶段计划（8 周入门到上岗）

| 阶段 | 时间 | 学什么 | 检验标准 |
| --- | --- | --- | --- |
| 第1阶段 | 第1~2周 | 装环境（WSL2/虚拟机）+ 第3、4章 | 能在终端里自由地找文件、看文件、改文件 |
| 第2阶段 | 第3~4周 | 第5~8章：权限、进程、文本三剑客、压缩 | 能用 grep/awk 从日志里统计出想要的数据 |
| 第3阶段 | 第5~6周 | 第9~12章：装软件、vim、shell 脚本、crontab、systemd | 能独立写一个定时备份脚本并部署 |
| 第4阶段 | 第7~8周 | 第13~15章：网络、实战排查、常见报错 | 遇到服务起不来，能按四步法自己定位问题 |

每天坚持 30 分钟，比周末突击 5 小时效果好得多。
### B.2 学习方法建议
- 多敲：命令是肌肉记忆，只看不敲等于没学。每个代码块都亲手执行一遍。
- 记笔记：每天记 3 个新命令 + 1 个例子，一个月就有 90 条，远超日常所需。
- 先自己搜：遇到报错，把报错原文复制去搜（中文搜不到就搜英文），自己解决一次顶别人讲十次。
- 大胆折腾：装个虚拟机随便玩，弄坏了重装就行。很多高手都是"折腾"出来的。
- 刻意练习：把第 14 章的四个实战场景，每周完整走一遍，直到不看文档能独立完成。
### B.3 推荐资源
- 《鸟哥的 Linux 私房菜》：最经典的 Linux 中文入门书，网上有免费在线版，当字典用。
- 菜鸟教程（runoob.com）Linux 部分：入门命令速查，界面友好。
- Linux 命令大全（man.linuxde.net）：按分类查命令，上班救急神器。
- 牛客网、力扣的 Linux/Shell 练习题：刷题检验水平。
- 一台云服务器：有条件就买/领一台免费的，真刀真枪部署个网站，学习效果翻倍。
### B.4 最后的话
Linux 的学习曲线确实比 Windows 陡，前两周会觉得处处碰壁。但请相信：命令行世界是"一通百通"的——你学会的命令，在 Ubuntu、Rocky、Debian、macOS 终端里几乎都能用。等你熟练之后，会发现自己比用鼠标的人快十倍。
保持好奇，多敲多试，出了问题先看日志。祝你早日成为命令行高手！
**【提示】**本手册配套了完整的命令速查表（附录A）和实战案例（第14章），建议打印出来或者放在手边，边做边查。

## 相关笔记

- [[Docker使用技巧]]
- [[GitHub使用技巧大全]]
- [[网络运维知识大全]]
- [[程序员知识库]]
- [[Python与智能体零基础教程]]
