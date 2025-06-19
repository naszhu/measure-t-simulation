
 Open your editor to edit the last commit’s message:
```bash
git commit --amend
# 2. Amend the most recent commit to include it
git commit --amend --no-edit
```

``git diff a1b2c3d4 e5f6g7h8 -- src/main.py``

check, when a line in a file was added in that file
```bash
git blame -L 42,42 -- path/to/file.ext
```

Or amend it in one step:
```bash
git commit --amend -m "Your new commit message"
```

force push
```bash
git push --force-with-lease origin main
```

---
### Repo Issue Links
```
Parent: #1220  
That cross-link makes it easy to navigate both ways.

```

```markdown
> **Child repos:**  
> • [`REM_E3_model_fixed`](https://github.com/naszhu/REM_E3_model_fixed) – Design-3 modelling code  
> • [`EXP_host`](https://github.com/naszhu/EXP_host) – live jsPsych front-end (Cloudflare Pages)
```

1. Make Commits in current repo to refer issue in another repo 
```txt
Refs other-owner/other-repo#42
```
##### Insert between commits:

```bash
# 1. Stash your un-committed changes
git add .
git stash

# 2. Start an interactive rebase over the last two commits
git rebase -i HEAD~2
```
In the editor, change it to:

```
edit <HEAD~1-SHA>
pick <HEAD-SHA>
```

Then:
```bash
# 3. When it stops at HEAD~1, re-apply your stashed work
git stash pop

# 4. Create your “insertion” commit
git add .
git commit -m "Your new commit message"

# 5. Continue the rebase (this will replay the original HEAD on top)
git rebase --continue

# 5. force push
git push --force-with-lease origin main
```

##### Change Commit into a certain date:

```bash
# 1. Start an interactive rebase at the parent of your “Meeting log Jun 12th” commit.
#    If that commit is two back from HEAD, you can do:
git rebase -i HEAD~3

#`pick` to `edit`, then save & exit:

# 2. When rebase stops at your Jun 12th commit, set the new date:
DATE=$(date -d '2025-06-17 17:20:00 +0800' '+%Y-%m-%dT%H:%M:%S%z')

# 3. Amend that commit’s date without touching its message:
GIT_COMMITTER_DATE="$DATE" git commit --amend --no-edit --date="$DATE"

# 4. Continue the rebase (it will replay the later commits on top):
git rebase --continue

# 5. Finally, force-push your rewritten history back to origin:
git push --force-with-lease origin main
```

##### Delete a file from all commits
```bash
cd /path/to/project-context
git fetch --all --tags
git filter-repo --path "IRB FOR ALL/" --invert-paths

###############3here, 
# if refusing to do the above, then do the below, then redo the above
git reflog expire --expire=now --all
git gc --prune=now --aggressive
###########


git push origin --force --all
git push origin --force --tags

```


Branch out and save
```bash
# 1. Create a new branch at the current HEAD (commit C)
git branch feature

# 2. Move main back one commit, dropping C from main
git reset --hard HEAD~1

# 3. Switch to your feature branch to keep working on top of C
git checkout feature

# then checkout back to main, or just work on the feature branch

```


Delete a branch
```bash
# Delete a local branch (won’t delete if it’s unmerged):
git branch -d <branch-name>

# Force‐delete a local branch (even if unmerged):
git branch -D <branch-name>

# Delete a remote branch:
git push origin --delete <branch-name>
```


## Between Branches
##### Move local main pointer when in another branch
```bash
git branch -f main HEAD~2
```