# GitHub使用技巧大全

> 科目：计算机与网络 ｜ 收录日期：2026-08-16 ｜ 原文：《GitHub使用技巧大全（小白版）.docx》

从注册账号到参与开源 · 零基础手把手中文教程
## 写在前面
你好！欢迎打开这本《GitHub 使用技巧大全（小白版）》。如果你完全没接触过 GitHub，看到英文网站就发怵，连“仓库”“分支”“提交”这些词都没听过，那这本书就是专门为你写的。我会用最土的大白话、最贴近生活的比喻，把每个概念讲明白，再给你能直接照抄的命令和操作步骤。
GitHub 是什么？一句话：它是全世界最大的“程序员代码网站”，相当于程序员的“代码仓库 + 朋友圈 + 简历”三合一。
- 代码仓库：把写好的代码存到网上，不怕电脑坏了丢代码，还能随时翻出任何一次历史版本。
- 朋友圈：关注大佬、看别人在写什么、给喜欢的项目点赞（GitHub 上叫 Star，相当于点个赞）。
- 简历：面试官打开你的 GitHub 主页，就能看到你写过什么项目、代码写得干不干净。很多公司招程序员，第一件事就是看 GitHub。
Git 和 GitHub 是什么关系？这是新手最容易搞混的两个词。记住一句话：Git 是一个工具（软件），装在你自己的电脑上，负责“管版本”；GitHub 是一个网站，负责“存代码 + 协作”。打个比方：Git 是相机，负责拍照记录每个瞬间；GitHub 是相册网站，你把照片传上去，别人能看、能点赞、还能和你一起整理。先有相机拍出照片，才能传相册——所以你得先在电脑上装好 Git，才能把代码传到 GitHub。
这本书怎么用？建议按顺序读：第 1 章从注册账号开始，第 2 到第 4 章是核心（建仓库、常用命令、分支协作），第 5 到第 9 章是美化与白嫖技巧，第 10 章教你用 GitHub 给求职加分，第 11 章是避坑指南，最后是三个附录速查表。每章的“命令”都放在灰色代码块里，你在电脑的 PowerShell 或 CMD（Windows）里一行一行输入即可；以 $ 开头的行表示“提示符”，$ 本身不用输入；<尖括号> 里的内容要换成你自己的，比如 <你的用户名> 要换成 zhang-san。
**【提示】**放心大胆地照做。GitHub 和 Git 的操作几乎不会弄坏你的电脑，最坏的结果也就是报个错。多敲、多错、多查，是学会 Git 和 GitHub 最快的路。
## 目录
- 第1章 从零开始：注册账号与安装 Git
- 第2章 第一个仓库：网页新建与第一次提交
- 第3章 常用 Git 命令精讲（含 30+ 速查表）
- 第4章 分支工作流：团队协作的核心
- 第5章 README 与文档美化（Markdown 速成）
- 第6章 Issues 与项目协作
- 第7章 GitHub Actions 自动化（进阶）
- 第8章 GitHub Pages 免费建站
- 第9章 搜索与发现（白嫖技巧）
- 第10章 参与开源与求职加分
- 第11章 常见坑与避坑指南
- 附录A Git 命令速查总表（40+ 条）
- 附录B GitHub 网页操作速查表（20+ 条）
- 附录C 提交信息规范与常用 emoji 表（20+ 条）
## 第1章 从零开始：注册账号
### 1.1 GitHub 到底是个啥（先建立感觉）
GitHub 是全世界最大的代码托管网站，几千万程序员都在上面。很多顶级项目——比如 Linux 操作系统、谷歌和微软的部分开源代码——都放在 GitHub 上。你可以把它理解成一个“云盘”，但它比云盘厉害得多：它不但帮你存代码，还帮你记录每一次改动、支持很多人同时协作，还自带社交功能。
对零基础的同学来说，你现在只需要记住三件事：第一，代码存上去不怕丢；第二，你的每一次提交（改动）都有记录，随时能翻旧账；第三，这个网站是你未来找工作的“门面”，好好经营它，收益很大。
### 1.2 注册账号（用户名/邮箱/头像/简介建议）
注册很简单：打开浏览器，访问 github.com，点右上角的 Sign up（注册），按提示填信息、收一封验证邮件点一下链接就完成了。下面是几个能让你的账号更“专业”的小建议：

| 项目 | 建议 | 为什么 |
| --- | --- | --- |
| 用户名 | 全英文、简短好记、和简历一致，如 zhang-san、lilei2024 | 别人好记、好搜，面试官搜得到你 |
| 邮箱 | 用常用邮箱，最好和简历上的邮箱一致 | 收验证邮件、找回密码、接收通知 |
| 头像 | 用本人照片或固定卡通头像 | 面试官会点开你的主页看 |
| 简介 Bio | 一句话介绍自己，如“大学生 · 喜欢 Python 和写博客” | 让人 3 秒知道你是谁、擅长什么 |

**【易错】**用户名注册后虽然可以改，但改一次全站链接都会变（别人收藏的你的链接会失效），所以起名要慎重：别用奇怪数字、别用中文、别用容易引起误会的词。
### 1.3 安装 Git（Windows 版）
Git 是必须装的工具，因为它负责在你电脑上“管版本”。Windows 用户这样装：
- 打开浏览器，访问官网 git-scm.com，点 Download for Windows 下载安装包。
- 双击安装包，一路点 Next（下一步），所有选项保持默认即可——小白不要乱改选项。
- 装完后，按 Win 键，搜索 PowerShell 或 CMD（命令行），打开它。
- 输入下面这条命令验证是否装好：
git --version
如果屏幕上出现类似 git version 2.4x.x.windows.1 的字样，就说明 Git 安装成功了。
**【易错】**装完 Git 之后，一定要把已经打开的命令行窗口全部关掉，再重新打开一个新的，新命令才会生效。
### 1.4 第一次配置（告诉 Git 你是谁）
Git 每次提交代码，都要记录“这次是谁改的”。所以第一次使用前，必须告诉 Git 你的名字和邮箱。打开命令行，输入下面两行（引号里换成你自己的信息）：
git config --global user.name "张三"
git config --global user.email "zhangsan@example.com"
这里的 --global 表示“对这台电脑上所有仓库生效”，配一次以后都不用再配。配完后可以用下面命令检查是否生效：
git config --global user.name
git config --global user.email
git config --list
**【技巧】**邮箱最好和你的 GitHub 注册邮箱保持一致。这样你提交的记录会自动关联到你的 GitHub 账号，头像也会显示在提交历史里，看起来特别专业。
### 1.5 配置 SSH 密钥（配一次，终身免密）
把代码推送到 GitHub 时，网站要确认“是不是你本人”。有两种认证方式：HTTPS（每次要输用户名和密码，现在还要输一串很长的 token）和 SSH（配一次密钥，以后永远免密）。强烈推荐 SSH。
SSH 密钥是个什么原理？打个比方：它是一把“钥匙（私钥）+ 一把锁（公钥）”的组合。你把锁（公钥）交给 GitHub，钥匙（私钥）永远留在你自己电脑里。之后每次操作，GitHub 一认锁就知道是你来了，不用再输密码。
第一步：打开命令行（Windows 推荐用 Git Bash，装 Git 时会自带），生成密钥：
ssh-keygen -t rsa -b 4096 -C "你的邮箱@example.com"
然后一路按回车（Enter）就行。如果它问你要不要设密码（passphrase），想更安全可以设一个，嫌麻烦就直接回车跳过。
第二步：查看公钥内容（公钥是给 GitHub 的那把“锁”，以 ssh-rsa 开头的一长串）：
cat ~/.ssh/id_rsa.pub
Windows 上想一键复制公钥，可以在 Git Bash 里执行：
clip < ~/.ssh/id_rsa.pub
第三步：把公钥添加到 GitHub。打开 GitHub 网页：右上角头像 → Settings（设置）→ 左侧 SSH and GPG keys → 点 New SSH key（新建 SSH 密钥）→ Title 随便填（比如“我的电脑”）→ 把刚才复制的公钥粘贴到 Key 框里 → 点 Add SSH key。
第四步：验证是否配置成功：
ssh -T git@github.com
如果看到 Hi 你的用户名! You have successfully authenticated（你好，验证成功）这样的提示，就大功告成了！
### 1.6 为什么要 SSH（免密、安全）
一句话总结：SSH 配一次，以后 push、pull 永远不用输密码；而且私钥从不离开你的电脑，比密码更安全。HTTPS 和 SSH 对比：

