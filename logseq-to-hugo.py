import os
import re
from datetime import datetime
from pathlib import Path

# 配置区域
LOGSEQ_ROOT_DIR = "/mnt/c/Users/40969/Documents/KMS/20-logseq"
HUGO_CONTENT_DIR = "/home/zj/workspace/my_KMS_Blog/content/posts"
INCLUDE_TAG = "blog"  # 需要提取的标签名
EXCLUDE_TAG = "draft"  # 需要排除的标签名
DATE_FORMAT = "%Y-%m-%d"  # 日期格式


def extract_tags_from_content(content):
    """
    从 Logseq Markdown 内容中提取标签。
    Logseq 的标签格式为 - #标签名 (#后面无空格才是标签，#后跟空格是标题)
    """
    tags = set()
    # 匹配 - #标签 的格式：#后面紧跟着非空格字符，但不是 ##（标题）
    # 使用负向前瞻 (?!#) 确保不是 ##
    tag_pattern = r'^\s*-\s+#(?!#)([^\s\n]+)'
    for match in re.finditer(tag_pattern, content, re.MULTILINE):
        tags.add(match.group(1).lower())
    return tags


def should_convert_file(content):
    """
    判断文件是否应该被转换。
    需要包含 blog 标签且不包含 draft 标签。
    """
    tags = extract_tags_from_content(content)
    
    # 检查是否包含要求的标签且不包含排除标签
    has_blog_tag = any(INCLUDE_TAG in tag for tag in tags)
    has_draft_tag = any(EXCLUDE_TAG in tag for tag in tags)
    
    return has_blog_tag and not has_draft_tag


def get_title_from_filename(filename):
    """
    从文件名获取标题。
    """
    # 移除 .md 扩展名
    title = filename.replace(".md", "")
    # 处理日期格式的文件名（例如 2026_04_27.md）
    title = title.replace("_", "-")
    return title


def extract_date_from_filename(filename):
    """
    从文件名中提取日期。
    支持格式：2026_04_27, 2026-04-27 等
    返回 YYYY-MM-DD 格式的日期字符串，如果无法提取则返回 None
    """
    name_without_ext = filename.replace(".md", "")
    
    # 尝试匹配 YYYY_MM_DD 或 YYYY-MM-DD 格式
    date_match = re.match(r'^(\d{4})[-_](\d{2})[-_](\d{2})', name_without_ext)
    if date_match:
        year, month, day = date_match.groups()
        return f"{year}-{month}-{day}"
    
    return None


def extract_date_from_content(content):
    """
    从笔记内容中提取日期。
    只检查前10行（Logseq 元数据通常在开头）
    支持Logseq格式：- date:: 2026-04-27 或 - created:: 2026-04-27
    返回 YYYY-MM-DD 格式的日期字符串，如果无法提取则返回 None
    """
    # 只检查前10行（避免匹配代码示例或其他内容中的日期）
    lines = content.split('\n')[:10]
    
    # Logseq 标准格式：- date:: 或 - created::
    date_pattern = r'^\s*-\s+(?:date|created)\s*::\s*(\d{4}[-/_]\d{2}[-/_]\d{2})'
    
    for line in lines:
        match = re.search(date_pattern, line, re.IGNORECASE)
        if match:
            date_str = match.group(1)
            # 标准化日期格式为 YYYY-MM-DD
            date_str = date_str.replace('_', '-')
            return date_str
    
    return None


def get_date_from_file(logseq_file_path, filename, content):
    """
    获取文件的日期。
    优先级：1. 从笔记内容中提取日期标记
           2. 从文件名提取（针对 journals 文件）
           3. 从文件修改时间获取（备用方案）
    """
    # 优先级 1：从笔记内容中提取日期
    date_from_content = extract_date_from_content(content)
    if date_from_content:
        return date_from_content
    
    # 优先级 2：从文件名提取日期
    date_from_filename = extract_date_from_filename(filename)
    if date_from_filename:
        return date_from_filename
    
    # 优先级 3：从文件修改时间获取
    file_mtime = os.path.getmtime(logseq_file_path)
    date = datetime.fromtimestamp(file_mtime).strftime(DATE_FORMAT)
    return date


def convert_logseq_to_hugo(logseq_file_path, hugo_post_dir):
    """
    将 Logseq 的 Markdown转化为 Hugo 格式。
    """
    try:
        with open(logseq_file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        print(f"❌ 无法读取文件 {logseq_file_path}: {e}")
        return False

    # 检查是否应该转换此文件
    if not should_convert_file(content):
        return False
    
    # 获取标题和日期
    filename = os.path.basename(logseq_file_path)
    title = get_title_from_filename(filename)
    
    # 从笔记内容、文件名或修改时间获取日期
    date = get_date_from_file(logseq_file_path, filename, content)
    
    # 提取标签
    tags = extract_tags_from_content(content)
    tags_str = ", ".join(sorted(tags))
    
    # 构建 Hugo 的 Front Matter
    hugo_front_matter = f"""---
title: "{title}"
date: "{date}"
tags: [{tags_str}]
---
"""
    
    # 创建 Hugo 文章
    safe_title = title.replace(" ", "-").replace("_", "-").lower()
    safe_title = re.sub(r'[^\w\-]', '', safe_title)  # 移除特殊字符
    hugo_file_path = os.path.join(hugo_post_dir, f"{safe_title}.md")
    
    # 避免覆盖已有文件
    counter = 1
    base_path = hugo_file_path
    while os.path.exists(hugo_file_path):
        name, ext = os.path.splitext(base_path)
        hugo_file_path = f"{name}-{counter}{ext}"
        counter += 1
    
    try:
        with open(hugo_file_path, "w", encoding="utf-8") as hugo_file:
            hugo_file.write(hugo_front_matter)
            hugo_file.write(content)
        print(f"✅ 已转换: {hugo_file_path}")
        return True
    except Exception as e:
        print(f"❌ 无法写入文件 {hugo_file_path}: {e}")
        return False


def main():
    """
    主函数：遍历 Logseq 的 pages 和 journals 文件夹，转换符合条件的文件。
    """
    # 确保 Hugo 目标目录存在
    os.makedirs(HUGO_CONTENT_DIR, exist_ok=True)

    # 要扫描的文件夹列表
    scan_dirs = [
        os.path.join(LOGSEQ_ROOT_DIR, "pages"),
        os.path.join(LOGSEQ_ROOT_DIR, "journals")
    ]
    
    converted_count = 0
    skipped_count = 0

    for scan_dir in scan_dirs:
        if not os.path.exists(scan_dir):
            print(f"⚠️  目录不存在: {scan_dir}")
            continue
        
        print(f"\n📂 扫描文件夹: {scan_dir}")
        
        # 遍历目录中的所有 markdown 文件
        for file in os.listdir(scan_dir):
            if file.endswith(".md"):
                logseq_file_path = os.path.join(scan_dir, file)
                if convert_logseq_to_hugo(logseq_file_path, HUGO_CONTENT_DIR):
                    converted_count += 1
                else:
                    skipped_count += 1

    # 打印统计结果
    print(f"\n" + "="*50)
    print(f"转换完成!")
    print(f"✅ 已转换: {converted_count} 篇文章")
    print(f"⏭️  已跳过: {skipped_count} 个文件 (没有 blog 标签或包含 draft 标签)")
    print(f"="*50)


if __name__ == "__main__":
    main()