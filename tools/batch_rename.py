#!/usr/bin/env python3
"""
Phoenix Tool #3: 批量重命名工具
支持按规则批量重命名文件

售价: ¥9.9
"""

import os
import re
import sys
from pathlib import Path

def batch_rename(files, pattern, replacement, mode='replace'):
    """
    批量重命名文件
    
    Args:
        files: 文件列表
        pattern: 匹配模式
        replacement: 替换内容
        mode: replace/sub/prefix/suffix/number
    """
    results = []
    
    for i, old_name in enumerate(files):
        new_name = old_name
        
        if mode == 'replace':
            new_name = old_name.replace(pattern, replacement)
        elif mode == 'sub':
            new_name = re.sub(pattern, replacement, old_name)
        elif mode == 'prefix':
            new_name = f"{replacement}{old_name}"
        elif mode == 'suffix':
            name, ext = os.path.splitext(old_name)
            new_name = f"{name}{replacement}{ext}"
        elif mode == 'number':
            ext = os.path.splitext(old_name)[1]
            new_name = f"{replacement}_{i+1:03d}{ext}"
        
        results.append({
            'old': old_name,
            'new': new_name,
            'changed': old_name != new_name
        })
    
    return results

def main():
    if len(sys.argv) < 2:
        print("=" * 50)
        print("📁 批量重命名工具")
        print("=" * 50)
        print()
        print("用法:")
        print("  python batch_rename.py <目录> [模式] [替换]")
        print()
        print("示例:")
        print("  python batch_rename.py ./photos prefix IMG_")
        print("  python batch_rename.py ./docs replace old new")
        print("  python batch_rename.py ./files number img")
        return
    
    directory = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else 'list'
    pattern = sys.argv[3] if len(sys.argv) > 3 else ''
    replacement = sys.argv[4] if len(sys.argv) > 4 else ''
    
    # 获取目录下的文件
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if mode == 'list':
        print(f"目录 {directory} 包含 {len(files)} 个文件:")
        for f in files[:10]:
            print(f"  - {f}")
        if len(files) > 10:
            print(f"  ... 还有 {len(files) - 10} 个文件")
        return
    
    # 执行重命名
    results = batch_rename(files, pattern, replacement, mode)
    
    print("预览:")
    print("-" * 50)
    for r in results[:20]:
        if r['changed']:
            print(f"  {r['old']} → {r['new']}")
        else:
            print(f"  {r['old']} (不变)")
    
    if len(results) > 20:
        print(f"  ... 还有 {len(results) - 20} 个文件")

if __name__ == '__main__':
    main()
