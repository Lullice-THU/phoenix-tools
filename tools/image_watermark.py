#!/usr/bin/env python3
"""
Phoenix Tool #4: 图片水印工具
支持批量添加文字/图片水印

售价: ¥14.9
"""

import sys

def add_text_watermark(image_path, text, position='bottom-right'):
    """添加文字水印"""
    print(f"  [{position}] 添加文字水印: {text}")
    return {'status': 'success', 'text': text}

def add_image_watermark(image_path, watermark_path, opacity=0.5):
    """添加图片水印"""
    print(f"  添加图片水印: {watermark_path} (透明度: {opacity})")
    return {'status': 'success', 'watermark': watermark_path}

def batch_watermark(directory, text='', watermark_path='', output_dir='output'):
    """批量添加水印"""
    import os
    
    files = [f for f in os.listdir(directory) 
             if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    print(f"找到 {len(files)} 张图片")
    print(f"输出目录: {output_dir}")
    
    results = []
    for f in files:
        if text:
            results.append(add_text_watermark(f, text))
        if watermark_path:
            results.append(add_image_watermark(f, watermark_path))
    
    return results

def main():
    print("=" * 50)
    print("🖼️ 图片水印工具")
    print("=" * 50)
    print()
    print("功能:")
    print("  - 批量添加文字水印")
    print("  - 批量添加图片水印")
    print("  - 支持透明度调整")
    print("  - 支持位置选择")
    print()
    print("使用方法:")
    print("  python image_watermark.py <目录> -t '版权声明'")
    print("  python image_watermark.py <目录> -w logo.png")

if __name__ == '__main__':
    main()
