---

---
  
  

## ✅ 步骤一：创建脚本文件

  
  

在项目根目录下，创建名为 `log_plot.sh` 的文件：

  
  

```bash

touch log_plot.sh

chmod +x log_plot.sh # 赋予可执行权限

  

```

  

编辑它，粘贴以下内容（按你当前结构调整后）：

  
  

```bash

#!/bin/bash

  

# === Get current commit and timestamp ===

commit=$(git rev-parse --short HEAD)

timestamp=$(date "+%Y-%m-%d %H:%M:%S")

  

# === Define destination folder and filenames ===

mkdir -p plot_archive

cp plot1.png plot_archive/${commit}_plot1.png

cp plot2.png plot_archive/${commit}_plot2.png

  

# === Append to markdown ===

echo "## Commit [$commit](https://github.com/yourusername/yourrepo/commit/$commit) — $timestamp" &gt;&gt; model_progress.md

echo "![](plot_archive/${commit}_plot1.png)" &gt;&gt; model_progress.md

echo "![](plot_archive/${commit}_plot2.png)" &gt;&gt; model_progress.md

echo "" &gt;&gt; model_progress.md

  

```

  
  

## ✅ 步骤二：设置 .gitignore

  
  

在根目录下的 `.gitignore` 添加：

  
  

```gitignore

plot_archive/

plot1.png

plot2.png

  

```

  
  

## ✅ 步骤三：运行方法

  
  

每次你完成一次 commit 后，运行：

  
  

```bash

./log_plot.sh

  

```
# 🔧 设置 post-commit 自动运行脚本

  
  

1. 在你的仓库中创建 Git 钩子文件：

  

```bash

mkdir -p .git/hooks

nano .git/hooks/post-commit

  

```

  

1. 填入内容：

  

```bash

#!/bin/bash

# Run the plot logging after each commit

bash ./log_plot.sh

  

```

  

1. 赋予执行权限：

  

```bash

chmod +x .git/hooks/post-commit

  

```

  

这样，每次你运行：

  
  

```bash

git commit -m "..."

  

```

  

Git 自动会运行 `log_plot.sh`，把当前的 `plot1.png/plot2.png` 加进 archive 并更新 `model_progress.md`。









---
# Then, changed idea add these below 
![[Pasted image 20250711234752.png]]