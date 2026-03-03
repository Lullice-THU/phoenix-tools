#!/usr/bin/env python3
"""
Phoenix Tool #1: 短视频文案生成器
帮助抖音/小红书创作者快速生成视频文案

售价: 9.9元/永久使用
"""

import random

TEMPLATES = {
    '开箱': {
        '开头': [
            '今天给大家带来一款{product}，真的惊艳到我了！',
            '等了这么久终于到了！{product}开箱测评！',
            '你们一直在问的{product}，今天它来了！',
        ],
        '主体': [
            '首先来看外观，{feature1}',
            '重点是这个{feature2}，实测效果太棒了',
            '再来说说使用体验，{feature3}',
        ],
        '结尾': [
            '总的来说这款{product}值得入手吗？我的答案是：真香！',
            '如果你们也想入手，链接在评论区自取~',
            '觉得有用的记得一键三连支持一下！',
        ]
    },
    '教程': {
        '开头': [
            '3分钟学会{skill}，新手也能轻松上手！',
            '今天手把手教你{skill}，收藏起来慢慢学！',
            '不会{skill}？看完这篇你就懂了！',
        ],
        '主体': [
            '第一步，{step1}',
            '第二步，注意{point1}',
            '第三步，{step2}',
        ],
        '结尾': [
            '学会了嘛？有问题评论区见~',
            '如果觉得有用，点个赞再走呗！',
            '关注我，每天分享实用技巧！',
        ]
    },
    '测评': {
        '开头': [
            '{product}深度测评一个月，这些优缺点你必须知道！',
            '买了{product}后悔了吗？真实使用感受分享！',
            '{product}到底值不值？看完这篇再做决定！',
        ],
        '主体': [
            '优点：{pro1}',
            '缺点：{con1}',
            '使用场景：{scene}',
        ],
        '结尾': [
            '综合评分7.5分，推荐指数⭐⭐⭐⭐',
            '适合人群：{target}',
            '有问题评论区问，看到都会回复！',
        ]
    }
}

def generate_script(template_type='开箱', product='', features=None):
    """生成视频文案"""
    if template_type not in TEMPLATES:
        template_type = '开箱'
    
    t = TEMPLATES[template_type]
    product = product or '产品'
    features = features or {'feature1': '质感很棒', 'feature2': '功能强大', 'feature3': '操作简单'}
    
    def fill(text):
        return text.format(
            product=product,
            skill=product,
            feature1=features.get('feature1', '很棒'),
            feature2=features.get('feature2', '好用'),
            feature3=features.get('feature3', '方便'),
            pro1=features.get('pro1', '性价比高'),
            con1=features.get('con1', '续航一般'),
            step1=features.get('step1', '打开设置'),
            step2=features.get('step2', '保存退出'),
            point1=features.get('point1', '注意保存'),
            scene=features.get('scene', '日常使用'),
            target=features.get('target', '所有人'),
        )
    
    script = {
        '开头': random.choice(t['开头']),
        '主体': '\n'.join([random.choice(t['主体']) for _ in range(3)]),
        '结尾': random.choice(t['结尾']),
    }
    
    # 填充占位符
    for key in script:
        script[key] = fill(script[key])
    
    return script

def main():
    print("=" * 50)
    print("🎬 短视频文案生成器")
    print("=" * 50)
    print()
    
    # 示例
    print("📝 示例文案（开箱类）：")
    print("-" * 30)
    script = generate_script('开箱', '无线耳机', {
        'feature1': '外观时尚，质感很好',
        'feature2': '降噪效果出色',
        'feature3': '佩戴舒适不累耳'
    })
    print(f"【开头】\n{script['开头']}\n")
    print(f"【主体】\n{script['主体']}\n")
    print(f"【结尾】\n{script['结尾']}\n")
    
    print("-" * 30)
    print("📝 示例文案（教程类）：")
    script = generate_script('教程', 'Python爬虫', {
        'step1': '安装必要的库：pip install requests',
        'point1': '注意robots.txt协议',
        'step2': '编写抓取逻辑并保存数据'
    })
    print(f"【开头】\n{script['开头']}\n")
    print(f"【主体】\n{script['主体']}\n")
    print(f"【结尾】\n{script['结尾']}")

if __name__ == '__main__':
    main()
