#!/usr/bin/env python3
"""
Validate ACL command files against the acl-command-1.0.0 schema.

Usage:
    python validate-schema.py path/to/file.json
    python validate-schema.py curated/
"""

import json
import os
import sys
from jsonschema import validate, ValidationError

SCHEMA_PATH = "schema/acl-command-1.0.0.json"

def load_schema():
    with open(SCHEMA_PATH, "r") as f:
        return json.load(f)

def validate_file(schema, filepath):
    with open(filepath, "r") as f:
        try:
            data = json.load(f)
            validate(instance=data, schema=schema)
            print(f"[OK] {filepath}")
        except ValidationError as e:
            print(f"[ERROR] {filepath}")
            print(f"Validation error: {e.message}")
        except Exception as ex:
            print(f"[ERROR] Failed to read {filepath}")
            print(str(ex))

def walk_and_validate(schema, path):
    if os.path.isfile(path):
        validate_file(schema, path)
    else:
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".json"):
                    validate_file(schema, os.path.join(root, file))

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate-schema.py <file-or-directory>")
        sys.exit(1)

    target = sys.argv[1]
    schema = load_schema()
    walk_and_validate(schema, target)

if __name__ == "__main__":
    main()
