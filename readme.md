git init 初始化本地仓库
git add 添加文件
git commond -m 提交文件
git status 查看状态

生成本地id_rsa是私钥，不能泄露；id_rsa.pub是公钥
ssh-keygen -t rsa -C "youxiang@qq.com"
or
git config --global user.name “username”
git config --global user.email “email”