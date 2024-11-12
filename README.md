# 42-Python-Piscine
Learning Python For Data Science

**These tasks wants us to use Python 3.10 spesifically, so our first initial step to arrange it out.**

<details>
<summary>🐍 Getting Started with Python 3.10</summary>

> A comprehensive guide to setting up Python 3.10 across different environments and platforms.

## 📑 Table of Contents

- [🚀 Quick Start Options](#-quick-start-options)
- [1. 🎯 Python Version Chooser](#1--python-version-chooser-for-the-multi-python-masters)
- [2. 🛡️ Virtual Environment Superhero](#2-️-virtual-environment-superhero-for-project-isolation)
  - [Setup Steps](#setup-steps)
  - [Platform-Specific Commands](#platform-specific-commands)
- [3. 🔄 pyenv: Version Juggler](#3--pyenv-the-python-version-juggler)
  - [Installation Steps](#installation-steps)
  - [Version Management](#version-management)
- [4. 🐼 conda: Environment Guru](#4--conda-the-environment-management-guru)
- [5. 🎯 Full Path Fury](#5--full-path-fury-for-the-python-path-pro)
- [6. 🐋 Docker: Isolation Mastermind](#6--docker-the-isolation-mastermind)

## 🚀 Quick Start Options

Choose the setup method that best matches your development style and requirements:

| Method | Best For | Complexity | Isolation |
|--------|----------|------------|-----------|
| Python Version Chooser | Quick starts | Low | None |
| Virtual Environment | Project isolation | Low | High |
| pyenv | Version management | Medium | Medium |
| conda | Data science projects | Medium | High |
| Full Path | System control | Low | None |
| Docker | Production deployment | High | Complete |

## 1. 🎯 Python Version Chooser (For the Multi-Python Masters)

Got multiple Python versions on your system? Simply point the command line at Python 3.10 directly:

```bash
python3.10 script.py
```

> 💡 **Pro Tip:** This assumes Python 3.10 is installed and accessible with the `python3.10` command.

## 2. 🛡️ Virtual Environment Superhero (For Project Isolation)

Virtual environments create isolated spaces for your project's dependencies, keeping things clean and separate from other projects.

### Setup Steps

Create your virtual environment:
```bash
python3.10 -m venv myenv
```

### Platform-Specific Commands

<details>
<summary>🖥️ macOS/Linux</summary>

```bash
source myenv/bin/activate
```
</details>

<details>
<summary>🪟 Windows</summary>

```bash
myenv\Scripts\activate
```
</details>

<details>
<summary>🔄 Deactivation (All Platforms)</summary>

```bash
deactivate
```
</details>

## 3. 🔄 pyenv: The Python Version Juggler

pyenv lets you install and switch between multiple Python versions with ease.

### Installation Steps

1. Install pyenv (follow their [installation instructions](https://github.com/pyenv/pyenv#installation))
2. Install Python 3.10:
   ```bash
   pyenv install 3.10.0
   ```

### Version Management

Set Python 3.10 as default:

```bash
# 🌍 Globally (system-wide)
pyenv global 3.10.0

# 📁 Locally (project-specific)
pyenv local 3.10.0

# ✅ Verify installation
python --version  # Should show Python 3.10.0
```

## 4. 🐼 conda: The Environment Management Guru

For Anaconda/Miniconda users, conda provides excellent environment management:

```bash
# 🏗️ Create environment
conda create -n myenv python=3.10

# ▶️ Activate environment
conda activate myenv

# ⏹️ Deactivate when finished
conda deactivate
```

## 5. 🎯 Full Path Fury (For the Python Path Pro)

For direct system path access:

```bash
# 🔍 Find Python 3.10 path
which python3.10

# 🎯 Run with full path
/path/to/python3.10 script.py
```

## 6. 🐋 Docker: The Isolation Mastermind

Create a complete isolated environment with Docker:

1. Create `Dockerfile`:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "script.py"]
```

2. Build and run:
```bash
# 🏗️ Build container
docker build -t my-python-app .

# 🚀 Run container
docker run my-python-app
```

---

<div align="center">

### 🛠️ Need Help?

| Resource | Link |
|----------|------|
| Python Docs | [python.org](https://docs.python.org/3.10/) |
| Virtual Environments | [Python Guide](https://docs.python.org/3/tutorial/venv.html) |
| pyenv | [GitHub](https://github.com/pyenv/pyenv) |
| Docker | [Docs](https://docs.docker.com/) |

</div>

---

<div align="center">

📝 Feel free to open an issue if you need help or find a bug!

⭐ Don't forget to star this repo if you found it helpful!

</div></details>
