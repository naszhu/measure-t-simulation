
 Open your editor to edit the last commit’s message:
```
git commit --amend
# 2. Amend the most recent commit to include it
git commit --amend --no-edit
```

``git diff a1b2c3d4 e5f6g7h8 -- src/main.py``

check, when a line in a file was added in that file
```
git blame -L 42,42 -- path/to/file.ext
```

Or amend it in one step:
```
git commit --amend -m "Your new commit message"
```

force push
```
git push --force-with-lease origin main
```

---
### Repo
```
Parent: #1220  
That cross-link makes it easy to navigate both ways.

```

```markdown
> **Child repos:**  
> • [`REM_E3_model_fixed`](https://github.com/naszhu/REM_E3_model_fixed) – Design-3 modelling code  
> • [`EXP_host`](https://github.com/naszhu/EXP_host) – live jsPsych front-end (Cloudflare Pages)
```


##### Insert between commits:

```git
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
```git
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

```git
# 1. Start an interactive rebase at the parent of your “Meeting log Jun 12th” commit.
#    If that commit is two back from HEAD, you can do:
git rebase -i HEAD~3

#`pick` to `edit`, then save & exit:

# 2. When rebase stops at your Jun 12th commit, set the new date:
DATE=$(date -d '2025-06-12 17:00:00 +0800' '+%Y-%m-%dT%H:%M:%S%z')

# 3. Amend that commit’s date without touching its message:
GIT_COMMITTER_DATE="$DATE" git commit --amend --no-edit --date="$DATE"

# 4. Continue the rebase (it will replay the later commits on top):
git rebase --continue

# 5. Finally, force-push your rewritten history back to origin:
git push --force-with-lease origin main
```