# Curated Commands

This folder contains the **approved**, **validated**, and **ready-for-use** AI commands in the AI Command Library. Every JSON file here follows the official ACL schema and represents a stable version of a community-submitted prompt.

Anything in this directory is considered part of the official library.

---

## Structure

Commands are organised by category:

```
/curated
  ├─ writing/
  ├─ business/
  ├─ coding/
  ├─ creative/
  ├─ productivity/
  ├─ analysis/
  └─ systems/
```

Categories map directly to the `category` field in each command’s JSON.

Curators may add new categories as the library grows.

---

## File Naming

Each command uses a **kebab-case slug** for its filename.
It must match the `slug` value inside the JSON file.

Example:

```
slug: "blog-outline-generator"
file: /curated/writing/blog-outline-generator.json
```

This keeps the library consistent, predictable, and easy to index.

---

## What qualifies a command for this folder?

Only commands that meet all of the following criteria should appear here:

* Reviewed by a curator
* Validated against the active ACL schema
* Properly versioned (starting at `1.0.0`)
* Slug assigned and matched to file name
* Attribution confirmed
* Free of harmful, plagiarized, or low-quality content
* Cleanly formatted and machine-readable

Anything that doesn’t meet these standards stays in `/prompts` until fixed.

---

## Versioning and Updates

When a command needs changes:

* Do **not** overwrite the existing file
* Increment the `version` field
* Update `_meta.updated_at`
* Link versions via `_meta.replaces` and `_meta.replaced_by`
* Save the new version as a separate file with the same slug

Previous versions remain for history and reproducibility.

---

## Schema Compliance

All curated commands must validate against:

```
/schema/acl-command-1.0.0.json
```

Curators use standard JSON Schema tools to ensure consistency and correctness.

---

## Submissions

Users do **not** add files directly to `/curated`.
All submissions must go through the GitHub Issue form.
Curators then approve, validate, and move the final JSON here.

Submission form:
`Issues -> New Issue -> Submit a New AI Command`

---

## Goal of This Directory

The curated section is the stable, trusted, high-quality core of the AI Command Library.
It should remain:

* Clear
* Consistent
* Organised
* Easy to browse
* Future-friendly

ACL grows publicly, but curation ensures it grows cleanly.
