5、提交修改，首先切换到LearnGit文件路径：

cd /Users/WENBO/Desktop/LearnGit 

然后输入：
//文件添加到仓库（.代表提交所有文件）
git add .
//把文件提交到仓库
git commit -m "First Commit"
//上传到github
git push

终端完整输出如下：
Last login: Sat Jan  6 15:49:54 on ttys000
WMBdeMacBook-Pro:~ WENBO$ cd /Users/WENBO/Desktop/LearnGit 
WMBdeMacBook-Pro:LearnGit WENBO$ git add .
WMBdeMacBook-Pro:LearnGit WENBO$ git commit -m "First Commit"
[master ae3bbe9] First Commit
 11 files changed, 649 insertions(+)
 create mode 100644 LearnGitDemo/LearnGitDemo.xcodeproj/project.pbxproj
 create mode 100644 LearnGitDemo/LearnGitDemo.xcodeproj/project.xcworkspace/contents.xcworkspacedata
 create mode 100644 LearnGitDemo/LearnGitDemo/AppDelegate.h
 create mode 100644 LearnGitDemo/LearnGitDemo/AppDelegate.m
 create mode 100644 LearnGitDemo/LearnGitDemo/Assets.xcassets/AppIcon.appiconset/Contents.json
 create mode 100644 LearnGitDemo/LearnGitDemo/Base.lproj/LaunchScreen.storyboard
 create mode 100644 LearnGitDemo/LearnGitDemo/Base.lproj/Main.storyboard
 create mode 100644 LearnGitDemo/LearnGitDemo/Info.plist
 create mode 100644 LearnGitDemo/LearnGitDemo/ViewController.h
 create mode 100644 LearnGitDemo/LearnGitDemo/ViewController.m
 create mode 100644 LearnGitDemo/LearnGitDemo/main.m
WMBdeMacBook-Pro:LearnGit WENBO$ git push
Warning: Permanently added the RSA host key for IP address '192.30.255.112' to the list of known hosts.
Counting objects: 20, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (18/18), done.
Writing objects: 100% (20/20), 6.80 KiB | 0 bytes/s, done.
Total 20 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
To github.com:wenmobo/LearnGit.git
   1000218..ae3bbe9  master -> master
WMBdeMacBook-Pro:LearnGit WENBO$ 

查看GitHub上的项目，LearnGit已经上传成功啦，如下图所示：

作者：WenBo丨星空灬
链接：https://www.jianshu.com/p/7edb6b838a2e
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
