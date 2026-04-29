---
title: "My First Post"
date: 2023-10-05
draft: false
---

这里是我的第一篇博客内容。
```

将 `draft` 改为 `false`，文章就会在最终发布时显示。

---

### 6. **运行本地开发服务器**

运行以下命令可以在本地启动一个开发服务器：
```bash
hugo server -D
```

然后你可以在浏览器中访问 `http://localhost:1313` 查看你的网站。

---

### 7. **生成静态文件并发布**

生成静态文件用于部署到服务器：
```bash
hugo
```
生成的文件会默认存放在 `public` 文件夹中，你可以通过任何支持静态文件的网站托管服务（如 GitHub Pages、Netlify、Vercel）部署。

---

### 8. **部署博客**

#### A. GitHub Pages 示例
1. 将 `public` 文件夹部署到 `gh-pages` 分支：
   ```bash
   cd public
   git init
   git add .
   git commit -m "Deploy my Hugo site"
   git branch -M gh-pages
   git remote add origin https://github.com/你的用户名/你的仓库名.git
   git push -u origin gh-pages