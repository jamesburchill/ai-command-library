# Scripts

This folder contains lightweight internal scripts used to maintain or support the AI Command Library. These scripts are intended for curators and maintainers, not end users.

Typical use cases include:

- JSON schema validation
- Prompt formatting helpers
- One-off maintenance utilities
- Conversion or cleanup scripts
- Internal tooling that does not need packaging

Scripts in this folder should be:

- Small
- Single-purpose
- Easy to run locally
- Optional for general contributors

If a script grows into a reusable tool or gains external users, it should be moved into `/tools`.
