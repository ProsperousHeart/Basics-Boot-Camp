# Git Hooks: Preventing Pipeline Failures with Pre-Push Validation

This tutorial explains how to use Git hooks to catch errors locally before pushing code, preventing CI/CD pipeline failures and saving time in the development workflow.

## What Are Git Hooks?

Git hooks are **scripts that Git automatically executes** before or after certain events such as commit, push, or merge. They allow you to:

- Run automated checks before code leaves your local machine
- Enforce code quality standards
- Prevent broken code from reaching the remote repository
- Save CI/CD pipeline minutes and reduce feedback loops

!!! info "Git Hooks vs. MkDocs Hooks"
    Don't confuse **Git hooks** (scripts that run during Git operations) with **MkDocs hooks** (Python functions that run during documentation builds). See [MkDocs Hooks and JupyterLite Images](mkdocs-hooks-and-jupyterlite-images.md) for details about MkDocs hooks.

### Common Git Hook Types

| Hook Name | When It Runs | Common Use Cases |
|-----------|--------------|------------------|
| `pre-commit` | Before a commit is created | Lint code, format check, run quick tests |
| `commit-msg` | After commit message is entered | Validate commit message format |
| `pre-push` | Before pushing to remote | Run builds, comprehensive tests, validate deployability |
| `post-merge` | After a merge completes | Update dependencies, rebuild assets |

## Why Use Pre-Push Hooks?

### The Problem: Delayed Feedback

Without pre-push validation:

```
┌──────────┐       ┌───────────┐      ┌────────┐      ┌─────────────┐
│Developer │       │ Local Git │      │ GitHub │      │ CI Pipeline │
└─────┬────┘       └─────┬─────┘      └───┬────┘      └──────┬──────┘
      │                  │                │                  │
      │ 1. git commit    │                │                  │
      ├─────────────────>│                │                  │
      │                  │                │                  │
      │ 2. git push      │                │                  │
      ├─────────────────>│                │                  │
      │                  │ 3. Push code   │                  │
      │                  ├───────────────>│                  │
      │                  │                │ 4. Trigger build │
      │                  │                ├─────────────────>│
      │                  │                │                  │
      │                  │                │   Build runs     │
      │                  │                │   (2-10 minutes) │
      │                  │                │                  │
      │                  │ 5. ❌ Build failed!               │
      │ <────────────────┴────────────────┴──────────────────┤
      │                                                      │
      │ 😞 Wasted 5-20 minutes waiting for CI...             │
      │                                                      │
      │ 6. Fix, commit, push again                           │
      ├─────────────────────────────────────────────────────>│
      │                                                      │
      │                  Build runs again (2-10 minutes)     │
      │                                                      │
      │ 7. ✅ Success (finally!)                             │
      │ <──────────────────────────────────────────────────┤│
      │                                                      │
```

??? note "View Interactive Sequence Diagram"
    ```mermaid
    sequenceDiagram
        participant Dev as Developer
        participant Git as Local Git
        participant GH as GitHub
        participant CI as CI Pipeline

        Dev->>Git: git commit
        Dev->>Git: git push
        Git->>GH: Push code
        GH->>CI: Trigger pipeline
        Note over CI: Build runs (2-10 min)
        CI->>Dev: ❌ Build failed!
        Note over Dev: 😞 Wasted 5-20 minutes
        Dev->>Git: Fix, commit, push
        Git->>GH: Push again
        GH->>CI: Trigger pipeline again
        Note over CI: Build runs (2-10 min)
        CI->>Dev: ✅ Success (finally)
    ```

**Time wasted:** 5-20+ minutes per iteration

### The Solution: Pre-Push Validation

With a pre-push hook:

