Status: NORMATIVE  
Lock State: UNLOCKED  
Version: 1.0.0
Editor: Charles F. Munat

# Repository Security Policy

## Signed commits (required)

All commits contributed to this repository MUST be **signed** with a key that GitHub can mark as **Verified**.

This repository includes a CI check that verifies every commit in a pull request is `verified=true` per the GitHub API. Configure branch protection to require that check.

## How to sign commits (local)

### Option A: SSH commit signing (recommended)

1. Create an SSH key (or use an existing one) and add it to your GitHub account.
2. Configure Git to sign commits using SSH:

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
```

### Option B: GPG commit signing

1. Create/import a GPG key and add the public key to GitHub.
2. Configure Git to sign commits:

```bash
git config --global user.signingkey <YOUR_KEY_ID>
git config --global commit.gpgsign true
```

## Branch protection (required to enforce)

In GitHub repo settings:

- Require pull requests before merging
- Require status checks to pass before merging
  - Require: "Require verified commits"
- Require signed commits

Direct pushes to protected branches should be disabled.
