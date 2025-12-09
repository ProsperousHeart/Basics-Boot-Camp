**Clean Code Before PR**

Purpose: a concise guide for contributors to ensure code is clean and CI-friendly before opening a pull request.

**Quick Summary**
- **Run linters:** `py -m ruff check .` and fix with `py -m ruff check --fix .`.
- **Run tests:** `py -m pytest -q`.
- **Check for secrets:** use a secrets scanner (e.g., `detect-secrets`).
- **Verify CI expectations:** ensure the CI job for linters and tests passes locally.

**Environment setup (Windows `cmd.exe`)**
- Create a virtual environment and install dev dependencies:

```bat
py -m venv .venv
.venv\Scripts\activate
py -m pip install -U pip
py -m pip install -r requirements-dev.txt
```

If the repository uses a different environment setup (Conda, Poetry, etc.), follow that project's README first.

**Local checks to run (recommended order)**

1. Formatting & linting

   - Run Ruff to discover issues:

   ```bat
   py -m ruff check .
   ```

   - Auto-fix simple issues (where supported):

   ```bat
   py -m ruff check --fix .
   ```

   - If you use an opinionated formatter (e.g., `black`), run it too. Example:

   ```bat
   py -m black .
   ```

   - Alternatively, for projects that prefer PEP 8 autofixes, you can use `autopep8` to automatically fix many PEP8 issues (line breaks, whitespace, minor formatting):

   ```bat
   py -m pip install autopep8
   py -m autopep8 --in-place --aggressive --aggressive -r .
   ```

   - Note: `autopep8` focuses on PEP 8 style fixes. `black` is a stricter, uncompromising formatter — choose one formatting tool for the project and apply it consistently.

2. Tests

   - Run the test suite and fix failing tests locally:

   ```bat
   py -m pytest -q
   ```

   - If tests are flaky, run the failing test with `-k` or verbose flags to debug.

3. Type checking (optional, if used in the project)

   - If the project uses `mypy` or typed code, run the type checker:

   ```bat
   py -m mypy .
   ```

4. Security & secrets scanning

   - Never push secrets into source code. Run a secrets scanner before committing.

   ```bat
   py -m pip install detect-secrets
   detect-secrets scan > .secrets.baseline
   ```

   - Add and review a `.secrets.baseline` when appropriate, but NEVER commit private keys or live credentials.

   - Use `pip-audit` to check dependencies for known vulnerabilities:

   ```bat
   py -m pip install pip-audit
   py -m pip_audit
   ```

5. Crypto & certificate sanity checks

   - Follow repository crypto guidelines: avoid banned/deprecated algorithms (MD5, SHA-1, RC4, DES, 3DES, etc.). Use `AES-GCM`, `ChaCha20`, `SHA-256+` or modern algorithms.

   - If your change adds or updates certificates (PEM), verify:
     - Certificate is not expired (`notAfter`), and `notBefore` is correct.
     - Public key size is strong (RSA >= 2048 or ECDSA P-256+).
     - Signature algorithm uses SHA-2 family (not SHA-1/MD5).

   - These checks prevent immediate CI/security review failures.

**Commit hygiene**

- Keep commits small and focused (one logical change per commit).
- Write meaningful commit messages: what, why (context), and reference issue/PR if applicable.
- Squash or reorganize commits if the branch history would be noisy for reviewers.

**PR description checklist (what reviewers expect)**

- **Title:** short, descriptive (feature/bugfix scope).
- **Description:** what changed, why, and link to any issue or tests added.
- **Testing:** list commands you ran locally (linters, tests, type checks).
- **Security notes:** declare any secrets/certificates added or any change to crypto usage. If you added certificate data in code, explain why and where the real secret is stored.
- **Dependencies:** note any new runtime or dev dependency and why it is needed.

**Pre-commit hooks (recommended)**

- Using `pre-commit` is an easy way to run linters and formatters on `git commit`:

```bat
py -m pip install pre-commit
pre-commit install
pre-commit run --all-files
```

Configure `.pre-commit-config.yaml` to run `ruff`, `black`, `detect-secrets`, and tests where appropriate.

**Common CI failure causes and fixes**

- Linter failures: run `py -m ruff check --fix .` and re-check. Address remaining warnings manually.
- Test failures: run the failing tests locally and repair the code or tests. Ensure environment parity with CI (Python version, env vars).
- Secrets found: remove secrets, rotate them if already shared, and put them into secure storage (vault, CI secrets).
- Formatting diffs: run the project's formatter and re-run linting.

**Quick pre-PR checklist (copy into PR description)**

- [ ] Ran `py -m ruff check .` (and fixed autofixable issues)
- [ ] Ran `py -m pytest -q` locally and all tests pass
- [ ] Scanned for secrets (e.g., `detect-secrets`) and removed any accidental keys
- [ ] Verified no banned crypto/cert issues were introduced
- [ ] Added/update relevant docs and PR description

**Next steps for maintainers**

- Ensure CI is enforcing the same commands documented above (linters + tests). Update CI config when the developer workflow changes.
- Consider adding `pre-merge` checks in the CI to block merges until green.

---

File location: `docs/tutorials/clean-code-before-pr.md` — please open and suggest local additions or project-specific commands you'd like included.