| 对比项 | HTTPS | SSH |
| --- | --- | --- |
| 每次操作 | 可能要输用户名 + 密码（或 token） | 配好后完全免密 |
| 安全性 | 较高（配合 token 使用） | 高（私钥不离开电脑） |
| 适合人群 | 偶尔用一下、图省事 | 长期使用、天天 push 的开发者（推荐） |
| 首次配置 | 基本不用配 | 需要生成一次密钥（5 分钟） |

**【重点】**私钥文件（id_rsa）绝对不要发给任何人、不要传到 GitHub 或任何网上！它就是你家的钥匙。公钥（id_rsa.pub）可以随便给人。
## 第2章 第一个仓库
### 2.1 在网页上新建仓库
“仓库”（Repository，简称 repo）就是 GitHub 上装你代码的那个文件夹。新建方法：登录 GitHub → 右上角 + 号 → New repository（新建仓库）。
填表时注意几个关键选项：
- Repository name（仓库名）：全英文，别用中文、别带空格，单词之间用短横线 - 连接，比如 my-first-project。
- Description（描述）：一句话说明这个项目是干什么的，可选但建议填。
- Public（公开）还是 Private（私有）：这是新手第一个重要选择。

| 选项 | 含义 | 适合场景 |
| --- | --- | --- |
| Public 公开 | 任何人都能看你的代码 | 想开源、想给简历加分、想让别人 Star |
| Private 私有 | 只有你和你邀请的人能看 | 练习、隐私项目、公司内部代码 |

- Add a README file（添加说明文件）：勾选它，GitHub 会自动帮你生成一个 README.md 说明文件。新手强烈建议勾上，省得后面手动建。
最后点绿色的 Create repository（创建仓库），网页上的仓库就建好了。
### 2.2 本地关联仓库的三种方式
仓库建在网页上还不够，你得把它和你电脑上的文件夹“关联”起来。根据你的情况，三选一：

| 方式 | 命令 | 适合场景 |
| --- | --- | --- |
| 一、全新开始 | git init | 本地从零开始，还没有任何代码 |
| 二、克隆别人的 | git clone <仓库地址> | 把 GitHub 上现成的仓库整个复制到本地 |
| 三、关联已有项目 | git remote add origin <仓库地址> | 本地已经有一个项目，想传到 GitHub |

# 方式一：在项目文件夹里初始化
git init
# 方式二：把 GitHub 上的仓库复制到本地
git clone https://github.com/你的用户名/my-first-project.git
# 方式三：本地已有项目，关联到远程仓库
git remote add origin https://github.com/你的用户名/my-first-project.git
关联完可以用 git remote -v 查看关联的远程地址，确认没问题。
### 2.3 第一次提交五步走（全流程演示）
现在是最激动人心的一步：把代码提交到 GitHub。整个过程就像“寄快递”，一共五步，每一步都有生活比喻，你照着敲一遍就懂了：

| 步骤 | 命令 | 生活比喻 |
| --- | --- | --- |
| 1. 看看状态 | git status | 照镜子：看看自己有什么改动 |
| 2. 加入暂存区 | git add . | 把要寄的东西装进快递盒（暂存区） |
| 3. 提交 | git commit -m "说明" | 封箱贴单：生成一个版本快照 |
| 4. 推送 | git push -u origin main | 快递寄出：上传到 GitHub |
| 5. 拉取 | git pull | 收快递：把云端的新东西下载到本地 |

在项目文件夹里打开命令行，依次执行（带 # 的是注释，不用敲）：
# 第 1 步：看看当前状态
git status
# 第 2 步：把所有文件加入暂存区（. 表示“全部”）
git add .
# 第 3 步：提交，生成一个版本（引号里写这次改了什么）
git commit -m "我的第一次提交"
# 第 4 步：推送到 GitHub（-u 是第一次推送时告诉 Git 记住目标）
git push -u origin main
# 第 5 步：以后想同步云端的最新代码，随时执行
git pull
逐条解释：git status 会告诉你哪些文件是新的、哪些改过了；git add 是把文件放进“暂存区”（相当于购物车）；git commit 是正式生成一个版本记录；git push 是把本地版本上传到 GitHub；git pull 是把 GitHub 上别人（或你其他电脑）的新提交下载到本地。第 4 步第一次执行时，如果弹出浏览器或要求输入用户名密码，按提示完成授权即可。
**【提示】**第一次 push 后，刷新 GitHub 仓库页面，看到你的文件出现在网页上，恭喜你——你已经完成了一次完整的“本地 → 云端”流程！
## 第3章 常用 Git 命令精讲
这一章把最常用的 Git 命令挨个讲透，每个都给例子。学完这章，你就能独立管理自己的代码了。
### 3.1 add 和 commit：拍照两步走
add 是把文件放进“暂存区”，commit 是“拍照”生成一个版本。注意：add 可以分多次，commit 一次可以打包多个文件。
# 添加单个文件
git add index.html
# 添加全部文件（. 表示当前目录下所有文件）
git add .
# 提交并写说明
git commit -m "feat: 新增登录页面"
提交信息（commit message）非常重要，它像“照片的备注”。GitHub 社区有一套约定俗成的写法：用英文前缀说明这次改动的类型，后面跟中文或英文说明。最常见的前缀：

| 前缀 | 含义 | 例子 |
| --- | --- | --- |
| feat: | 新功能 | feat: 新增登录页面 |
| fix: | 修复 bug | fix: 修复按钮点击无反应 |
| docs: | 文档相关 | docs: 更新使用说明 |
| style: | 格式、样式 | style: 调整代码缩进 |
| refactor: | 重构（不改功能） | refactor: 拆分 login 函数 |
| test: | 测试相关 | test: 新增登录测试用例 |
| chore: | 杂务（依赖、配置等） | chore: 更新依赖版本 |

