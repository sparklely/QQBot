import json
import yaml


def json_read(url):
    with open(url, 'r', encoding='utf-8', errors='ignore') as open_doc:
        return json.loads(open_doc.read())


def json_write(url, data):
    with open(url, 'w', encoding='utf-8', errors='ignore') as open_doc:
        open_doc.write(json.dumps(data))
        open_doc.close()


def yaml_read(url):
    with open(url, 'r', encoding='utf-8', errors='ignore') as open_doc:
        return yaml.safe_load(open_doc.read())
