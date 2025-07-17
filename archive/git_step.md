### Upload to Git
- `cd user/my-project`: change to current working directory 
- `git init`: initialize project
- `git add A.txt` or `git add .`: add to staging area
- `git commit -m "the message you want to convey"`: commit to git

### Push to GitHub
- `git remote add origin https://github.com/your-username/your-repository.git`: associate with remote repository
- `git push -u origin main`: link local branch with remote branch 

### If u already have a repository on GitHub
`add`-`commit`-`push`

### Clone from GitHub
- `git clone https://github.com/username/repository.git`: clone the project

### If u wanna contribute to a repository
- `fork` to your own profile
- `clone` to local 
- `git remote add upstream https://github.com/username/repository.git`: add original author as upstream
- `git fetch upstream`：get upstream  
`git merge upstream/main`: get updates of the original repository
- request for *Pull Request* on GitHub


