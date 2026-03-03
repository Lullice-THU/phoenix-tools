#!/usr/bin/env python3
"""
Phoenix Tool #2: Excel/CSV 数据处理助手
功能：批量数据清洗、格式转换、统计分析

售价: 19.9元/永久使用
"""

import pandas as pd
import json
import sys

def process_data(input_file, operation='clean'):
    """处理数据"""
    try:
        # 读取文件
        if input_file.endswith('.csv'):
            df = pd.read_csv(input_file)
        elif input_file.endswith('.xlsx'):
            df = pd.read_excel(input_file)
        else:
            return {'error': '不支持的文件格式'}
        
        result = {'status': 'success', 'rows': len(df)}
        
        if operation == 'clean':
            # 数据清洗
            original_rows = len(df)
            # 删除空行
            df = df.dropna(how='all')
            # 删除重复行
            df = df.drop_duplicates()
            # 填充空值
            df = df.fillna('')
            result['cleaned_rows'] = len(df)
            result['removed'] = original_rows - len(df)
            
        elif operation == 'stats':
            # 统计分析
            numeric_cols = df.select_dtypes(include=['number']).columns
            result['stats'] = {}
            for col in numeric_cols:
                result['stats'][col] = {
                    'mean': float(df[col].mean()),
                    'max': float(df[col].max()),
                    'min': float(df[col].min()),
                    'sum': float(df[col].sum())
                }
                
        elif operation == 'filter':
            # 简单过滤 - 删除包含空值的行
            df = df.dropna()
            result['filtered_rows'] = len(df)
        
        return result
        
    except Exception as e:
        return {'error': str(e)}

def demo():
    """演示"""
    print("=" * 50)
    print("📊 Excel/CSV 数据处理助手")
    print("=" * 50)
    print()
    print("功能列表：")
    print("  1. clean  - 清洗数据（去重、去空值）")
    print("  2. stats  - 统计分析（均值、最大、最小、总和）")
    print("  3. filter - 过滤数据（删除空值行）")
    print()
    print("使用方法：")
    print("  python data_processor.py input.csv clean")
    print("  python data_processor.py input.csv stats")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        result = process_data(sys.argv[1], sys.argv[2])
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        demo()