**【易错】**提交信息千万别写 “update”“111”“aaa” 这种没意义的话。面试官和未来的你都会看提交历史，写清楚“做了什么”是专业的第一表现。
### 3.2 status 和 log：查看状态和历史
# 查看当前状态（哪些文件改了、哪些没提交）
git status
# 查看提交历史（完整版）
git log
# 查看提交历史（简洁版，一行一条，最常用）
git log --oneline
git status 会显示文件三种状态：未跟踪（untracked，新文件，Git 还不认识它）、已修改（modified，改过了还没 add）、已暂存（staged，已经 add 还没 commit）。git log --oneline 输出形如 a1b2c3d feat: 新增登录页面，前面那串乱码是提交编号（commit hash），后面是提交说明。
### 3.3 push 和 pull：本地和云端同步
push 是“上传”，pull 是“下载”。-u 参数只在第一次推送时用，作用是让 Git 记住“这个分支对应远程的哪个分支”，以后直接敲 git push 就行。
# 第一次推送：-u 表示记住关联关系
git push -u origin main
# 以后直接推送
git push
# 拉取云端更新（别人推的新代码）
git pull
### 3.4 branch 和 checkout：分支（岔路）
分支（branch）可以理解成“修路时的施工便道”：主路（main 分支）保持通畅，你在旁边开一条便道干活，干好了再并回主路，互不耽误。
# 查看当前有哪些分支（* 号表示当前所在分支）
git branch
# 创建新分支 dev
git branch dev
# 切换到 dev 分支
git checkout dev
# 创建并切换（一步到位，最常用）
git checkout -b dev
新版本 Git 也支持更直观的 git switch 命令：git switch dev 切换分支，git switch -c dev 创建并切换。效果和 checkout 一样。
### 3.5 merge：合并分支（含冲突解决）
在便道上干完活，要把改动并回主路。做法：先切回要接收改动的主分支，再 merge 那个功能分支。
# 先切回 main 分支
git checkout main
# 把 dev 分支合并进 main
git merge dev
如果两个人改了同一个文件的同一处地方，Git 会“打架”，这叫冲突（conflict）。别慌，Git 会告诉你哪些文件冲突了，文件里会出现这样的标记：
<<<<<<< HEAD
这是 main 分支上的内容
=======
这是 dev 分支上的内容
>>>>>>> dev
冲突解决三步走：第一步，打开文件，把 <<<<<<<、=======、>>>>>>> 这三行标记删掉，只保留你想留下的内容（也可以两个都要）；第二步，git add 那个文件；第三步，git commit 提交，冲突就解决了。
**【技巧】**冲突不是错误，是 Git 在保护你的代码——它宁可停下来问你，也不擅自覆盖任何人的劳动。解决一次冲突，你对 Git 的理解就上一个台阶。
### 3.6 stash：临时把改动收起来
场景：你正在改代码改到一半，突然老板让你先修另一个紧急 bug，但你不想把改到一半的东西提交。这时用 stash 把改动“收进抽屉”，干完别的再拿出来。
# 把未提交的改动收起来
git stash
# 查看收起来的东西
git stash list
# 把改动拿出来（恢复）
git stash pop
### 3.7 tag：打标签（版本号）
项目做到一个重要节点（比如发布 v1.0），可以打一个标签，相当于给某个提交贴个“里程碑”贴纸，以后想找随时能找到。
# 给当前提交打标签
git tag v1.0.0
# 查看所有标签
git tag
# 把标签推送到 GitHub
git push origin v1.0.0
### 3.8 revert 和 reset：两种“后悔药”
改错了想撤销，有两条路：revert 是“做一个反向操作把错误抵消”（历史完整保留，安全）；reset 是“时光倒流回到过去”（历史被改写，危险）。
# revert：生成一个反向提交（推荐，安全）
git revert a1b2c3d
# reset：回到上一个版本，改动也丢掉（危险！只用于本地没推送的提交）
git reset --hard HEAD~1
# reset：回到上一个版本，但保留改动内容
git reset --soft HEAD~1

| 对比项 | revert（反向提交） | reset（时光倒流） |
| --- | --- | --- |
| 原理 | 新增一个提交，把之前的改动抵消 | 把分支指针移回旧版本 |
| 历史记录 | 完整保留，能看到“改错了又改回来” | 历史被删除，好像从没发生过 |
| 安全性 | 安全，团队协作推荐 | 危险，可能丢掉别人的提交 |
| 适合场景 | 已经推送到 GitHub 的提交 | 本地还没推送的提交 |

**【重点】**原则：已经 push 到 GitHub 的提交，用 revert；只在本地、还没 push 的提交，才考虑用 reset。千万不要对已经推送到团队共享分支的提交用 reset --hard，会害了所有人。
### 3.9 常用命令速查表（30 条+）

| 命令 | 作用 | 例子 |
| --- | --- | --- |
| git init | 初始化仓库 | git init |
| git clone <地址> | 克隆远程仓库 | git clone https://github.com/xxx/yyy.git |
| git status | 查看状态 | git status |
| git add <文件> | 加入暂存区 | git add . |
| git add -A | 全部加入（含删除） | git add -A |
| git commit -m "信息" | 提交 | git commit -m "feat: 新增登录" |
| git commit -am "信息" | add + commit 一步到位 | git commit -am "fix: 改标题" |
| git log | 查看提交历史 | git log |
| git log --oneline | 简洁历史 | git log --oneline |
| git log --oneline --graph | 图形化历史 | git log --oneline --graph |
| git diff | 查看未暂存的改动 | git diff |
| git diff --staged | 查看暂存区改动 | git diff --staged |
| git push | 推送本地提交 | git push |
| git push -u origin main | 首次推送并记住关联 | git push -u origin main |
| git pull | 拉取并合并远端更新 | git pull |
| git fetch | 只拉取不合并 | git fetch |
| git branch | 查看分支 | git branch |
| git branch <名> | 创建分支 | git branch dev |
| git branch -a | 查看所有分支（含远端） | git branch -a |
| git branch -d <名> | 删除分支 | git branch -d dev |
| git checkout <分支> | 切换分支 | git checkout dev |
| git checkout -b <名> | 创建并切换分支 | git checkout -b feature-x |
| git switch <分支> | 切换分支（新版） | git switch dev |
| git switch -c <名> | 创建并切换（新版） | git switch -c feature-y |
| git merge <分支> | 合并分支 | git merge dev |
| git stash | 暂存未提交的改动 | git stash |
| git stash pop | 恢复暂存的改动 | git stash pop |
| git stash list | 查看暂存列表 | git stash list |
| git tag <名> | 打标签 | git tag v1.0.0 |
| git push origin <标签> | 推送标签 | git push origin v1.0.0 |
| git revert <编号> | 反向提交（安全撤销） | git revert a1b2c3d |
| git reset --soft HEAD~1 | 撤销提交但保留改动 | git reset --soft HEAD~1 |
| git reset --hard HEAD~1 | 撤销提交并丢弃改动（危险） | git reset --hard HEAD~1 |
| git reflog | 查看所有操作记录 | git reflog |
| git remote -v | 查看远程地址 | git remote -v |
| git remote add origin <地址> | 添加远程仓库 | git remote add origin https://github.com/xxx/yyy.git |
| git config --list | 查看所有配置 | git config --list |
| git rm <文件> | 删除文件 | git rm old.txt |
| git mv <旧名> <新名> | 重命名文件 | git mv a.txt b.txt |
| git show <编号> | 查看某次提交详情 | git show a1b2c3d |

