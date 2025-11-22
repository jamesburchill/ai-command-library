# AI Command Library - Pull Request Template

Thank you for contributing to the AI Command Library.  
Please complete all sections below so curators can review your submission efficiently.

## 1. Submission Type
Select one:

- [ ] New prompt (JSON command)
- [ ] Update to an existing prompt
- [ ] Fix or improvement (metadata, formatting, slug, etc.)
- [ ] Other (explain below)

If "Other", explain here:

```
<your text>
```

## 2. Prompt Details
Provide the top-level information from your JSON file.

```
Name:
Slug:
Category:
Version:
Author:
Description:
```

## 3. File Location Confirmation
Your submitted prompt **must** be placed in:

```
/prompts/<slug>.json
```

- [ ] I confirm the JSON file is located in `/prompts`
- [ ] The filename matches the slug exactly

## 4. Schema Validation
All submitted JSON must validate against:

```
/schema/acl-command-1.0.0.json
```

- [ ] I validated the file locally
- [ ] All required fields are present
- [ ] No unknown or additional fields are included
- [ ] Version uses semantic versioning

If you used a validator script or tool, specify which one:

```
<validator used>
```

## 5. Summary of Changes

```
<your summary>
```

## 6. Prompt Purpose

```
<purpose and usage>
```

## 7. Checklist (Required)

- [ ] JSON formatted
- [ ] Slug is lowercase and hyphen-separated
- [ ] Category is valid
- [ ] Copyright included if needed
- [ ] Content is original and safe
- [ ] Permission granted to include in the library

## 8. Additional Notes

```
<any extra info for reviewers>
```
