# Prompts

This folder contains **unapproved prompt submissions** contributed by technical users through Pull Requests. These files have *not* yet been validated, curated, or added to the official library.

If you're submitting a prompt through a PR, place your JSON file here:

```
/prompts/<slug>.json
```

## Purpose of this folder

This directory acts as the **staging area** for incoming prompts received through GitHub PRs. It keeps submissions organized and separate from the official library while they undergo review.

Prompts stored here:

* may be incomplete
* may not conform to the ACL schema
* may require edits, cleanup, or restructuring
* are waiting for curator approval

Once a submission has been reviewed and approved, maintainers will move it into:

```
/curated
```

That folder holds the official, schema-validated, production-ready AI Command Library commands.

## How submissions arrive here

There are two submission paths for contributors:

### 1. **Technical contributors (PR submission)**

* Fork the repo
* Add your prompt JSON to `/prompts`
* Validate against `acl-command-1.0.0.json`
* Submit a PR

### 2. **Non-technical contributors (Issue submission)**

* Submit via GitHub Issues
* Curators create the JSON file
* Once finalized, it goes directly into `/curated`
* `/prompts` is *not* used for Issue submissions

## Notes for contributors

* Filenames must match the `slug` field inside the JSON
* JSON must be valid and formatted
* Schema compliance is required before approval
* Curators may modify or reject submissions if needed

