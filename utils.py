import json


def get_dict_from_json():
    with open('candidates.json', 'r', encoding='UTF-8') as fp:
        data = json.load(fp)
        candidates = {}
        for i in data:
            candidates[i['id']] = i
        return candidates
