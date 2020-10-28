#! /usr/bin/env python3

import json
import jsonschema
import os
import sys

SCHEMA_FILENAME = 'elba_config_schema.json'
USAGE = "Usage: Input on STDIN, eg. `validate.py < /home/foo/config.json`"

def main():
    schema_path = os.path.join(os.path.dirname(__file__), SCHEMA_FILENAME)
    with open(schema_path, 'r') as schema_file:
        schema = json.loads(schema_file.read())
    if sys.stdin.isatty():
        print("Input must be non-empty", USAGE, sep="\n", file=sys.stderr)
        sys.exit(1)
    input_json = json.loads(sys.stdin.read())
    jsonschema.validate(input_json, schema)
    print("Elba config JSON is valid", file=sys.stderr)

if __name__ == '__main__':
    if len(sys.argv)>1:
        print(USAGE, file=sys.stderr)
        sys.exit(1)
    main()
