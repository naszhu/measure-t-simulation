[[conventional commit]]]


### GIT edit in vs code:  don't go in nano
```bash
git config --global core.editor "code --wait"
```
once will write that setting into your `~/.gitconfig` and persist for all future Git commands (across shells and repos). If you ever need to change it, just re-run with a different editor or omit `--global` to set it per-repo.\



### normal git thing

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
#### Compare between files for specific commits
```bash
git diff COMMIT_ID1 COMMIT_ID2 -- path/to/yourfile.jl
```

## Issue

find issue with keyword
```bash
gh issue list | grep 'function'
```

[Commit ]refer to issue in another repo
```text
Refs naszhu/project-context#42
```


##### Repo Issue Links
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
DATE=$(date -d '2025-06-22 17:20:00 +0800' '+%Y-%m-%dT%H:%M:%S%z')

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


#### Get all repo names  
```bash
gh repo list naszhu --limit 100 --json name
 -q '.[].name'
```
# Notes
One commit:
```bash
git notes add -m "⚠️ Known bug: off-by-one here" <bad-commit-hash>

git push origin refs/notes/*
```
 A series of commits:
```bash
# Annotate all those SHAs with the same note
commits=(
  6cd43de
  17777ae
  89e265c
  9fb5dcb
  b11ee7c
  9c4b2aa
)

for sha in "${commits[@]}"; do
  git notes add -m "⚠️ Known bug: should have made p_switch to zero in checking pure influence, but forgot to do that. I went back, checked out each commit and found that the predictions change a bit but the general trend of the A)-D) are the same." "$sha"
done

# push your notes up
git push origin refs/notes/*
```

Ways of view notes:
```bash
# 1) show notes inline in your log
git log --show-notes=commits --oneline
bash
Copy
Edit
# 2) list every commit-SHA with a note, then print each note
git notes list | awk '{print $2}' | xargs -n1 git notes show
```
## Branch

modify branch name
```bash
git branch -m debug-first-stage-disappear-issue35
```

merge branch in parallel
```bash
git checkout main
git merge --no-ff simple-v-after-recall-explore \
  -m "Merge feature simple-v-after-recall-explore into main"
git push
```

merge side branch without changing main head  
```bash
git merge --no-ff -s ours temp_branch
```
### revert history (go to last version)
```bash
git reflog
git reset --hard HEAD@{1}
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

##### push merge to git 
```bash
# 1. Switch back to main
git switch main

# 2. Merge in your feature branch, forcing a merge-commit so you see the join point
git merge --no-ff feature -m "Merge feature into main"

# 3. (Optional) Push the updated main up to remote
git push origin main
```