**【技巧】**命令记不住很正常，高手也是边查边用。Git 自带帮助：git help <命令> 或 git <命令> --help，随时可以查。
## 第4章 分支工作流（团队协作核心）
### 4.1 为什么用分支
想象一条主干道：大家都靠它通行，要是谁都能随便在主干道上挖坑、施工，整条路就瘫痪了。Git 的分支就是“施工便道”：想改东西，先在旁边开一条便道（分支）慢慢干，干完验收合格，再并回主干道。这样主干道（main 分支）永远稳定，谁都能放心用。
一个人写代码时分支可有可无；但一旦多人协作，分支就是保命技能——没有分支，你改一半的代码可能直接毁掉别人正在用的版本。
### 4.2 经典工作流：Git Flow 简化版
Git 社区流传最广的一套分支规范叫 Git Flow，小白先掌握简化版就够了，就三个角色：

| 分支 | 用途 | 谁在上面干活 |
| --- | --- | --- |
| main | 正式稳定版，只放能发布的代码 | 所有人都在用，轻易不动 |
| dev | 开发版，日常开发都合到这里 | 整个开发团队 |
| feature/xxx | 单个功能的分支 | 每个开发者自己 |

典型流程：从 dev 拉一个 feature 分支 → 在上面开发新功能 → 完成合回 dev → dev 测试稳定后 → 合回 main 发正式版。
### 4.3 Pull Request（PR）完整流程
PR（拉取请求）是 GitHub 上“申请把我的改动合进你的仓库”的正式流程。它是开源协作的心脏，也是面试必问。完整流程八步走：
- 第 1 步 fork：在别人项目页右上角点 Fork，把仓库“复印”一份到你自己账号下（比喻：复印一本别人的书，在复印件上写写画画）。
- 第 2 步 clone：把你 fork 的仓库克隆到本地。
git clone https://github.com/你的用户名/项目名.git
- 第 3 步 建分支：为你的改动开一个分支（好习惯）。
git checkout -b fix-login-bug
- 第 4 步 改代码：修改、add、commit，正常提交。
git add .
git commit -m "fix: 修复登录 bug"
- 第 5 步 push：把分支推到你自己 fork 的仓库。
git push -u origin fix-login-bug
- 第 6 步 发 PR：回到 GitHub，你的 fork 页面会出现一个 Compare & pull request 按钮，点它 → 确认“从你的分支 → 到原项目分支”→ 写清楚改了什么、为什么改 → 点 Create pull request。
- 第 7 步 review：项目维护者（或团队同事）审查你的代码，可能提出修改意见，你们在 PR 评论区讨论；要改就继续在本地改、提交、push，PR 会自动更新。
- 第 8 步 merge：审查通过后，维护者点 Merge pull request，你的改动正式合并进原项目。
**【重点】**PR 的完整流程是“fork → clone → 建分支 → 改代码 → push → 发 PR → review → merge”。面试官问“你参与过开源吗”，讲清这 8 步就够了。
### 4.4 review 是什么
review（代码审查）就是“互相检查代码”，像写作文让同桌帮忙改错别字。好处有三个：提前发现 bug（代码刚写完时最容易发现问题）、互相学习（看到别人的好写法）、保证质量（至少两个人看过，不容易出错）。在 GitHub 上，审查者在 PR 的 Files changed（文件变更）页面里对每一行代码发表评论，最后点 Review changes → Approve（通过）或 Request changes（请修改）。
### 4.5 三种合并方式区别
合并 PR 时，GitHub 会问你用哪种方式合并，小白先记住一句话版：

| 合并方式 | 提交历史 | 一句话特点 | 适合 |
| --- | --- | --- | --- |
| Merge commit | 完整保留所有提交 | 最真实，能看到每一步 | 新手、团队协作 |
| Squash and merge | 压成一个提交 | 历史最干净，像“汇总成一个总结” | 一个功能有多次琐碎提交时 |
| Rebase and merge | 线性排列 | 历史像一条直线，最整洁 | 高级用户、追求极简历史 |

**【提示】**拿不准就选 Merge commit，它最安全、信息最全，永远不会错。
## 第5章 README 与文档美化
### 5.1 README 是什么
README 是每个仓库的“门面”，也就是别人点进你仓库第一眼看到的说明文件（通常叫 README.md）。它回答三个问题：这个项目是干什么的？怎么安装？怎么用？一个写得好的 README，能让人 30 秒决定要不要用你的项目、要不要给你 Star。写不好的 README，就算代码再好也没人看。
### 5.2 Markdown 语法速成
README.md 的 .md 是 Markdown 格式——一种“用简单符号排版”的纯文本格式，GitHub 会自动把它渲染成漂亮的网页。速成表：

