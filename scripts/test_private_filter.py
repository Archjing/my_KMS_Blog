#!/usr/bin/env python3
"""
测试 #private 块过滤功能
"""
import re
from pathlib import Path

def get_indent_level(line):
    """获取一行的缩进级别。"""
    if not line:
        return -1
    count = 0
    for char in line:
        if char == ' ':
            count += 1
        elif char == '\t':
            count += 4
        else:
            break
    return count


def filter_private_blocks(content):
    """过滤掉包含 #private 标签的 block。"""
    lines = content.split('\n')
    result_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        if '#private' in line.lower():
            current_indent = get_indent_level(line)
            i += 1
            
            while i < len(lines):
                next_line = lines[i]
                if next_line.strip() == '':
                    i += 1
                    continue
                
                next_indent = get_indent_level(next_line)
                if next_indent <= current_indent:
                    break
                i += 1
        else:
            result_lines.append(line)
            i += 1
    
    return '\n'.join(result_lines)


# 测试用例
test_content = """- #Blog
  - 这是一个公开的块
    - 这是子块
  - #private 这是一个私有的块
    - 私有块的子块1
    - 私有块的子块2
  - 这是另一个公开的块
    - 公开块的子块
    - #private 嵌套的私有块
      - 嵌套私有块的子块
    - 还是公开的子块
  - #PRIVATE 大写的私有块
    - 私有块内容
  - 最后一个公开块"""

print("原始内容:")
print("=" * 50)
print(test_content)
print("\n" + "=" * 50)
print("过滤后的内容:")
print("=" * 50)
filtered = filter_private_blocks(test_content)
print(filtered)
print("\n" + "=" * 50)
print("✅ 测试完成")
