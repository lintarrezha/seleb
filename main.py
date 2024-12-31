import json

#followers
f = open('./data/followers_1.json')

data = json.load(f)

follower = []

for i in data:
    for j in i["string_list_data"]:
        follower.append(j["value"])
        
#following
f = open('./data/following.json')

data = json.load(f)

following = []

for i in data["relationship_following"]:
    for j in i["string_list_data"]:
        following.append(j["value"])
        
#main
seleb = []

for i in following:
    if i in follower:
        seleb.append(i)
        
for i in follower:
    if i not in seleb:
        print("https://www.instagram.com/" + i)
        