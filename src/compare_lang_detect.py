import json
import os
from langdetect import detect, DetectorFactory

es_data = {}

def process_json_file(file_path):
    """Process a single file."""
    print("Processing file: {}".format(file_path))
    # Gdt file name from file path
    language_code = file_path.split('/')[-1].split('_')[0]
    # print(language_code)
    with open(file_path) as json_file:
        data = json.load(json_file)
        # print(len(data['hits']['hits']))
        for hit in data['hits']['hits']:
            # print(hit['_source']['message'])
            es_data[hit['_id']] = hit['_source']['originalText']
            detected_language = detect_language(hit['_source']['originalText'])
            if detected_language != language_code:
                print(detected_language)

def detect_language(text):
    try:
        DetectorFactory.seed = 0
        return detect(text)

    except:
        return "unknown"



def process_files_in_folder(folder_path):
    """Process all files in a folder."""
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            process_json_file(os.path.join(folder_path, file_name))

if __name__ == "__main__":
    process_files_in_folder("/Users/manavleslie/code/personal/poc/translator/output/output")
