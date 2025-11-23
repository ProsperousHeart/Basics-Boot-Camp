# Makefile & Windows Setup

This document explains what a `Makefile` is, why we added one to this repository, and how to use it on Windows systems. It includes multiple setup options (WSL, Chocolatey, and MSYS2) and `cmd.exe` commands you can copy.

## Why we added a `Makefile`

- The repository's CI workflow (`.github/workflows/ci.yml`) runs `make lint` on an Ubuntu runner. When no `Makefile` exists, the job fails with:

  ```text
  make: *** No rule to make target 'lint'.  Stop.
  ```

- Adding a small `Makefile` provides a single place to define common developer tasks used by CI and contributors (linting, formatting, running tests, installing dev dependencies).

## What this Makefile contains

- `install-dev` — installs pip requirements and common dev tools (`flake8`, `black`, `pytest`).
- `lint` — runs `flake8` and `black --check` (this is what CI calls).
- `format` — runs `black` to automatically format code.
- `test` — runs `pytest`.
- `help` — prints available targets.

The Makefile is intentionally minimal so it works in CI and for local development. If your project layout differs (for example you don't have `src/` or `test/`), adjust the `black` paths or use `black .`.

## Windows Setup Options (choose one)

### 1) Recommended — Use WSL (Windows Subsystem for Linux)

WSL gives you a native Linux environment where `make` behaves exactly as on CI. This is the most reliable option.

One-time: install WSL and Ubuntu (Windows 10/11):

```cmd
wsl --install -d Ubuntu
```

Open the Ubuntu terminal and install required packages:

```bash
sudo apt update
sudo apt install -y build-essential python3 python3-venv python3-pip make
```

Use the project from WSL (Windows drives are under `/mnt`):

```bash
cd /mnt/d/Programming/Code/Basics-Boot-Camp
make install-dev
make lint
make test
```

### 2) Chocolatey — install GNU Make on native Windows

If you prefer staying in `cmd.exe` or PowerShell, install `make` via Chocolatey (requires admin privileges).

Install Chocolatey (run in an elevated PowerShell):

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; \
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; \
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Install `make` (cmd or PowerShell):

```cmd
choco install make -y
```

Then from `cmd.exe`:

```cmd
cd D:\Programming\Code\Basics-Boot-Camp
make install-dev
make lint
```

### 3) MSYS2 / Git for Windows (advanced)

- MSYS2 provides a Unix-like environment on Windows. Install MSYS2, then in the MSYS2 shell:

```bash
pacman -Syu
pacman -S make python python-pip
```

You can then run `make` from the MSYS2 shell.

### 4) No-make alternative — run commands directly in `cmd.exe` or PowerShell

If you cannot or do not want to install `make`, run the equivalent commands manually:

```cmd
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
pip install flake8 black pytest
flake8 .
black --check src/ test/
pytest -q
```

## Tips & troubleshooting

- The CI uses `black --check src/ test/` — if your repository doesn't have `src/` or `test/`, change the Makefile to use `black --check .` or specify the correct folders.
- If `black` or `flake8` report errors, run `make format` or fix issues locally.
- The `Makefile` is safe: it only installs dependencies and runs linters/tests.

## Files added

- `Makefile` (repository root) — implements the `lint` target required by CI.
- `docs/tutorials/makefile-windows-setup.md` — this tutorial file.

## Next steps (optional)

- I can update `.github/workflows/ci.yml` to run `black --check .` instead of `black --check src/ test/` to match the repository layout, or add a small PowerShell wrapper to mimic `make` on Windows. Tell me which you'd prefer.
