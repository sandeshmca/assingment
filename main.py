import json

f = open('data.json')
data = json.load(f)


list_data = list(data.keys())
length_data = len(list_data)

weekly_cost_of_each_paper = {}
weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for i in range(length_data):
    temp = 0
    for j in weeks:
        temp += data[list_data[i]][j]
    weekly_cost_of_each_paper[list_data[i]] = temp


n = int(input())
res = []
for i in range(length_data):
    for j in range(i + 1, length_data):
        if weekly_cost_of_each_paper[list_data[i]] + weekly_cost_of_each_paper[list_data[j]] < n:
            ans = """{\"""" + list_data[i] + """\",\"""" + list_data[j] + """\"}"""
            print(ans, end=' ')


