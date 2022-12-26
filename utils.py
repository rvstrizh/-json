import json
from pprint import pprint

def load_candidates():
    with open('candidates.json', 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        candidates={}
        for i, j in enumerate(data):
            candidates[i+1] = j
        return candidates


load_candidates()