| 功能 | 写法 | 效果 |
| --- | --- | --- |
| 一级标题 | # 标题 | 大标题 |
| 二级标题 | ## 标题 | 中标题 |
| 加粗 | **重要文字** | 重要文字（加粗） |
| 斜体 | *强调* | 强调（斜体） |
| 无序列表 | - 第一项 | • 第一项 |
| 有序列表 | 1. 第一项 | 1. 第一项 |
| 链接 | [文字](https://网址) | 可点击的文字 |
| 图片 | ![说明](图片地址) | 显示图片 |
| 代码块 | ``` 代码 ``` | 灰色代码块 |
| 行内代码 | `代码` | 代码（行内） |
| 表格 | | 列1 | 列2 | | 表格 |
| 引用 | > 引用的内容 | 引用样式 |
| 分隔线 | --- | 一条横线 |

来一段完整的例子，感受一下（这本身就是 Markdown 源码）：
# 我的第一个项目
## 简介
这是一个**超好用**的 Python 工具。
## 功能
- 功能一：自动整理文件
- 功能二：一键生成报告
## 安装
```bash
pip install mytool
```
## 使用
```python
import mytool
mytool.run()
```
## 更多
去 [我的博客](https://example.com) 看看。
### 5.3 一个好 README 的模板
直接复制下面这个模板，把内容换成你自己的，就是一个合格的项目门面：
# 项目名称
> 一句话介绍这个项目是干什么的
![项目截图](screenshots/demo.png)
## ✨ 功能特点
- 特点一：……
- 特点二：……
## 📦 安装
```bash
pip install 你的包名
```
## 🚀 使用
```python
import 你的包
你的包.run()
```
## 🤝 贡献
欢迎提 Issue 和 Pull Request！请看 [贡献指南](CONTRIBUTING.md)。
## 📄 许可证
本项目使用 MIT 许可证。
**【技巧】**README 里至少要有：项目名 + 一句话简介 + 安装方法 + 使用方法。截图非常加分——人们是视觉动物，一张效果图胜过十段文字。
### 5.4 GitHub 个人主页 README 技巧
想让你自己的 GitHub 主页（用户名.github.io 那个页面）显示一段自我介绍？秘诀：新建一个和你的用户名“完全同名”的仓库（比如你的用户名是 zhang-san，就建一个叫 zhang-san 的仓库），在里面放一个 README.md，它就会自动显示在你的主页顶部。
主页 README 可以放：自我介绍、技术栈（会的语言和工具）、联系方式、甚至动态统计卡片。比如放一行：
![GitHub 统计](https://github-readme-stats.vercel.app/api?username=你的用户名)
这一行会自动渲染成一张带绿格子和数字的统计图，显得你 GitHub 玩得很专业。
### 5.5 License 是什么
License（许可证）就是“版权声明”：告诉别人“我的代码你能不能用、怎么用”。没有 License 的代码默认“版权所有，禁止使用”。三种最常见的：

| 许可证 | 一句话 | 适合 |
| --- | --- | --- |
| MIT | 随便用，标注来源即可（最宽松） | 绝大多数项目（小白首选） |
| Apache 2.0 | 随便用，需保留声明，含专利条款 | 大公司、重视专利的项目 |
| GPL | 用了我的代码，你的代码也必须开源 | 希望代码永远开源的理想主义项目 |

**【提示】**不知道选什么就选 MIT，它最宽松、最流行，GitHub 一键就能添加（仓库页面点 Add file → Create new file，命名为 LICENSE）。
## 第6章 Issues 与项目协作
### 6.1 Issues 是什么
Issue（问题单）就是仓库的“意见箱”：任何人发现 bug、想要新功能、有问题要问，都可以开一个 Issue。每个 Issue 有编号（#1、#2…），大家可以评论讨论，解决后关闭。对开源项目来说，Issues 就是它的“客户服务系统 + 需求收集箱”。
### 6.2 怎么写一个好 Issue
一个好的 Issue 要让维护者不用追问就能复现你的问题。标准模板：
标题：一句话说清楚问题（比如：登录页面点击按钮报 500 错误）
环境：
- 系统：Windows 11
- 软件版本：Python 3.13 / 项目 v1.2.0
复现步骤：
1. 打开登录页面
2. 输入账号密码
3. 点击登录按钮
期望结果：应该成功登录并跳转主页
实际结果：页面报 500 错误，控制台显示 xxx
截图：附上截图或报错信息

| 坏标题 | 问题在哪 | 好标题 |
| --- | --- | --- |
| 救命！报错了 | 没说清什么错、在哪错 | 登录时点击按钮报 500 错误 |
| 怎么安装？ | 太宽泛，没说环境和操作 | Windows 下 pip 安装依赖报编码错误 |
| 建议加个功能 | 没说要什么功能 | 建议支持导出 CSV 格式的报表 |

### 6.3 Issue 模板与标签
仓库可以设置“Issue 模板”，让提 Issue 的人自动按格式填写（仓库 Settings → General → Set up templates）。常用标签（Label）：

| 标签 | 含义 | 谁会用 |
| --- | --- | --- |
| bug | 程序出错了 | 用户/开发者 |
| enhancement | 想要新功能 | 用户 |
| good first issue | 适合新手的任务（新手福音） | 维护者 |
| help wanted | 需要志愿者帮忙 | 维护者 |
| documentation | 文档相关 | 任何人 |
| question | 提问 | 用户 |

### 6.4 Projects 看板
Projects（项目看板）一句话：它像办公室墙上的便利贴看板，把 Issue 拖到 To do（待办）、In progress（进行中）、Done（完成）三列里，一眼看清项目进度。团队用它管理任务，个人也可以用它管理自己的学习计划。
### 6.5 在开源项目里提 Issue 的礼貌规范
- 先搜索：提之前先搜一搜，是不是已经有人提过同样的问题（别重复打扰维护者）。
- 用英语：绝大多数国际开源项目用英语交流，实在不行用翻译工具也要翻成英文。
- 说清楚：版本、环境、复现步骤、截图，一样都别少。
- 别催、别骂：维护者也是志愿者，没有义务秒回你；催更和抱怨只会让人讨厌。
- 先感谢：问题解决后，回一句 Thanks 或关闭 Issue，社区会记住你的礼貌。
**【技巧】**礼貌是开源社区的第一张名片。一个写得好、有礼貌的 Issue，可能直接让维护者对你印象深刻——这是很多人参与开源的第一步。
## 第7章 GitHub Actions 自动化（进阶）
### 7.1 Actions 是什么
Actions 是 GitHub 内置的“自动化机器人”：你可以规定“当某件事发生时，机器人自动做某件事”。最常见的用法是 CI（持续集成）：每次有人 push 代码，机器人自动把代码拉下来、跑一遍测试，有问题立刻报警。你不用自己买服务器，GitHub 免费给你提供运行环境（公共仓库免费额度非常充足）。
打个比方：你雇了一个不用发工资的实习生，规矩是“只要有人交新代码，你就立刻跑一遍所有测试，并把结果贴在公告栏”。这个实习生就是 Actions。
### 7.2 一个最简单的 workflow（完整示例 + 逐行注释）
在仓库里新建一个文件：.github/workflows/ci.yml（注意是隐藏文件夹 .github，workflows 是固定名字）。内容如下，每行都有中文注释：
name: CI              # 工作流名字，随便起，会显示在 Actions 标签页
on:                   # “什么时候触发”
  push:               # 当有人 push（推送）代码时
    branches: [ main ]  # 只监听 main 分支的推送
jobs:                 # “要干哪些活”（可以有多个 job）
  test:               # 这个活叫 test
    runs-on: ubuntu-latest   # 在 Ubuntu 虚拟机上运行（免费的云电脑）
    steps:            # 一步步往下做
      - name: 拉取代码
        uses: actions/checkout@v4   # 用官方提供的“拉代码”工具
      - name: 安装 Python
        uses: actions/setup-python@v5
        with:               # 给上面这个工具传参数
          python-version: "3.13"   # 指定 Python 版本
      - name: 安装依赖
        run: pip install pytest    # run = 在虚拟机上执行命令
      - name: 跑测试
        run: pytest                # 跑测试，失败则整个工作流报红
把这个文件 commit 并 push 到 GitHub 后，打开仓库的 Actions 标签页，就能看到机器人开始干活；跑完会显示绿色的对勾（成功）或红色的叉（失败）。以后每次 push 代码，它都会自动跑一遍。
### 7.3 常见用途表

| 用途 | 触发时机 | 例子 |
| --- | --- | --- |
| CI 自动测试 | 每次 push | 自动跑 pytest，报错就提醒 |
| 自动发 Release | 打 tag 时 | 自动打包、生成安装文件并发布 |
| 定时任务 | 按 cron 定时 | 每天早上自动抓取数据 |
| 部署 Pages/服务器 | push 到 main | 自动把网站部署上线 |
| 自动处理 Issue | 新 Issue 创建时 | 自动打上 bug 标签 |

**【提示】**想白嫖更多现成“机器人零件”，去 GitHub 搜 Actions 市场（Marketplace），里面有成千上万现成的步骤可以直接用，不用自己写。
## 第8章 GitHub Pages 免费建站
### 8.1 Pages 是什么
GitHub Pages 是 GitHub 免费送你的“网站空间”：把你的网页文件放在仓库里，GitHub 帮你托管，别人就能通过网址访问。适合放个人主页、项目文档、博客。域名格式：你的用户名.github.io/仓库名。不用买服务器、不用备案，完全免费。
### 8.2 三步开启
- 第一步：打开仓库 → 点顶部的 Settings（设置）。
- 第二步：左侧菜单往下找 Pages（在 General 下面）。
- 第三步：在 Source（来源）那里选 Deploy from a branch（从分支部署）→ Branch 选 main → 目录选 / (root) → 点 Save（保存）。
等一两分钟，访问 你的用户名.github.io/仓库名，就能看到你的网站了。
**【易错】**如果你的仓库名刚好叫 用户名.github.io（比如 zhang-san.github.io），那网址就直接是 用户名.github.io，不用带仓库名。
### 8.3 用 Jekyll / Hexo 建个人博客
Pages 原生支持 Jekyll（一个把 Markdown 文档变成网页的工具），你把文章写成 Markdown 文件 push 上去，Jekyll 自动渲染成漂亮的博客页面。国内更流行的是 Hexo——一个博客框架，写好文章后生成静态网页再推到 Pages。一句话：Jekyll 和 Hexo 都是“把你写的 Markdown 文章变成网页”的工具，选哪个都行，小白可以先从 Jekyll 上手（GitHub 原生支持，零配置）。
### 8.4 Markdown 直接发文章
用 Jekyll 建博客后，发文章就是三步：在仓库里建一个 _posts 文件夹 → 新建一个名字类似 2024-01-01-我的第一篇文章.md 的文件 → 文件开头写几行“头部信息”（front matter），正文直接写 Markdown。文件头长这样：
---
title: 我的第一篇文章
date: 2024-01-01
---
正文从这里开始，直接写 Markdown 就行……
push 上去，文章就自动出现在你的博客里了。从此写博客 = 写 Markdown + push，超级简单。
## 第9章 搜索与发现（白嫖技巧）
GitHub 上躺着几亿个仓库，怎么快速找到好东西？这章全是白嫖技巧。
### 9.1 搜索语法速查表（12 条+）
在 GitHub 顶部搜索框里输入关键词，配合下面的语法，能精确过滤结果：

| 语法 | 含义 | 例子 |
| --- | --- | --- |
| 关键词 | 全文搜索 | python |
| "精确短语" | 搜索完全匹配的短语 | "machine learning" |
| in:readme | 只在 README 里搜 | in:readme 爬虫 |
| in:name | 只在仓库名里搜 | in:name django |
| language:xxx | 限定编程语言 | language:python |
| stars:>1000 | 星标数大于 1000 | stars:>1000 |
| forks:>500 | 分支（复制）数大于 500 | forks:>500 |
| pushed:>2024-01-01 | 最近更新过 | pushed:>2024-01-01 |
| created:>2023-01-01 | 创建时间之后 | created:>2023-01-01 |
| user:xxx | 只看某个用户的仓库 | user:torvalds |
| org:xxx | 只看某个组织的仓库 | org:github |
| topic:xxx | 按主题搜索 | topic:machine-learning |
| label:good first issue | 搜带某标签的 Issue | label:good first issue |
| is:issue / is:pr | 搜 Issue 或 PR | is:issue label:bug |
| fork:true / fork:false | 是否包含复制品 | fork:false |
| awesome 前缀 | 搜资源合集 | awesome python |

语法还能组合，比如想找“Python 写的、超过 1000 星、关于网页爬虫的项目”：
language:python stars:>1000 爬虫
### 9.2 Awesome 系列是什么
awesome 开头的仓库（比如 awesome-python）是“优质资源合集”：有人帮你把某个领域最值得看的工具、库、教程全部整理好。这相当于 GitHub 上的“精选收藏夹”。用法：搜索 awesome + 你感兴趣的关键词，比如 awesome-python、awesome-machine-learning、awesome-selfhosted（自建服务合集）。学习一个新领域，先找它的 awesome 列表，能少走很多弯路。
### 9.3 Trending 每日热门
打开 github.com/trending，能看到今天全世界最火的项目（按星标增长排序），还可以按语言筛选（Python、JavaScript 等）。每天花 5 分钟刷一眼，就知道行业在流行什么——这是程序员版的“刷微博”。
### 9.4 Star / Fork / Watch 区别
看到好项目，有三个按钮可以点，别搞混：

| 操作 | 作用 | 比喻 |
| --- | --- | --- |
| Star | 收藏 + 点赞，让别人知道这个项目受欢迎 | 给帖子点赞收藏 |
| Fork | 复制一份到你自己账号下，可以随意修改 | 复印一份自己留着 |
| Watch | 关注这个项目的动态，有更新会通知你 | 订阅这个公众号 |

**【技巧】**Star 数越高，代表项目越受欢迎。给喜欢的好项目点个 Star，是开源社区表达感谢最直接的方式，也是帮助项目被更多人发现。
### 9.5 下载单个文件 / 子目录技巧
- 下载单个文件：点进文件 → 点 Raw（原始）按钮 → 在新页面右键 → 另存为，就能只下载这一个文件。
- 下载子目录：克隆整个仓库太大？用 sparse-checkout（稀疏检出），只拉取需要的子目录：
git clone --no-checkout https://github.com/用户名/仓库名.git
cd 仓库名
git sparse-checkout init --cone
git sparse-checkout set docs
git checkout main
执行后本地只会出现 docs 这一个目录，其他大文件都不下载，省流量省时间。
## 第10章 参与开源与求职加分
### 10.1 为什么参与开源
参与开源 = 给别人的开源项目贡献代码。好处多到数不清：

| 好处 | 说明 |
| --- | --- |
| 简历亮点 | 面试官最爱的加分项，比“自我评价写热爱编程”有说服力一万倍 |
| 真实练手 | 接触真实项目、真实用户、真实的代码规范，比自己做练习强太多 |
| 混圈子 | 和大佬同框讨论问题，被看见、被认可，机会自然来 |
| 免费老师 | 看别人怎么组织代码、怎么写测试、怎么做 review，全是免费课 |

### 10.2 找适合新手的项目
- 在 GitHub 搜索框搜 label:good first issue，会列出所有标记了“适合新手”的任务。
- 选项目三看：星标多（说明项目健康）、最近有更新（说明还在维护）、文档全（说明好上手）。
- 从最简单的贡献开始：修文档、补注释、写测试用例、修小 bug，一步步来，别一上来就啃大功能。
### 10.3 贡献流程复习
一句话复习第 4 章：fork（复印）→ clone（拉下来）→ 建分支 → 改代码 → push → 发 PR → 等 review → merge。全流程命令再贴一遍：
git clone https://github.com/你的用户名/项目名.git
git checkout -b my-fix
git add .
git commit -m "fix: 修复 xxx 问题"
git push -u origin my-fix
然后在 GitHub 上点 Compare & pull request 发 PR，等维护者 review。
### 10.4 GitHub 简历怎么写
GitHub 主页就是你的“程序员简历”，从四方面经营：

| 模块 | 怎么做 |
| --- | --- |
| 主页 README | 建同名仓库，放自我介绍、技术栈、联系方式 |
| 置顶项目 | 在主页点 Customize your pins，置顶 6 个最能打的项目 |
| 贡献热力图 | 主页那些绿格子，坚持每天提交，越绿越好看（面试官真的会看） |
| 项目 README | 每个项目都要有像样的 README，别人点进去看得懂 |

**【技巧】**热力图不要求你天天写代码，但“长期、稳定地提交”这件事本身，就是自律和持续学习的证明，面试官很吃这一套。
### 10.5 面试中 GitHub 怎么讲
- 挑 2-3 个最能打的项目，不要贪多。
- 讲“为什么做”：当时遇到了什么问题、为什么选择做这个项目（解决问题的动机最打动面试官）。
- 讲“怎么做的”：技术选型、整体结构、你负责的部分、用到了哪些 Git/GitHub 协作方式。
- 讲“踩过的坑”：说一个真实 bug 或冲突是怎么解决的一 这种故事最显实力。
- 别背代码、别背 README，像讲故事一样讲你的项目。
**【重点】**一句话公式：为什么做 + 怎么做的 + 踩过什么坑 + 学到了什么。按这个公式准备 2-3 个项目，面试这一关稳了。
## 第11章 常见坑与避坑指南
这章全是过来人的血泪经验，每个坑都给出解决办法，建议收藏。
### 11.1 push 被拒（non-fast-forward）
报错：! [rejected] main -> main (non-fast-forward)。原因：远端有别人（或你另一台电脑）的新提交，而你本地没有。解决：先 pull 把远端的新提交拉下来合并，再 push。
git pull --rebase
git push
**【易错】**记住口诀：push 被拒，先 pull 再 push。
### 11.2 冲突解决（再复习一遍）
完整流程：看到冲突提示 → 打开冲突文件 → 删除 <<<<<<< ======= >>>>>>> 标记、保留想要的内容 → git add → git commit。
# 1. 看看哪些文件冲突了
git status
# 2. 手动编辑文件，保留正确内容，删掉冲突标记
# 3. 标记已解决
git add 冲突的文件名
# 4. 提交
git commit -m "merge: 解决冲突"
### 11.3 误删分支 / 误操作恢复（reflog）
Git 有个“后悔药”：reflog 会记录你所有的操作历史，哪怕分支被删、提交被 reset 掉，也能找回来。
# 查看操作历史
git reflog
# 恢复到某次操作之前的状态
git reset --hard HEAD@{1}
只要你能在 reflog 里找到那个提交编号，就能把几乎任何误操作救回来。
### 11.4 .gitignore 是什么
.gitignore 是一个特殊文件，告诉 Git“哪些文件不要管、不要提交”。需要忽略的典型文件：依赖目录（node_modules）、缓存目录（__pycache__）、密钥文件（.env）、系统垃圾文件（.DS_Store）。直接复制这份模板：
# 依赖和构建产物
node_modules/
dist/
build/
__pycache__/
*.pyc
# 密钥和环境变量（千万别提交！）
.env
.env.local
*.pem
config/secret.json
# 系统垃圾文件
.DS_Store
Thumbs.db
desktop.ini
# 日志
*.log
把这份内容保存为 .gitignore 放在仓库根目录，Git 就会自动忽略这些文件。
### 11.5 不要把密码提交上去（重要警告）
这是全文档最重要的一条警告：绝对不要把密码、API 密钥、token、数据库连接串提交到 GitHub！
**【重点】**一旦密钥进了公开仓库，等于把家门钥匙贴在大街上——任何人都能搜到、都能用你的账号，可能造成金钱损失或严重安全事件。这不是吓唬人，每年都有大量真实案例。
- 提交前自查：git status 看一眼，确认没有 .env、config.json 这类文件混进来。
- 密钥永远放本地环境变量或 .env 文件里，并用 .gitignore 排除。
- 万一已经提交了：第一，立刻去相关平台修改密码 / 吊销 token（改密码是第一步，删除提交记录只是补救）；第二，再用工具清理历史（如 git filter-repo，高级操作，建议查官方文档）。
- GitHub 有自动扫描机制（secret scanning），会检测到部分泄露的密钥并警告你，但别指望它，自己小心才是正道。
### 11.6 大文件提交不了
GitHub 限制单个文件最大 100MB（超过 50MB 就警告）。视频、数据集、安装包这类大文件直接传会失败。解决办法是 Git LFS（Large File Storage，大文件存储）：
git lfs install
git lfs track "*.zip"
git add .gitattributes
git add 大文件.zip
git commit -m "feat: 添加数据包"
git push
LFS 会把大文件单独存到 GitHub 的专门存储里，仓库本身保持轻量。
### 11.7 代理 / 网络问题（clone 慢）
国内访问 GitHub 偶尔很慢或连不上，常见解决办法：
- 用代理（如果你有）：给 Git 配置代理：
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
# 不用代理时取消
git config --global --unset http.proxy
git config --global --unset https.proxy
- 换镜像站：用国内镜像（如 ghproxy 类加速前缀）下载仓库压缩包。
- 换 SSH 方式：有时候 HTTPS 慢，改用 SSH 反而快。
**【易错】**不要随便用来路不明的“加速器”或第三方工具——它们可能偷你的账号和代码。安全第一。
### 11.8 常见坑速查表

| 问题 | 原因 | 解决办法 |
| --- | --- | --- |
| push 被拒 | 远端有新提交，本地没有 | git pull --rebase 再 git push |
| 合并冲突 | 两个人改了同一处 | 手动解决 → git add → git commit |
| clone 特别慢 | 网络/代理问题 | 配代理、换镜像、或换 SSH |
| 密钥泄露 | 把 .env 之类提交上去了 | 立即改密码/吊销 token，再清理历史 |
| 大文件传不上 | 超过 100MB | 用 Git LFS |
| 提交信息乱写 | 写 update、111 | 按规范写 feat:/fix:/docs: 前缀 |
| git 命令不识别 | 没装好或没重开终端 | 重装 Git，重开 PowerShell 再试 |
| 网页打不开 | 网络问题 | 刷新、换浏览器、检查代理 |

## 附录A Git 命令速查总表（40+ 条）

| 命令 | 作用 | 常用例子 |
| --- | --- | --- |
| git init | 初始化仓库 | git init |
| git clone <地址> | 克隆远程仓库 | git clone https://github.com/xxx/yyy.git |
| git status | 查看工作区状态 | git status |
| git add <文件> | 加入暂存区 | git add index.html |
| git add . | 加入全部文件 | git add . |
| git add -A | 加入全部（含删除） | git add -A |
| git commit -m "信息" | 提交并写说明 | git commit -m "feat: 新增登录" |
| git commit -am "信息" | add + commit 一步 | git commit -am "fix: 改标题" |
| git log | 查看提交历史 | git log |
| git log --oneline | 简洁版历史 | git log --oneline |
| git log --oneline --graph | 图形化历史 | git log --oneline --graph |
| git diff | 查看未暂存改动 | git diff |
| git diff --staged | 查看已暂存改动 | git diff --staged |
| git show <编号> | 查看某次提交详情 | git show a1b2c3d |
| git push | 推送本地提交 | git push |
| git push -u origin main | 首次推送并关联 | git push -u origin main |
| git pull | 拉取并合并 | git pull |
| git pull --rebase | 拉取并用变基合并 | git pull --rebase |
| git fetch | 只拉取不合并 | git fetch |
| git branch | 查看本地分支 | git branch |
| git branch <名> | 创建分支 | git branch dev |
| git branch -a | 查看全部分支 | git branch -a |
| git branch -d <名> | 删除分支 | git branch -d dev |
| git branch -D <名> | 强制删除分支 | git branch -D dev |
| git checkout <分支> | 切换分支 | git checkout dev |
| git checkout -b <名> | 创建并切换 | git checkout -b feature-x |
| git switch <分支> | 切换分支（新版） | git switch dev |
| git switch -c <名> | 创建并切换（新版） | git switch -c feature-y |
| git merge <分支> | 合并分支 | git merge dev |
| git rebase <分支> | 变基（重排提交） | git rebase main |
| git stash | 暂存未提交改动 | git stash |
| git stash pop | 恢复暂存改动 | git stash pop |
| git stash list | 查看暂存列表 | git stash list |
| git stash drop | 丢弃某条暂存 | git stash drop stash@{0} |
| git tag <名> | 打标签 | git tag v1.0.0 |
| git tag | 查看标签 | git tag |
| git push origin <标签> | 推送标签 | git push origin v1.0.0 |
| git revert <编号> | 反向提交（安全） | git revert a1b2c3d |
| git reset --soft HEAD~1 | 撤销提交保留改动 | git reset --soft HEAD~1 |
| git reset --hard HEAD~1 | 撤销提交丢改动（危险） | git reset --hard HEAD~1 |
| git reset --hard <编号> | 回到某个提交 | git reset --hard a1b2c3d |
| git reflog | 查看操作历史 | git reflog |
| git remote -v | 查看远程地址 | git remote -v |
| git remote add origin <地址> | 添加远程 | git remote add origin https://github.com/xxx/yyy.git |
| git remote remove origin | 删除远程 | git remote remove origin |
| git config --global user.name "名" | 配置用户名 | git config --global user.name "张三" |
| git config --global user.email "邮" | 配置邮箱 | git config --global user.email "a@b.com" |
| git config --list | 查看全部配置 | git config --list |
| git rm <文件> | 删除文件 | git rm old.txt |
| git mv <旧> <新> | 重命名文件 | git mv a.txt b.txt |
| git cherry-pick <编号> | 挑一个提交过来 | git cherry-pick a1b2c3d |
| git clean -fd | 清理未跟踪文件（危险） | git clean -fd |
| git grep "关键词" | 在仓库里搜索 | git grep "TODO" |
| git help <命令> | 查看命令帮助 | git help log |
| git lfs install | 启用大文件支持 | git lfs install |
| git lfs track "*.zip" | 跟踪大文件 | git lfs track "*.zip" |

## 附录B GitHub 网页操作速查表（20+ 条）

| 想做什么 | 在哪点 / 怎么做 |
| --- | --- |
| 新建仓库 | 右上角 + 号 → New repository |
| 改仓库名/描述 | 仓库页 → Settings → General → Repository name / Description |
| 删除仓库 | 仓库页 → Settings → Danger Zone → Delete this repository |
| 收藏项目 | 仓库右上角 Star |
| 复制项目到自己账号 | 仓库右上角 Fork |
| 关注项目更新 | 仓库右上角 Watch 下拉选 All Activity |
| 下载仓库压缩包 | 仓库页 Code 按钮 → Download ZIP |
| 发 Pull Request | 仓库页 Pull requests → New pull request → 选分支 → Create |
| 审查别人的 PR | PR 页面 → Files changed → 逐行评论 → Review changes → Approve |
| 合并 PR | PR 页面 → Merge pull request → 选合并方式 → Confirm merge |
| 提 Issue | 仓库页 Issues → New issue → 写标题和内容 → Submit |
| 给 Issue 打标签 | Issue/PR 页面右侧 Labels 齿轮图标 |
| 指派负责人 | Issue/PR 页面右侧 Assignees |
| 看自动化运行结果 | 仓库页 Actions 标签页 |
| 开启 GitHub Pages | 仓库 Settings → Pages → Source 选分支 → Save |
| 添加 SSH 公钥 | 头像 → Settings → SSH and GPG keys → New SSH key |
| 生成访问令牌 Token | 头像 → Settings → Developer settings → Personal access tokens |
| 修改头像 | 头像 → Settings → Profile → Upload a photo |
| 修改简介 Bio | 头像 → Settings → Profile → Bio |
| 置顶项目 | 个人主页 → Customize your pins → 选 6 个项目 |
| 发 Release（版本发布） | 仓库页 Releases → Draft a new release → 写版本号 → Publish |
| 看每日热门 | 访问 github.com/trending |
| 搜索代码/仓库 | 页面顶部搜索框，配合语法（见第 9 章） |
| 开启两步验证 | 头像 → Settings → Password and authentication → Two-factor authentication |
| 看自己的贡献热力图 | 个人主页 Contributions 区域 |
| 给项目提建议 | 仓库页 Discussions（若开启） |

## 附录C 提交信息规范与常用 emoji 表（20+ 条）
规范写法：<类型>: <说明>，比如 feat: 新增登录页面。加 emoji 更醒目（非必需，团队统一即可）。

| 类型 | emoji | 含义 | 提交信息例子 |
| --- | --- | --- | --- |
| feat | 🎉 | 新功能 | feat: 新增登录页面 |
| fix | 🐛 | 修复 bug | fix: 修复按钮点击无反应 |
| docs | 📝 | 文档 | docs: 更新 README |
| style | 🎨 | 格式/样式 | style: 调整代码缩进 |
| refactor | ♻️ | 重构 | refactor: 拆分 login 函数 |
| perf | ⚡ | 性能优化 | perf: 加速图片加载 |
| test | ✅ | 测试 | test: 新增登录测试用例 |
| build | 📦 | 构建相关 | build: 升级打包配置 |
| ci | 💚 | CI 配置 | ci: 修复 Actions 报错 |
| chore | 🔧 | 杂务/依赖 | chore: 更新依赖版本 |
| revert | ⏪ | 回滚 | revert: 回滚登录页改动 |
| release | 🚀 | 发布版本 | release: 发布 v1.2.0 |
| deps+ | ➕ | 添加依赖 | chore: ➕ 添加 requests 库 |
| deps- | ➖ | 移除依赖 | chore: ➖ 移除无用依赖 |
| deps↑ | ⬆️ | 升级依赖 | chore: ⬆️ 升级 Flask 到 3.0 |
| deps↓ | ⬇️ | 降级依赖 | chore: ⬇️ 降级 numpy |
| security | 🔒 | 安全修复 | fix: 🔒 修复 XSS 漏洞 |
| i18n | 🌐 | 国际化/翻译 | feat: 🌐 添加英文翻译 |
| remove | 🔥 | 删除无用代码 | refactor: 🔥 删除废弃函数 |
| typo | ✏️ | 修正笔误 | docs: ✏️ 修正错别字 |
| docker | 🐳 | Docker 相关 | build: 🐳 更新 Dockerfile |
| asset | 🍱 | 资源文件 | feat: 🍱 添加图标资源 |
| lint | 🚨 | 修复代码检查警告 | style: 🚨 修复 lint 警告 |
| wip | 🚧 | 开发中（半成品） | feat: 🚧 登录页开发中 |

**【技巧】**emoji 可以自己加在说明文字里（如 fix: 🐛 修复 xxx），GitHub 提交历史里会显示彩色图标，一眼就能看出每次提交的类型。

## 相关笔记

- [[程序员知识库]]
- [[Linux系统使用技巧]]
- [[Docker使用技巧]]
