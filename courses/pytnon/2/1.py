# & C:/Users/alex/AppData/Local/Programs/Python/Python37-32/python.exe d:/My/nanshannia_2/cources/devops-2/pytnon/2/1.py D:\My\nanshannia_2\cources\devops-2\pytnon\2\JSON D:\My\nanshannia_2\cources\devops-2\pytnon\2\JSON\result.json
import os, json, sys
from os import listdir
from os.path import isfile, join

def parsing_json(file):
    import_file = open(file)
    data = json.load(import_file)
    import_file.close()
    now_id = -1
    for data1 in data['matrix']:
        if data1['result'] == 0:
            if now_id < data1['id']:
                now_id = data1['id']
    for data1 in data['matrix']:
        if data1['id'] == now_id:
            res = '{"id":' + str(data1['id']) +', '+ '"number":'  +  str(data1['number']) +',' + '"committer_name":"' + str(data['committer_name']) + '",' +'"committer_email":"' + str(data['committer_email']) + '"}\n'
            with open(sys.argv[2], 'a') as file:
                file.write(res)

json_folder = sys.argv[1]
onlyfiles = [f for f in listdir(json_folder) if isfile(join(json_folder, f))]
files2 = []
for file in onlyfiles:
    file = os.path.join(json_folder, file)
    if file != sys.argv[2]:
        parsing_json(file)



    
