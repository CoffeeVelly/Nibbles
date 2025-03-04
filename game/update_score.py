import json
import os

def record_score(playername, score):
    file_path = 'user_data/score.json'
    
    # 加载现有的分数数据
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            scores = json.load(file)
    else:
        scores = []

    # 添加新的分数
    scores.append({'name': playername, 'score': score})

    # 对分数列表进行排序，并只保留前十名
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:10]

    # 将更新后的分数列表写回到 JSON 文件中
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(scores, file, ensure_ascii=False, indent=4)