# 🤝 Contributing to Lily Pi

First of all — thank you for your interest in contributing!  
Lily Pi is a community project and every contribution, however small, matters.

---

## Table of Contents

1. [Code of Conduct](#1-code-of-conduct)
2. [Ways to Contribute](#2-ways-to-contribute)
3. [Development Setup](#3-development-setup)
4. [Branch & Commit Conventions](#4-branch--commit-conventions)
5. [Submitting a Pull Request](#5-submitting-a-pull-request)
6. [Hardware Contributions](#6-hardware-contributions)
7. [Documentation Contributions](#7-documentation-contributions)
8. [Reporting Bugs](#8-reporting-bugs)
9. [Feature Requests](#9-feature-requests)
10. [License](#10-license)

---

## 1. Code of Conduct

Be respectful, inclusive, and constructive. We follow the
[Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/)
code of conduct. Please report unacceptable behaviour to the maintainers via GitHub issues.

---

## 2. Ways to Contribute

| Area | What's needed |
|------|---------------|
| 🐍 Software | New sensor drivers, display modules, AI features |
| 🖨️ Hardware | 3-D printable models, wiring diagrams, BOM improvements |
| 📝 Docs | Tutorials, translations, example use-cases |
| 🐛 Bug fixes | Any reproducible bug described in an issue |
| 🧪 Tests | Unit tests for core runtime modules (`main.py`, `core/`) |
| 🎨 UI / UX | OLED layout designs, mockups |

---

## 3. Development Setup

```bash
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/<your-username>/Lily-Pi.git
cd Lily-Pi

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements-dev.txt

# 4. Run a short deterministic demo to verify your setup
python main.py --demo-seconds 10 --no-clear
```

### Coding Standards

- **Python 3.9+** — use type hints (`def foo(x: int) -> str:`)
- Follow **PEP 8** style — run `flake8 main.py core/` to check
- Use **docstrings** for all public functions and classes (Google style)
- Keep lines ≤ 100 characters

---

## 4. Branch & Commit Conventions

### Branch names

```
feat/<short-description>      # new feature
fix/<short-description>       # bug fix
docs/<short-description>      # documentation only
hardware/<short-description>  # hardware files (models, diagrams, BOM)
refactor/<short-description>  # code refactoring
```

### Commit messages (Conventional Commits)

```
feat: add MPU-6050 IMU driver
fix: correct NeoPixel colour order (RGB → GRB)
docs: expand getting-started guide with Jetson instructions
hardware: add motorcycle full-face helmet 3-D mount STL
```

---

## 5. Submitting a Pull Request

1. Create your branch from `main`:
   ```bash
   git checkout -b feat/my-feature
   ```
2. Make your changes and commit them
3. Push to your fork:
   ```bash
   git push origin feat/my-feature
   ```
4. Open a Pull Request on GitHub with:
   - A clear title following the commit convention
   - A description of **what** changed and **why**
   - Links to any related issues (`Closes #42`)
   - Screenshots / photos for hardware or UI changes

### PR Review Checklist

- [ ] Code follows PEP 8 and passes `flake8 main.py core/`
- [ ] All new functions and classes have docstrings
- [ ] Hardware additions include both `.stl` and `.step` files
- [ ] README / docs updated if applicable
- [ ] Tested on real hardware (or documented as simulation-only)

---

## 6. Hardware Contributions

When contributing 3-D models or wiring diagrams:

- Place STL/STEP files in `hardware/3d-models/`
- Place Fritzing (`.fzz`) and PDF diagrams in `hardware/wiring-diagrams/`
- Update the respective `README.md` table with your new file
- Update `hardware/bom.md` with any new components

**Naming conventions:**
```
hardware/3d-models/raspberry-pi-visor-mount.stl     # kebab-case
hardware/wiring-diagrams/oled-ssd1306-i2c.fzz
```

---

## 7. Documentation Contributions

- Docs live in `docs/` and `README.md`
- Use clear, plain English — assume the reader is a competent maker but may not be a software engineer
- Markdown only; no HTML inside `.md` files unless absolutely necessary
- Add a "Last updated" line if you significantly revise a doc

---

## 8. Reporting Bugs

Open a GitHub Issue with:

- **Title**: brief, descriptive summary
- **Environment**: OS, Python version, Pi/Jetson model, Enki AI version
- **Steps to reproduce**: numbered, minimal steps
- **Expected behaviour**
- **Actual behaviour** (include error traceback if applicable)
- **Log output**: copy from `main.py` console

---

## 9. Feature Requests

Open a GitHub Issue labelled `enhancement` with:

- A description of the problem this feature would solve
- A proposed solution (optional)
- Any relevant prior art or references

---

## 10. License

Lily Pi uses a **dual license** — see [LICENSE](../LICENSE) for the full text.

| Scope | License |
|-------|---------|
| Software (`*.py`, `*.sh`, executable source) | [GNU AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.txt) |
| Docs, hardware & images | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |

By contributing to Lily Pi, you agree that your contributions will be licensed under the
applicable license for the area you are contributing to (AGPL-3.0 for code, CC BY-SA 4.0
for documentation and hardware). You also confirm that you have the right to submit the
code or files you are contributing (no third-party intellectual property violations).

---

*Thank you for helping make Lily Pi better! 🪖*
