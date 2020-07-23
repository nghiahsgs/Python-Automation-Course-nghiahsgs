import json

# doc file
# data=""
# with open('data.json') as file_name:
#     data=json.load(file_name)

# ghi file  dict=> file
data={}
data['users']=[]
data['users'].append({"id":0, 'name': 'nguyen', 'age':20})
data['users'].append({"id":1, 'name': 'ba', 'age':21})
data['users'].append({"id":2, 'name': 'nghia', 'age':22})

with open('data.json','w') as file_json:
    json.dump(data,file_json)


