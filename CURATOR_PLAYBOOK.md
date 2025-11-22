# AI Command Library – Curator Playbook

Curators ensure that community submissions are high-quality, consistent, and safely structured. This playbook explains the exact steps to follow when reviewing a submission and adding it to the library.

The goal is to keep ACL clean, useful, and easy to grow over time.

---

# 1. Responsibilities of a Curator

Curators handle:

* Reviewing new submissions
* Requesting clarifications when needed
* Converting plain-language submissions into ACL JSON
* Validating files against the latest schema
* Ensuring naming, formatting, and structure are consistent
* Maintaining attribution integrity
* Moving approved files to `/curated`
* Rejecting low-value or harmful submissions
* Flagging duplicates, spam, or malicious content

Curators do **not**:

* Edit the author's intent
* Rewrite prompts beyond formatting/clarity fixes
* Change attribution
* Accept unsafe, fraudulent, or plagiarized material

---

# 2. Curator Workflow (Step-by-Step)

This is the standard workflow for each new submission.

## Step 1 — Open the submission

Go to:

```
Issues -> New submissions
```

Look for issues labeled:

```
submission
needs-review
```

## Step 2 — Quick quality checks

Before touching JSON, confirm:

* The prompt has a **clear purpose**
* The idea is **original or reasonably distinct**
* The content is **not harmful or misleading**
* The prompt is **complete** (no missing text)
* Attribution is clear (or anonymous by choice)

If anything is unclear, comment on the issue and ask for clarification.

## Step 3 — Create a slug

Use kebab-case:

```
blog-outline-generator
keyword-expander
email-tone-shifter
```

Filenames must match the slug:

```
prompts/<slug>.json   (if uncurated)
curated/<slug>.json   (when approved)
```

## Step 4 — Convert the submission to ACL JSON

Populate the fields using the schema:

```
schema_version   "1.0.0"
version          "1.0.0" (first release)
name             From submission
slug             Your generated slug
category         From submission (or best fit)
prompt           Exact text provided by contributor
inputs           Extract any {{variables}} if applicable
instructions     Optional
examples         Optional
tags             Optional
author           Contributor’s chosen credit name
copyright        Optional
license          Optional
notes            Optional
_meta:
    created_at
    updated_at
    source_issue
```

Do not rewrite the intent.
Do fix formatting, escape characters, or inconsistent spacing.

## Step 5 — Validate against the schema

Use any JSON Schema validator.

Example (Python):

```python
from jsonschema import validate
import json

schema = json.load(open("schema/v1/acl-command-1.0.0.json"))
data = json.load(open("prompts/<slug>.json"))

validate(instance=data, schema=schema)
```

If it validates, proceed.

If it fails:

* Fix the structural problem
* Or request clarification if the content is the issue

## Step 6 — Approve and move to `/curated`

Move the JSON file from:

```
/prompts -> /curated
```

Commit with a clear message:

```
Add <slug> command (v1.0.0)
```

## Step 7 — Close the submission issue

* Link to the curated file
* Thank the contributor
* Add label: `accepted`
* Remove: `needs-review`
* Close the issue

---

# 3. Updating a command (curators only)

When improving or modifying an existing command:

* Do NOT overwrite the old file.
* Increment **version**:

```
1.0.0 -> 1.0.1   minor fix  
1.0.0 -> 1.1.0   compatible improvements  
1.0.0 -> 2.0.0   breaking/major change
```

* Update:

```
_meta.updated_at
_meta.replaces
_meta.replaced_by (in previous file)
```

* Keep history intact.

---

# 4. Rejecting a submission

Reject when:

* It’s clear spam
* It’s harmful, unethical, or unsafe
* It’s copied from somewhere else without permission
* It duplicates an existing entry with no meaningful improvement
* It’s too vague to be useful
* The author declines to clarify incomplete material

Reject politely:

```
Thanks for your submission. After review, we cannot accept this command because <reason>. 
Feel free to submit an improved version in the future.
```

Label:

```
rejected
```

Close the issue.

---

# 5. Tagging conventions

Use labels to track workflow:

* `submission`
* `needs-review`
* `needs-clarification`
* `needs-formatting`
* `accepted`
* `rejected`
* `duplicate`
* `low-quality`

Curators may create new labels as needed.

---

# 6. Avoiding curator burnout

ACL scales by being simple. To avoid overload:

* Keep reviews short
* Don’t overthink formatting
* Use schema validation to do the heavy lifting
* Reject unclear submissions early
* Don’t chase perfection
* Merge improvements in future versions instead of blocking submissions

Good-enough now is better than perfect later.

---

# 7. Need help?

Curators can always open an internal issue tagged:

```
curator-discussion
```

Use it for:

* Complex decisions
* Debates about naming
* Schema updates
* Workflow changes
* Emerging concerns

ACL should stay lean and collaborative.
