---
title: "Hugo"
date: 2026-04-29
tags: [blog]
---
- #blog
- ## 标准工作流
	- Hugo 的标准工作流主要围绕 **“本地写作 -> 版本控制 -> 自动构建/部署”** 这几个核心环节展开。下面是一个标准、高效的工作流程，能帮你快速上手。
	  
	  ```mermaid
	  flowchart TD
	      A[本地安装Hugo] --> B[创建新站点]
	      B --> C[添加/配置主题]
	      C --> D[本地创建内容<br>（Markdown + Front Matter）]
	      D --> E[本地预览<br>hugo server]
	      E -- 满意 --> F[构建静态文件<br>hugo]
	      F --> G[部署到服务器<br>（如GitHub Pages）]
	      
	      G --> H[Git推送源码<br>git push]
	      H --> I[CI自动构建与部署<br>（如GitHub Actions）]
	      I --> J[网站更新上线]
	      
	      D -- 修改/新增 --> E
	  ```
	- ### 🔧 第一步：环境搭建与项目初始化
	  
	  这是所有工作的基础，只需进行一次。
	  
	  1.  **安装Hugo**：根据你的操作系统选择安装方式。
	    *   **macOS**: `brew install hugo`
	    *   **Windows**: 可使用 **Chocolatey** (`choco install hugo-extended`) 或 **Winget** (`winget install Hugo.Hugo.Extended`)
	    *   **Linux**: 使用包管理器，如 `sudo apt install hugo` (Debian/Ubuntu) 
	    > **💡 建议安装“扩展版”**：部分主题需要Sass/SCSS支持，安装 `hugo-extended` 版本可以避免后续麻烦。
	  
	  2.  **创建新站点**：在终端中运行以下命令，会在当前目录下生成一个名为 `my-blog` 的文件夹。
	    ```bash
	    hugo new site my-blog
	    cd my-blog
	    ```
	  
	  3.  **初始化Git仓库（强烈推荐）**：从这一步开始进行版本控制，是后续实现自动化部署的关键。
	    ```bash
	    git init
	    ```
	- ### ✍️ 第二步：添加主题与创作内容
	  
	  站点建好后，就可以挑选喜欢的“皮肤”（主题），并开始写文章了。
	  
	  1.  **选择并安装主题**：访问 [Hugo官方主题库](https://themes.gohugo.io/) 挑选一个喜欢的。推荐使用 **Git Submodule** 的方式添加，方便后续更新主题。
	    ```bash
	    # 以添加 “Ananke” 主题为例
	    git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
	    ```
	  2.  **配置主题**：将主题文件夹 `exampleSite` 里的配置文件（如 `config.toml`）内容，复制到你站点的根目录配置文件中。
	  
	  3.  **创作新文章**：使用以下命令创建一篇新文章，一个Markdown文件会出现在 `content/posts/` 目录下。
	    ```bash
	    hugo new posts/my-first-post.md
	    ```
	  
	  4.  **编辑文章内容**：用任何代码编辑器打开刚才生成的Markdown文件。你会看到文件顶部有这样一段“前言”（Front Matter）：
	    ```yaml
	    ---
	    title: "My First Post"
	    date: 2025-05-08T10:00:00+08:00
	    draft: true  # 草稿状态，预览时需加 -D 参数才能看到
	    ---
	    ```
	    将 `draft: true` 改为 `false`，就可以在下方用Markdown语法开始写作了。
	- ### 🚀 第三步：本地预览与构建
	  
	  在发布前，最好先在本地确认效果。
	  
	  1.  **本地预览**：在站点根目录下运行 `hugo server`。终端会显示一个本地地址（通常是 `http://localhost:1313`），在浏览器打开它就能实时预览网站效果。
	    *   如果想预览包括“草稿”在内的所有文章，可以加上 `-D` 参数：`hugo server -D`。
	  
	  2.  **构建静态文件**：当你对网站内容满意后，运行 `hugo` 命令。Hugo 会瞬间将你所有的内容和主题，编译成纯静态的HTML、CSS和JS文件，默认存储在 `public/` 文件夹中。
	    ```bash
	    hugo
	    # 如果想对文件进行压缩，可以加上 --minify 参数
	    hugo --minify
	    ```
	- ### 🌐 第四步：部署上线
	  
	  你不需要手动把 `public/` 文件夹里的内容上传到服务器，最标准的做法是使用 **Git + CI（持续集成）**。
	  
	  1.  **连接远程代码库**：在 GitHub、GitLab 或 Gitee 上创建一个空的仓库，并将本地的代码推送到远程。
	    ```bash
	    git remote add origin https://github.com/你的用户名/你的仓库名.git
	    git branch -M main
	    git push -u origin main
	    ```
	  
	  2.  **配置自动化部署（以GitHub Pages为例）**：这是Hugo工作流的精髓，一旦配置好，以后你只需要负责写作和 `git push`，网站会自动更新。
	    *   在你的GitHub仓库中，点击 **Settings** -> **Pages**。在 **Build and deployment** 部分，将 **Source** 改为 **GitHub Actions**。
	    *   GitHub 可能会提供预设的Hugo工作流，或者你可以手动创建一个新文件 `.github/workflows/hugo.yaml`，并粘贴官方提供的工作流配置代码。这个配置文件会告诉GitHub，当你每次推送代码时，如何自动安装Hugo、构建网站，并部署到Pages服务上。
	  
	  3.  **享受自动化**：完成上述设置后，只要你运行 `git push` 将新文章推送到GitHub，GitHub Actions就会自动运行，几分钟后你的网站就会更新。整个流程中，你无需再手动运行 `hugo` 命令或管理 `public/` 文件夹，非常方便。
-