git init 初始化本地仓库
git add 添加文件
git commond -m 提交文件
git status 查看状态

生成本地id_rsa是私钥，不能泄露；id_rsa.pub是公钥
ssh-keygen -t rsa -C "youxiang@qq.com"
or
git config --global user.name “username”
git config --global user.email “email”

github 添加公钥 id_rsa.pub是公钥
ssh -T git@github.com 查看是否添加成功

github 建立新仓库 不要选初始化

根据仓库的命令用
git remote add origin https://github.com/xu-xiaoya/Elegent.git
问题一：新建远程仓库的时候勾选Initialize this repository with a README，推送时可能会报failed to push some refs to https://github.com/xu-xiaoya/Elegent.git的错。

解决方案：这是由于你新创建的那个仓库里面的README文件不在本地仓库目录中，这时可以同步内容。

$ git pull --rebase origin master
1
之后再进行git push origin master就能成功了。

常见的使用命令

git clone 拷贝远程仓库
git reset 回退版本 https://www.runoob.com/git/git-reset.html
git diff 查看改动 https://www.runoob.com/git/git-diff.html
git rm 删除 https://www.runoob.com/git/git-rm.html
git mv 移动 https://www.runoob.com/git/git-mv.html

git log 查看历史记录 https://blog.csdn.net/m0_46278037/article/details/119628828
https://www.runoob.com/git/git-commit-history.html#git-log
git blame <file> 查看指定文件 https://www.runoob.com/git/git-commit-history.html#git-blame

git fetch 从远程仓库获取代码
git merge 融合不同分支
git pull 下载远程代码并合并
git push 长传远程代码并合并