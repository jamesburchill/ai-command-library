# Contributing to the AI Command Library

Thanks for your interest in contributing. The AI Command Library (ACL) is built on simple principles: openness, clarity, credit to creators, and a curated structure that avoids chaos. This guide explains how to contribute without needing to know Git, JSON, schemas, or anything technical.

## The simplest way to contribute

If you want to share a prompt:

1. Go to **Issues**
2. Click **New Issue**
3. Choose **Submit a New AI Command**
4. Fill out the form in plain language
5. Submit

A curator will handle the rest.

You only need a free GitHub account to participate.

## What happens after you submit

A curator will:

* Review your submission
* Convert it into the ACL JSON format
* Assign a slug and version
* Validate it against the schema
* Add it to the `/curated` directory
* Credit you as specified

If they have questions, they will comment directly on your issue.

## Guidelines for submitting prompts

To keep things consistent and useful:

* Provide a clear, descriptive title
* Explain the purpose of the prompt
* Paste the full prompt exactly as intended
* Include optional examples if you have them
* Add your credit name (or stay anonymous)

Prompts that are harmful, misleading, or abusive will not be accepted.

## How curation works

Curators maintain quality by:

* Ensuring prompts follow the schema
* Fixing formatting or structural issues
* Normalizing tone, naming, and input fields
* Adding version numbers and timestamps
* Rejecting duplicates or low-value submissions
* Ensuring attribution is correctly applied

All curated prompts live under:

```
/curated
```

They follow the schema:

```
/schema/acl-command-1.0.0.json
```

## Working with the schema (optional, for curators)

Curators and advanced contributors can validate commands locally.

Install a validator:

```sh
pip install jsonschema
```

Validate a command:

```python
from jsonschema import validate
import json

schema = json.load(open("schema/v1/acl-command-1.0.0.json"))
data = json.load(open("path/to/command.json"))

validate(instance=data, schema=schema)
```

If validation passes, the file is ready for `/curated`.

## Folder structure

```
/prompts       Raw or in-progress command files
/curated       Approved, validated commands
/schema        Versioned JSON Schemas
.github        Issue templates (including the submission form)
```

## Naming and versioning rules

Each command:

* Uses a **kebab-case slug** for its filename
* Includes a **semantic version number**
* Declares which **schema version** it conforms to
* Should be updated through new versions, not overwritten

Example filename:

```
blog-outline-generator.json
```

Example version string inside the command:

```
"version": "1.0.0"
```

## Licensing and attribution

Prompts remain the intellectual property of their authors unless they state otherwise.

Contributors may choose:

* A licence (MIT, CC-BY-4.0, etc.)
* A public name or handle for credit
* Anonymous attribution

Curators will honour the contributor's wishes exactly.

## Code of conduct

Keep it simple:

* No abuse
* No harassment
* No theft of other people's work
* No spam
* No prompt injections that cause harm or mislead users

ACL aims to be an open, public good. Treat it that way.

## Need help?

Open an Issue with your question.
You don’t need technical knowledge. Just ask.
