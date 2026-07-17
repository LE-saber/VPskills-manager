# Contributing

VPskills Manager accepts personal Skills, reviewed external Skills, registry improvements, validation changes, and documentation fixes.

## Add a Skill

1. Copy `templates/SKILL.template.md`.
2. Create `skills/<skill-name>/SKILL.md`.
3. Use lowercase letters, numbers, and single hyphens.
4. Make the frontmatter `name` match the folder.
5. Write a specific `description` that explains both capability and trigger context.
6. Add the Skill to `registry/index.json`.
7. Run:

```bash
python scripts/validate_registry.py
```

8. Test the Skill on a real task.
9. Submit a focused commit or pull request.

## External Skills

When importing or registering an external Skill:

- retain the original author and license;
- record repository, path, and ref;
- prefer an exact commit for important workflows;
- inspect all scripts and external links;
- do not mark it active until reviewed;
- document local modifications.

## Security

Never commit secrets, private keys, tokens, cookies, passwords, personal identity documents, confidential company data, or unsafe scripts without clear controls.

Skills that send, delete, publish, install, pay, expose private data, or alter systems must clearly require explicit user authorization.

## Commit style

```text
feat(skill): add <skill-name>
fix(skill): correct <problem>
docs: improve <section>
chore(registry): update metadata
```
