import json

with open('data.json', 'r') as f:
		init_movie = json.load(f)
t = init_movie['1']

print(t['Title'])