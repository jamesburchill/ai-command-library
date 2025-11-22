#!/usr/bin/env python3
"""
ACL Command Generator
Creates a skeleton JSON file conforming to the acl-command-1.0.0 schema.
This is an interactive tool for curators and contributors.
"""

import json
import datetime
import os

SCHEMA_VERSION = "1.0.0"

def prompt(msg):
    return input(msg).strip()

def main():
    print("AI Command Library - JSON Command Generator")
    print("-------------------------------------------")

    name = prompt("Command name: ")
    slug = prompt("Slug (kebab-case): ")
    category = prompt("Category: ")
    author = prompt("Author name or GitHub handle: ")
    license_choice = prompt("License (default MIT): ") or "MIT"
    model = prompt("Suggested model (optional): ")
    role = prompt("Role/system instructions (optional): ")

    print("\nPaste the main prompt text. End with a blank line:")
    prompt_lines = []
    while True:
        line = input()
        if not line:
            break
        prompt_lines.append(line)
    prompt_text = "\n".join(prompt_lines)

    print("\nList input variables (press Enter when done):")
    inputs = []
    while True:
        var = input("Variable: ").strip()
        if not var:
            break
        inputs.append(var)

    now = datetime.datetime.utcnow().isoformat() + "Z"

    data = {
        "schema_version": SCHEMA_VERSION,
        "version": "1.0.0",
        "copyright": "",
        "name": name,
        "slug": slug,
        "category": category,
        "model": model,
        "role": role,
        "prompt": prompt_text,
        "inputs": inputs,
        "instructions": [],
        "examples": [],
        "tags": [],
        "author": author,
        "license": license_choice,
        "notes": "",
        "_meta": {
            "created_at": now,
            "updated_at": now,
            "source_issue": "",
            "deprecated": False
        },
        "extensions": {}
    }

    # Output directory decision
    target_dir = f"curated/{category}"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    filename = f"{target_dir}/{slug}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"\nCommand created: {filename}")


if __name__ == "__main__":
    main()
