## change config
command change
```
git config --global core.editor vim
git config --global user.email "wang.shuxi@outlook.com"
git config --global user.name "wang shuxi"
```

 ~/.gitconfig
```
[user]
        name = Shuxi Wang
        email = wang.shuxi@outlook.com

[core]
        editor ='vim'

[user]
        name = gitsuck
        email = fxbp@outlook.com

[core]
        editor ='vim'

```


## general cmd
```
git push -u origin master(main)
git add .
git commit .
git commit --amend [commit id]
```

## reset
```
git reset --soft HEAD~
reset to the previous version but the files don't change

git reset --hard HEAD~
reset and files changed
```

## push
```
git push -u ogrigin main/master

# force push
git push -f 
git push origin <your_branch_name> --force
```

## pull
```
git pull
```

## branch
```
git branch <new-branch>
git branch <new-branch> <base-branch>
git branch <new-branch> commit id

git checkout branch_name
git push -u origin <local-branch>


git cherry-pick <commit>
```



```bash
git cherry-pick <commitHash>
```