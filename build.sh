#!/bin/bash

# Hugo 博客构建脚本
# 用途：清理、转换、构建、预览

set -e  # 任何命令失败都会退出

echo "================================================"
echo "开始构建 Hugo 博客..."
echo "================================================"

# 1. 清空 content 目录下的文件（保留子文件夹）
echo ""
echo "📝 第1步：清空 content 目录下的文件..."
find ./content -type f -delete
echo "✅ 已清空 content 目录下的文件"

# 2. 删除 public 文件夹里的内容
echo ""
echo "🗑️  第2步：删除 public 文件夹内容..."
if [ -d "./public" ]; then
    rm -rf ./public/*
    echo "✅ 已清空 public 目录"
else
    mkdir -p ./public
    echo "✅ public 目录已创建"
fi

# 3. 运行 logseq-to-hugo-v2.py 脚本
echo ""
echo "🔄 第3步：运行 Logseq 转 Hugo 脚本..."
python3 ./scripts/logseq-to-hugo-v2.py
echo "✅ Logseq 笔记已转换"

# 4. 执行 hugo --gc --minify
echo ""
echo "🏗️  第4步：构建 Hugo 站点（清理 + 最小化）..."
hugo --gc --minify
echo "✅ Hugo 站点构建完成"

# 5. 启动 Hugo 开发服务器
echo ""
echo "🚀 第5步：启动 Hugo 开发服务器..."
echo "================================================"
echo "服务器地址: http://localhost:1313"
echo "按 Ctrl+C 停止服务器"
echo "================================================"
echo ""
hugo server -D
