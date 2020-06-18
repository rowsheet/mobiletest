import yaml
import json

with open("dashboard.yaml", 'r') as stream:
    try:
        parsed = yaml.safe_load(stream)
        print(json.dumps(parsed, indent=2, sort_keys=True))
    except yaml.YAMLError as exc:
        print(exc)