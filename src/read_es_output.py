import json
import os

es_data = {}

def process_json_file(file_path):
    """Process a single file."""
    print("Processing file: {}".format(file_path))
    with open(file_path) as json_file:
        data = json.load(json_file)
        print(len(data['hits']['hits']))
        for hit in data['hits']['hits']:
            # print(hit['_source']['message'])
            es_data[hit['_id']] = hit['_source']['originalText']
            write_content_to_id(hit['_id'], hit['_source']['originalText'])

def write_content_to_id(file_id, file_content):
    """Write the content to a file."""
    with open('output/original/' + file_id + '.txt', 'w') as f:
        f.write(file_content)

def write_keys_to_file(ids_list):
    """Write the keys to a file."""
    with open('output/keys.txt', 'w') as f:
        for key in ids_list:
            f.write(key + '\n')

def process_files_in_folder(folder_path):
    """Process all files in a folder."""
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            process_json_file(os.path.join(folder_path, file_name))

if __name__ == "__main__":
    process_files_in_folder("/Users/manavleslie/code/personal/poc/translator/output/output")
    print(len(es_data))
    print(es_data.keys())
    write_keys_to_file(es_data.keys())