```
┌──────────┐     ┌─────────────┐    ┌───────────┐    ┌────────┐    ┌─────────────┐
│Developer │     │ Pre-Push    │    │ Local Git │    │ GitHub │    │ CI Pipeline │
│          │     │ Hook        │    │           │    │        │    │             │
└─────┬────┘     └──────┬──────┘    └─────┬─────┘    └───┬────┘    └──────┬──────┘
      │                 │                 │              │                │
      │ 1. git commit   │                 │              │                │
      ├────────────────────────────────────>             │                │
      │                 │                 │              │                │
      │ 2. git push     │                 │              │                │
      ├────────────────────────────────────>             │                │
      │                 │ 3. Run hook     │              │                │
      │                 │<────────────────┤              │                │
      │                 │                 │              │                │
      │                 │  Build check    │              │                │
      │                 │  (10-60 sec)    │              │                │
      │                 │                 │              │                │
      │ 4. ❌ Error!    │                 │              │                │
      │<────────────────┤                 │              │                │
      │                 │                 │              │                │
      │ ✅ Fix immediately (seconds, not minutes!)       │                │
      │                 │                 │              │                │
      │ 5. git commit & push again        │              │                │
      ├────────────────────────────────────>             │                │
      │                 │ 6. Run hook     │              │                │
      │                 │<────────────────┤              │                │
      │                 │  Build check    │              │                │
      │                 │  (10-60 sec)    │              │                │
      │                 │                 │              │                │
      │ 7. ✅ Passed!   │                 │              │                │
      │<────────────────┤                 │              │                │
      │                 │                 │ 8. Push code │                │
      │                 │                 ├─────────────>│                │
      │                 │                 │              │ 9. Trigger CI  │
      │                 │                 │              ├───────────────>│
      │                 │                 │              │                │
      │ 10. ✅ CI Success (first try!)    │              │                │
      │ <──────────────────────────────────┴──────────────┴────────────────┤
      │                 │                 │              │                │
```

??? note "View Interactive Sequence Diagram"
    ```mermaid
    sequenceDiagram
        participant Dev as Developer
        participant Hook as Pre-Push Hook
        participant Git as Local Git
        participant GH as GitHub
        participant CI as CI Pipeline

        Dev->>Git: git commit
        Dev->>Git: git push
        Git->>Hook: Run validation
        Note over Hook: Build check (10-60 sec)
        Hook->>Dev: ❌ Error found!
        Note over Dev: Fix immediately
        Dev->>Git: Fix, commit, push
        Git->>Hook: Run validation
        Note over Hook: Build check (10-60 sec)
        Hook->>Git: ✅ Passed!
        Git->>GH: Push code
        GH->>CI: Trigger pipeline
        CI->>Dev: ✅ Success!
    ```

**Time saved:** 90% reduction in CI failures and wait time

## Real Example: MkDocs Build Validation

### The Scenario

Your GitHub Actions pipeline runs:

```yaml title=".github/workflows/deploy-mkdocs.yml"
- name: Build MkDocs site
  run: uv run mkdocs build --strict
```

If this fails in CI, you've wasted:

- Pipeline execution time
- Your own time waiting for results
- Potential embarrassment if others are watching the repo

### The Hook Solution

A pre-push hook that runs the exact same command locally:

```bash title=".git/hooks/pre-push" linenums="1"
#!/bin/bash  # (1)!

echo "Running MkDocs build validation..."
if ! uv run mkdocs build --strict; then  # (2)!
    echo "❌ MkDocs build failed! Fix errors before pushing."
    exit 1  # (3)!
fi
echo "✅ MkDocs build passed!"
```

1. **Shebang line** - Required as the first line to tell the system this is a Bash script
2. **Negated condition** - `!` means "if this command fails", so we enter the block on failure
3. **Exit code 1** - Non-zero exit code tells Git to abort the push operation

!!! success "Automatic Execution"
    Now when you `git push`, this runs **automatically** and blocks the push if it fails!

## How Git Hooks Work: Architecture

### Where Hooks Live

```
your-project/
├── .git/
│   └── hooks/              # (1)!
│       ├── pre-commit.sample
│       ├── pre-push.sample
│       ├── pre-push        # (2)!
│       └── ...
├── src/
├── docs/
└── pyproject.toml
```

1. Git hooks directory - Created automatically when you run `git init`
2. Your custom hook - Remove the `.sample` extension to activate

