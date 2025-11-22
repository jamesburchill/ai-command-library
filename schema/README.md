# AI Command Library Schema

This folder contains the versioned JSON Schemas that define how every command in the AI Command Library is structured. The schema keeps the library consistent, searchable, and machine friendly, while still being easy for humans to read and curate.

## Current stable schema

The current stable version is:

```
acl-command-1.0.0.json
```

This is the baseline structure used for all new commands submitted to the library. Every command JSON file must include:

```
"schema_version": "1.0.0"
```

to indicate it conforms to this version.

Direct link to the schema:
`https://aicommandlibrary.com/schema/acl-command-1.0.0.json`

## Versioning rules

ACL uses semantic versioning for schemas:

```
major.minor.patch
```

* **Major** -- breaking changes that require commands to be updated
* **Minor** -- new optional fields, extensions, or improvements that do not break existing commands
* **Patch** -- corrections, clarifications, and documentation-only updates

Each version gets its own standalone file:

```
acl-command-1.0.0.json
acl-command-1.1.0.json
acl-command-2.0.0.json
```

Older schemas are never deleted. They remain available for reference and backwards compatibility.

## Why schemas matter

The schema ensures:

* Consistent structure across all commands
* Easy validation during curation
* Machine-readable semantics for future tooling
* Predictable filenames and slugs
* A safe upgrade path as the library grows

Tools and scripts can rely on a stable schema rather than guessing field names or formats.

## How contributors interact with the schema

Contributors **do not** need to understand or work with the schema directly.
They submit prompts through a simple GitHub Issue template.

Curators take care of:

* Generating JSON
* Validating it against the schema
* Adding it to the library
* Tracking revisions over time

## How curators validate a command

Curators can validate command files using any JSON Schema validator. For example, using Python:

```sh
pip install jsonschema
```

```python
from jsonschema import validate
import json

schema = json.load(open("acl-command-1.0.0.json"))
data = json.load(open("path/to/command.json"))

validate(instance=data, schema=schema)
```

## Future expansions

Upcoming improvements may include:

* Tooling to auto-generate HTML pages from the schema
* An ACL API that accepts schema-validated submissions
* Namespaced extensions for vendors or speciality use cases
* A `response` schema to pair with the command schema
