import yaml
import json

with open("config.yaml", 'r') as stream:
    try:
        parsed = yaml.safe_load(stream)
        print(json.dumps(parsed, indent=4, sort_keys=True))
    except yaml.YAMLError as exc:
        print(exc)