!!! warning "Not Version Controlled"
    Files in `.git/` are **never** committed to version control. See [Sharing Hooks with Your Team](#sharing-hooks-with-your-team) for solutions.

### Hook Execution Flow

```
                    ┌────────────────────────────┐
                    │ Developer runs: git push   │
                    └──────────────┬─────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────────┐
                    │ Hook exists at                   │
                    │ .git/hooks/pre-push?             │
                    └───────┬──────────────┬───────────┘
                            │              │
                          NO│              │YES
                            │              │
                            ▼              ▼
              ┌─────────────────────┐  ┌────────────────────┐
              │ Proceed with push   │  │ Execute hook       │
              │ immediately         │  │ script             │
              └─────────────────────┘  └─────────┬──────────┘
                                                 │
                                                 ▼
                                    ┌───────────────────────┐
                                    │ Exit code = 0?        │
                                    │ (Success?)            │
                                    └────┬──────────────┬───┘
                                         │              │
                                    YES  │              │ NO
                                         │              │
                                         ▼              ▼
                            ┌─────────────────┐  ┌──────────────────┐
                            │ ✅ Continue     │  │ ❌ BLOCK push    │
                            │ with push       │  │ Show error msg   │
                            └─────────────────┘  └──────────────────┘
```

??? note "View Interactive Flowchart"
    ```mermaid
    flowchart TD
        A[Developer runs: git push] --> B{Hook exists at<br/>.git/hooks/pre-push?}
        B -->|No| C[Proceed with push immediately]
        B -->|Yes| D[Execute hook script]
        D --> E{Exit code = 0?}
        E -->|Yes - Success| F[Continue with push]
        E -->|No - Failure| G[BLOCK push<br/>Show error message]

        style F fill:#90EE90
        style G fill:#FFB6C6
        style D fill:#87CEEB
    ```

### Exit Codes Matter

Hooks communicate success/failure through **exit codes**:

- **Exit 0:** Success → Git continues with the operation
- **Exit 1-255:** Failure → Git aborts the operation

=== "Correct ✅"

    ```bash
    if ! some_validation_command; then
        echo "❌ Validation failed"
        exit 1  # Blocks the push
    fi
    echo "✅ Validation passed"
    exit 0  # Allows the push
    ```

=== "Wrong ❌"

    ```bash
    if ! some_validation_command; then
        echo "❌ Validation failed"
        # Missing exit 1 - push will continue!
    fi
    echo "✅ Validation passed"
    ```

## Implementing Pre-Push Hooks

### Step 1: Create the Hook File

Navigate to your repository:

=== "Linux/macOS"

    ```bash
    cd /path/to/your/repository
    nano .git/hooks/pre-push
    ```

=== "Windows (Git Bash)"

    ```bash
    cd /d/path/to/your/repository
    nano .git/hooks/pre-push
    ```

=== "Windows (PowerShell)"

    ```powershell
    cd D:\path\to\your\repository
    notepad .git\hooks\pre-push
    ```

### Step 2: Write the Hook Script

For MkDocs validation:

```bash title=".git/hooks/pre-push" linenums="1"
#!/bin/bash
# ABOUTME: Pre-push hook to validate MkDocs build before pushing to remote
# ABOUTME: Prevents pipeline failures by catching build errors locally

set -e  # (1)!

echo ""
echo "🔍 Running pre-push validation..."
echo ""

# Run MkDocs build in strict mode (same as CI)
echo "📚 Building MkDocs site..."
if ! uv run mkdocs build --strict; then  # (2)!
    echo ""
    echo "❌ MkDocs build failed!"
    echo ""
    echo "Common issues:"
    echo "  • Configuration warnings (check mkdocs.yml)"
    echo "  • Invalid markdown syntax"
    echo "  • Missing files referenced in nav"
    echo "  • Plugin compatibility issues"
    echo ""
    echo "Fix the errors above and try pushing again."
    echo ""
    exit 1  # (3)!
fi

echo ""
echo "✅ All validations passed! Proceeding with push..."
echo ""

exit 0  # (4)!
```

1. **`set -e`** causes the script to exit immediately if any command fails (except in if conditions)
2. **Exact CI command** - Run the identical command that runs in your GitHub Actions workflow
3. **Exit 1** blocks the push when validation fails
4. **Exit 0** allows the push to proceed when validation succeeds

!!! tip "Match Your CI Exactly"
    Always use the **exact same command** that runs in your CI pipeline to ensure 100% parity between local and remote validation.

### Step 3: Make the Hook Executable

!!! warning "Required Step"
    Hooks **must** be executable or Git will silently ignore them!

=== "Linux/macOS"

    ```bash
    chmod +x .git/hooks/pre-push
    ```

=== "Windows (Git Bash)"

    ```bash
    chmod +x .git/hooks/pre-push
    ```

=== "Windows (PowerShell as Admin)"

    ```powershell
    icacls .git\hooks\pre-push /grant Everyone:RX
    ```

### Step 4: Test the Hook

Try pushing to test:

```bash
git push origin your-branch
```

You should see output like:

```
🔍 Running pre-push validation...

📚 Building MkDocs site...
INFO    -  Cleaning site directory
INFO    -  Building documentation to directory: site
INFO    -  Documentation built in 2.34 seconds

✅ All validations passed! Proceeding with push...

Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
```

??? example "Example: Intentional Failure Test"

    To test that your hook properly blocks pushes, temporarily break your `mkdocs.yml`:

    ```yaml
    # Add an invalid configuration
    invalid_key: this will cause an error
    ```

    Then try to push:

    ```bash
    $ git push origin documentation

    🔍 Running pre-push validation...

    📚 Building MkDocs site...
    WARNING -  Config value 'invalid_key': Unrecognised configuration name: invalid_key
    Aborted with 1 configuration warnings in 'strict' mode!

    ❌ MkDocs build failed!

    Fix the errors above and try pushing again.

    error: failed to push some refs to 'origin'
    ```

    Remove the invalid line and the push will succeed! ✅

## Advanced Hook Patterns

### Multiple Validation Steps

Run several checks in sequence:

```bash title=".git/hooks/pre-push" linenums="1"
#!/bin/bash
# ABOUTME: Comprehensive pre-push validation
# ABOUTME: Runs linting, tests, and build checks before allowing push

set -e

echo "🔍 Running pre-push validations..."

# Step 1: Linting
echo ""
echo "1️⃣  Running linter..."
if ! make lint; then  # (1)!
    echo "❌ Linting failed!"
    exit 1
fi

# Step 2: Unit tests
echo ""
echo "2️⃣  Running tests..."
if ! make test; then
    echo "❌ Tests failed!"
    exit 1
fi

# Step 3: MkDocs build
echo ""
echo "3️⃣  Building documentation..."
if ! uv run mkdocs build --strict; then
    echo "❌ MkDocs build failed!"
    exit 1
fi

echo ""
echo "✅ All validations passed!"
exit 0
```

1. Each validation step fails fast - if linting fails, we don't waste time running tests

!!! info "Performance Consideration"
    Each check adds time to your push. Keep total hook execution under 60 seconds for good developer experience.

### Conditional Checks (Only Changed Files)

Optimize by only checking files you've changed:

```bash title=".git/hooks/pre-push" linenums="1"
#!/bin/bash
# ABOUTME: Smart pre-push hook that only validates what changed
# ABOUTME: Checks docs only if documentation files were modified

set -e

# Get list of files changed compared to remote main branch
CHANGED_FILES=$(git diff --name-only origin/main...HEAD)  # (1)!

# Check if docs-related files changed
if echo "$CHANGED_FILES" | grep -qE "(^docs/|mkdocs\.yml)"; then  # (2)!
    echo "📚 Documentation changed, validating MkDocs build..."
    if ! uv run mkdocs build --strict; then
        echo "❌ MkDocs build failed!"
        exit 1
    fi
    echo "✅ Documentation build passed!"
else
    echo "ℹ️  No documentation changes, skipping MkDocs validation"
fi

exit 0
```

1. Compare your branch to the remote main branch to find what changed
2. Regex pattern matches files in `docs/` directory or the `mkdocs.yml` file

!!! tip "When to Use Conditional Checks"
    Use this pattern when:

    - Your validation is slow (> 30 seconds)
    - Changes to unrelated files don't affect the check
    - Your repo has multiple subsystems (docs, code, tests, etc.)

### Interactive Override (Emergency Bypass)

```bash title=".git/hooks/pre-push" linenums="1"
#!/bin/bash
# ABOUTME: Pre-push validation with emergency bypass instructions
# ABOUTME: Guides users to use --no-verify only when necessary

echo "🔍 Running pre-push validation..."

if ! uv run mkdocs build --strict; then
    echo ""
    echo "❌ MkDocs build failed!"
    echo ""
    echo "⚠️  To push anyway (NOT RECOMMENDED), use:"
    echo "    git push --no-verify"  # (1)!
    echo ""
    echo "This bypasses ALL hooks and should only be used in emergencies."
    echo ""
    exit 1
fi

echo "✅ Validation passed!"
```

1. The `--no-verify` flag skips **all** hooks for this push

!!! danger "Emergency Use Only"
    ```bash
    git push --no-verify  # Skips ALL hooks!
    ```

    Only use this when:

    - You're absolutely certain the code is safe
    - There's a critical production issue
    - The hook itself is broken (rare)

    **Never** use this to bypass failing validations without fixing them!

## Sharing Hooks with Your Team

### The Challenge

Git hooks in `.git/hooks/` are **not tracked by version control**. Each team member needs to install them manually.

```
┌─────────────────────┐                  ┌──────────────┐                  ┌─────────────────────┐
│ Developer 1         │                  │ GitHub Repo  │                  │ Developer 2         │
│ ✅ Has hook         │──── pushes ────> │              │ ──── clones ───> │ ❌ NO hook          │
│    installed        │                  │              │                  │    installed        │
└─────────────────────┘                  └──────────────┘                  └─────────────────────┘
     (Protected)                                                                 (Vulnerable)
```

??? note "View Interactive Diagram"
    ```mermaid
    flowchart LR
        A[Developer 1<br/>Has hook installed] -->|pushes| B[GitHub Repo]
        B -->|clones| C[Developer 2<br/>NO hook installed ❌]

        style A fill:#90EE90
        style C fill:#FFB6C6
    ```

### Solution 1: Tracked Hook Scripts

Store hook scripts in a tracked directory:

```
your-project/
├── .git/
│   └── hooks/           # ← Not tracked (Git internal)
├── .githooks/           # ← Tracked! ✅ Commit this!
│   ├── pre-push
│   ├── pre-commit
│   └── install.sh
├── docs/
└── pyproject.toml
```

**Install script** (`.githooks/install.sh`):

```bash title=".githooks/install.sh" linenums="1"
#!/bin/bash
# ABOUTME: Installs Git hooks from .githooks/ to .git/hooks/
# ABOUTME: Run this after cloning the repo: bash .githooks/install.sh

HOOK_DIR=".git/hooks"
SOURCE_DIR=".githooks"

echo "Installing Git hooks from $SOURCE_DIR..."

for hook in "$SOURCE_DIR"/*; do
    if [ -f "$hook" ] && [ "$(basename "$hook")" != "install.sh" ]; then  # (1)!
        hook_name=$(basename "$hook")
        cp "$hook" "$HOOK_DIR/$hook_name"
        chmod +x "$HOOK_DIR/$hook_name"
        echo "✅ Installed $hook_name"
    fi
done

echo ""
echo "✅ Git hooks installed successfully!"
echo "Hooks will now run automatically during git operations."
```

1. Skip copying the install script itself - only copy actual hook files

**Setup instructions for team** (add to README):

```markdown title="README.md"
## Development Setup

After cloning this repository, install Git hooks:

```bash
bash .githooks/install.sh
```

This installs pre-push validation that catches errors before they reach CI.
```

!!! success "Commit the Hooks"
    ```bash
    git add .githooks/
    git commit -m "Add pre-push hook for MkDocs validation"
    git push
    ```

    Now everyone who clones can run the install script!

### Solution 2: Git Config (Git 2.9+)

Configure Git to use a tracked hooks directory automatically:

```bash
# Set hooks directory for this repo
git config core.hooksPath .githooks
```

Now hooks in `.githooks/` are used **automatically** without manual installation!

**Add to project setup:**

```bash title=".githooks/pre-push" linenums="1"
#!/bin/bash
# This file is in .githooks/ and tracked by Git

echo "🔍 Running pre-push validation..."
if ! uv run mkdocs build --strict; then
    echo "❌ Build failed!"
    exit 1
fi
echo "✅ Build passed!"
```

Commit it:

```bash
git add .githooks/pre-push
git commit -m "Add pre-push hook for MkDocs validation"
```

**Team members setup:**

```bash
# After cloning
git config core.hooksPath .githooks
# Done! Hooks work automatically now
```

!!! tip "Make it Easy for Your Team"
    Add hook setup to your project documentation and onboarding checklist so new team members don't forget!

### Solution 3: Pre-Commit Framework

Use the [pre-commit](https://pre-commit.com/) framework for robust, cross-platform hook management:

**Install:**

=== "Using UV"

    ```bash
    uv add --dev pre-commit
    ```

=== "Using pip"

    ```bash
    pip install pre-commit
    ```

**Create configuration:**

```yaml title=".pre-commit-config.yaml" linenums="1"
repos:
  - repo: local
    hooks:
      - id: mkdocs-build  # (1)!
        name: MkDocs Build Validation
        entry: uv run mkdocs build --strict  # (2)!
        language: system
        pass_filenames: false  # (3)!
        stages: [push]  # (4)!
```

1. Unique ID for this hook
2. The command to run - same as your CI pipeline
3. Don't pass changed filenames to the command
4. Only run this hook on push, not commit

**Install hooks:**

```bash
pre-commit install --hook-type pre-push
```

**Commit the config:**

```bash
git add .pre-commit-config.yaml
git commit -m "Add pre-commit framework for hook management"
```

!!! success "Automatic for Everyone"
    Team members just need to run `pre-commit install --hook-type pre-push` after cloning. The framework handles platform differences automatically!

## Troubleshooting

### Hook Not Running

!!! failure "Problem: Push completes without running hook"

??? tip "Solution 1: Verify File Exists"

    ```bash
    # Check if file exists
    ls -la .git/hooks/pre-push

    # Should show something like:
    # -rwxr-xr-x  1 user  staff  423 Dec  8 10:30 .git/hooks/pre-push
    #  ^^^
    #  └── These 'x' indicate executable permission
    ```

??? tip "Solution 2: Check Executable Permission"

    === "Linux/macOS"

        ```bash
        chmod +x .git/hooks/pre-push
        ```

    === "Windows (Git Bash)"

        ```bash
        chmod +x .git/hooks/pre-push
        ```

??? tip "Solution 3: Verify Shebang Line"

    The first line **must** be:

    ```bash
    #!/bin/bash
    ```

    Or for sh compatibility:

    ```bash
    #!/bin/sh
    ```

    Common mistakes:

    - Missing shebang entirely
    - Extra spaces before `#`
    - Not on the first line

??? tip "Solution 4: Test Hook Manually"

    ```bash
    # Run the hook directly
    .git/hooks/pre-push

    # Should show output and exit with 0 or 1
    echo $?  # Shows exit code of last command
    ```

### Hook Blocks Valid Push

!!! failure "Problem: Hook fails but code is actually fine"

??? tip "Solution 1: Check Your Environment"

    ```bash
    # Verify UV is installed and accessible
    which uv
    # Should show: /path/to/uv (or C:\path\to\uv.exe on Windows)

    uv --version
    # Should show: uv 0.x.x

    # Verify dependencies are installed
    uv sync
    ```

??? tip "Solution 2: Run Validation Manually"

    ```bash
    # Run the same command the hook runs
    uv run mkdocs build --strict

    # If this fails, the issue is with your code/config, not the hook
    # If this succeeds, there's a hook environment issue
    ```

??? tip "Solution 3: Check Working Directory"

    Hooks run from the repository root. Verify:

    ```bash
    # In your hook, add debug output:
    echo "Working directory: $(pwd)"
    echo "Files here: $(ls)"
    ```

??? tip "Solution 4: Emergency Bypass"

    If you're certain the code is fine:

    ```bash
    git push --no-verify
    ```

    But investigate why the hook failed afterwards!

### Windows Line Ending Issues

!!! failure "Problem: Hook fails with `^M: bad interpreter` error"

This happens when the hook file has Windows line endings (CRLF) instead of Unix line endings (LF).

??? tip "Solution 1: Using dos2unix (Git Bash)"

    ```bash
    # Install dos2unix if needed (usually included in Git Bash)
    dos2unix .git/hooks/pre-push
    ```

??? tip "Solution 2: Using PowerShell"

    ```powershell
    (Get-Content .git\hooks\pre-push -Raw) -replace "`r`n","`n" | `
        Set-Content .git\hooks\pre-push -NoNewline
    ```

??? tip "Solution 3: Using Git Configuration"

    Configure Git to handle line endings automatically:

    ```bash
    # Set for this repo
    git config core.autocrlf false

    # Ensure .githooks/ files use LF
    echo "* text=auto" > .gitattributes
    echo ".githooks/* text eol=lf" >> .gitattributes
    git add .gitattributes
    git commit -m "Ensure hooks use LF line endings"
    ```

### Hook Shows Error But Push Continues

!!! failure "Problem: Hook prints error message but push still succeeds"

The hook is not exiting with a non-zero code!

??? tip "Solution: Add Explicit Exit"

    **Wrong ❌:**

    ```bash
    if ! uv run mkdocs build --strict; then
        echo "Error!"
        # Missing exit 1 here!
    fi
    # Script continues and returns 0 by default
    ```

    **Correct ✅:**

    ```bash
    if ! uv run mkdocs build --strict; then
        echo "Error!"
        exit 1  # This blocks the push!
    fi
    ```

    Or use `set -e` at the top:

    ```bash
    #!/bin/bash
    set -e  # Exit on any error

    uv run mkdocs build --strict
    # If this fails, script exits with non-zero automatically
    ```

## Best Practices

### 1. Keep Hooks Fast ⚡

Users will bypass slow hooks, defeating their purpose!

| Duration | User Experience |
|----------|----------------|
| < 10 seconds | Excellent - barely noticeable |
| 10-30 seconds | Good - acceptable wait time |
| 30-60 seconds | Poor - users get impatient |
| > 60 seconds | Terrible - users will bypass |

!!! tip "Speed Optimization Strategies"

    - **Run only on changed files** (see [Conditional Checks](#conditional-checks-only-changed-files))
    - **Use caching** (UV caches dependencies automatically)
    - **Move slow checks to CI only** (keep hooks for fast checks)
    - **Run checks in parallel** when possible

### 2. Provide Clear Error Messages 💬

Bad ❌:

```bash
echo "Failed"
exit 1
```

Good ✅:

```bash
echo "❌ MkDocs build failed!"
echo ""
echo "Common fixes:"
echo "  • Check mkdocs.yml for configuration errors"
echo "  • Validate markdown syntax in changed files"
echo "  • Run 'uv run mkdocs build --strict' to see details"
echo ""
echo "Need help? See: docs/tutorials/git-hooks-pre-push-validation.md"
exit 1
```

!!! success "Help Users Help Themselves"
    Good error messages include:

    - **What failed** (specific check name)
    - **Why it might have failed** (common causes)
    - **How to debug** (command to run manually)
    - **Where to get help** (documentation link)

### 3. Match CI Exactly 🎯

Run the **exact same commands** as your CI pipeline:

=== "GitHub Actions"

    ```yaml title=".github/workflows/deploy.yml"
    - name: Build MkDocs site
      run: uv run mkdocs build --strict
    ```

=== "Pre-Push Hook"

    ```bash title=".git/hooks/pre-push"
    uv run mkdocs build --strict
    ```

This ensures **100% parity** between local and remote validation.

!!! warning "Don't Use Approximations"
    ❌ Don't run `mkdocs build` locally if CI runs `mkdocs build --strict`
    ❌ Don't run tests on one Python version if CI uses another
    ✅ Match the command exactly, including all flags and options

### 4. Document Hook Requirements 📝

Add to your project README:

````markdown title="README.md"
## Development Setup

### Install Git Hooks

This project uses Git hooks to validate code before pushing.

**Install hooks:**

```bash
bash .githooks/install.sh
```

**Required tools:**

- [UV](https://docs.astral.sh/uv/) (Python package manager)
- Python 3.12+
- Make (optional, for build automation)

**What the hook does:**

- Validates MkDocs can build without errors
- Catches configuration issues before CI
- Saves time by providing immediate feedback

**Bypass in emergencies only:**

```bash
git push --no-verify  # NOT RECOMMENDED
```

This skips validation and should only be used for critical fixes.
````

### 5. Version Control Your Hooks 🗂️

Store hooks in `.githooks/` or similar and commit them:

```bash
# Create tracked hooks directory
mkdir -p .githooks

# Move hook to tracked location
mv .git/hooks/pre-push .githooks/pre-push

# Make it executable
chmod +x .githooks/pre-push

# Commit to version control
git add .githooks/pre-push
git commit -m "Add pre-push hook for MkDocs validation"

# Configure Git to use this directory
git config core.hooksPath .githooks
```

## Comparison: Hooks vs. CI-Only

| Aspect | Pre-Push Hook | CI-Only |
|--------|---------------|---------|
| **Feedback Speed** | 10-60 seconds ⚡ | 2-10+ minutes 🐌 |
| **Catch Errors** | Before push ✅ | After push ❌ |
| **CI Load** | Reduced 📉 | Higher 📈 |
| **Developer Experience** | Immediate feedback 😊 | Delayed feedback 😞 |
| **Setup Complexity** | Medium (manual install) | Low (automatic) |
| **Bypassable** | Yes (`--no-verify`) | No (authoritative) |
| **Platform Issues** | Possible (Windows/Mac differences) | Rare (standardized environment) |

!!! success "Best of Both Worlds"
    **Use both:**

    - **Pre-push hooks** for fast, common checks (lint, quick tests, build validation)
    - **CI** for comprehensive, authoritative validation (all tests, security scans, deployment)

    Hooks catch 90% of issues instantly, CI provides final authority.

## Summary

Git hooks, especially pre-push hooks, are powerful tools for:

✅ **Catching errors early** - Before they reach the remote repository
✅ **Saving time** - Immediate local feedback vs. waiting for CI
✅ **Reducing CI load** - Fewer failed pipeline runs
✅ **Enforcing standards** - Consistent validation across the team

### Quick Reference

```bash
# Create pre-push hook
nano .git/hooks/pre-push

# Make executable
chmod +x .git/hooks/pre-push

# Test hook
git push origin your-branch

# Bypass hook (emergency only!)
git push --no-verify
```

### Key Takeaways

1. **Hooks are scripts** in `.git/hooks/` that run automatically during Git operations
2. **Pre-push hooks** run before `git push` completes and can block it
3. **Exit codes matter:** 0 = success (allow), non-zero = failure (block)
4. **Share with your team** by storing hooks in a tracked directory like `.githooks/`
5. **Match CI exactly** to ensure local validation mirrors remote validation

## Next Steps

<div class="grid cards" markdown>

-   :material-hammer-wrench:{ .lg .middle } **Implement Your Hook**

    ---

    Follow the [implementation guide](#implementing-pre-push-hooks) to create a pre-push hook for your project

-   :material-test-tube:{ .lg .middle } **Test It**

    ---

    Intentionally break something and verify the hook blocks the push

-   :material-share-variant:{ .lg .middle } **Share with Team**

    ---

    Use [Solution 2: Git Config](#solution-2-git-config-git-29) or [Solution 3: Pre-Commit Framework](#solution-3-pre-commit-framework)

-   :material-book-open-variant:{ .lg .middle } **Learn More**

    ---

    Explore [advanced patterns](#advanced-hook-patterns) for conditional checks and multi-step validation

</div>

## Additional Resources

- [Git Hooks Official Documentation](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks){ target="_blank" }
- [Pre-Commit Framework](https://pre-commit.com/){ target="_blank" }
- [Atlassian Git Hooks Tutorial](https://www.atlassian.com/git/tutorials/git-hooks){ target="_blank" }
- [GitHub: Sample Git Hooks](https://github.com/git/git/tree/master/templates/hooks){ target="_blank" }

---

**Related Tutorials:**

- [Clean Code Before PR](clean-code-before-pr.md)
- [Transitioning to UV](transitioning-to-uv.md)
- [MkDocs Hooks and JupyterLite Images](mkdocs-hooks-and-jupyterlite-images.md)
