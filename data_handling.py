import json

def read_data(data_file_path):
    with open(data_file_path,'r') as file:
        data=json.load(file)
    return data

def write_data(data,data_file_path):
    with open(data_file_path,'w') as file:
        json.dump(data,file,indent=2)
