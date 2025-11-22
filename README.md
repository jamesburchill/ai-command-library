# AI Command Library

The AI Command Library (ACL) is a public, crowd-sourced collection of useful AI prompts. Think of it as a shared reference library for anyone who wants better results from AI systems without hunting through social feeds or buying secret prompt packs.

Everything here is open, transparent, and credited. Curators help keep things organized so it never turns into chaos.

## Why this project exists

Prompts are like recipes. They get better when shared, tested, and improved. Some people hide them behind paywalls or pretend they are magic spells. We prefer a more open approach.

This library aims to:

* Make high-quality prompts easy to find
* Give full credit to authors
* Keep the structure consistent using a simple JSON schema
* Let people contribute without being technical
* Create a stable resource that can grow over time

## How to contribute (simple method) 

You do **not** need to understand JSON, Git, or technical workflows.

Anyone can submit a prompt using GitHub Issues in plain language. No technical knowledge required.

If you have a useful AI prompt:

1. Click **Issues**
2. Click **New Issue**
3. Choose **Submit a New AI Command**
4. Fill in the form in plain language
5. Submit

A curator will turn your submission into the official ACL JSON format and add it to the library.

You only need a free GitHub account to participate.

## How to contribute (advanced method)

If you're comfortable with Git and JSON, you can also contribute directly by following the detailed guidelines in the CONTRIBUTING.md file. [Click for more details](https://github.com/jamesburchill/ai-command-library/blob/main/CONTRIBUTING.md)

## Library structure

```
/prompts            Raw contributed prompts (JSON, curated)
/curated            Approved and validated prompts
/schema             JSON schema files (versioned)
/.github            Issue templates and repo config
/docs               Documentation
/scripts            Internal helpers
/tools              Reusable utilities
```

Each prompt follows a versioned schema so the format stays stable even as ACL evolves.

## JSON schema

The schema defines how each command is structured. You do not need to interact with it directly unless you enjoy that sort of thing.

Curators use it to ensure every prompt is consistent and machine-readable.

## Versioning

The schema uses semantic versioning:

* `major.minor.patch`
* Breaking changes will trigger a major version bump
* All prompts include their schema version to ensure long-term compatibility

## Credit and licensing

The AI Command Library uses a dual-licence model to keep the project open and creator-friendly:

* MIT Licence — applies to all software code, schemas, and tooling
* CC-BY 4.0 — applies to all AI commands, prompt text, examples, and creative contributions

You may use, copy, adapt, or build on this project (including commercial use) as long as you keep attribution to the original contributors.

Full details are in [LICENSE.md](https://github.com/jamesburchill/ai-command-library/blob/main/LICENSE.md)

## Roadmap

Some possible upgrades as the project grows:

* Auto-generate HTML pages from the JSON library
* API access for developers
* A browser-friendly search interface
* A simple web form for non-GitHub submissions (optional)

The focus now is keeping things small, clean, and useful.

## Start here

To submit a prompt:
**[Submit a new Ai Command Prompt](https://github.com/jamesburchill/ai-command-library/issues/new/choose)**

To explore prompts:
Browse the `/curated` folder.

---
