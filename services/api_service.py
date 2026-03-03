#!/usr/bin/env python3
"""
Phoenix MVP - 自动化数据处理服务
提供: 批量文本处理、格式转换、数据清洗服务

定价:
- 免费版: 100条/天
- 付费版: 9.9元/月，无限次

目标: 快速变现100元
"""

import json
import time
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# 简单存储
users = {}  # user_id -> {usage_today, last_date, paid}

def get_usage(user_id):
    today = datetime.now().date().isoformat()
    if user_id not in users:
        users[user_id] = {'usage_today': 0, 'last_date': today, 'paid': False}
    elif users[user_id]['last_date'] != today:
        users[user_id]['usage_today'] = 0
        users[user_id]['last_date'] = today
    return users[user_id]

@app.route('/api/process', methods=['POST'])
def process():
    user_id = request.headers.get('X-User-ID', 'anonymous')
    data = request.json
    
    usage = get_usage(user_id)
    
    # 检查限额
    if not usage['paid'] and usage['usage_today'] >= 100:
        return jsonify({'error': '免费额度已用完，请付费升级'}), 403
    
    # 处理类型
    process_type = data.get('type', 'text_clean')
    content = data.get('content', '')
    
    result = {'processed': content, 'type': process_type}
    
    if process_type == 'text_clean':
        # 简单文本清洗
        result['processed'] = content.strip()
    elif process_type == 'json_format':
        # JSON格式化
        try:
            parsed = json.loads(content)
            result['processed'] = json.dumps(parsed, indent=2, ensure_ascii=False)
        except:
            result['error'] = 'Invalid JSON'
    elif process_type == 'csv_to_json':
        # CSV转JSON
        lines = content.strip().split('\n')
        if lines:
            headers = lines[0].split(',')
            result['processed'] = []
            for line in lines[1:]:
                values = line.split(',')
                obj = dict(zip(headers, values))
                result['processed'].append(obj)
            result['processed'] = json.dumps(result['processed'], ensure_ascii=False)
    
    # 更新使用量
    usage['usage_today'] += 1
    
    return jsonify(result)

@app.route('/api/upgrade', methods=['POST'])
def upgrade():
    """升级接口 - 模拟支付"""
    user_id = request.headers.get('X-User-ID', 'anonymous')
    # 这里集成真实支付接口
    users[user_id]['paid'] = True
    return jsonify({'status': 'upgraded', 'message': '升级成功!'})

@app.route('/api/usage', methods=['GET'])
def usage():
    user_id = request.headers.get('X-User-ID', 'anonymous')
    u = get_usage(user_id)
    return jsonify({
        'usage_today': u['usage_today'],
        'paid': u['paid'],
        'limit': 'unlimited' if u['paid'] else 100
    })

if __name__ == '__main__':
    print("🚀 Phoenix API Service Starting...")
    print("免费额度: 100条/天")
    print("付费版: 9.9元/月")
    app.run(host='0.0.0.0', port=5001, debug=False)
