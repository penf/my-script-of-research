import json
path = "D:\\android_malware\\api.txt"
with open(path, "r") as f:
    content = json.load(f)
print(len(content))
res = {}
res_name ={}
i = 0

for k,v in content.items():
    res_name[k] = i
    for api in v:
        res[api] = i
    i += 1

with open('d:\\apis.json','w') as f:
    f.write(json.dumps(res))

with open('d:\\apis_index.json','w') as f:
    f.write(json.dumps(res_name))
