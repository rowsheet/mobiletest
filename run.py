import yaml
import json

with open("dashboard.yaml", 'r') as stream:
    try:
        parsed = yaml.safe_load(stream)
        print(json.dumps(parsed, indent=1, sort_keys=False))
    except yaml.YAMLError as exc:
        print(exc)
