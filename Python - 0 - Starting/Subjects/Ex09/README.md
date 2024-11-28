# 📦 ft_package

A lightweight Python utility package for list operations with simple, powerful functions.

## ✨ Features

- **`count_in_list`**: Quickly count occurrences of an element in a list
- **`reverse_list`**: Effortlessly reverse the order of list elements

## 🚀 Installation

Install the package using pip:

```bash
# Option 1: From wheel file
pip install ./dist/ft_package-0.0.1-py3-none-any.whl

# Option 2: From source distribution
pip install ./dist/ft_package-0.0.1.tar.gz
```

## 🔧 Usage

```python
from ft_package import count_in_list, reverse_list

# Count occurrences
count = count_in_list(["toto", "tata", "toto"], "toto")
print(count)  # Output: 2

# Reverse a list
reversed_list = reverse_list(["a", "b", "c"])
print(reversed_list)  # Output: ["c", "b", "a"]
```

## 🧪 Testing

### Run Unit Tests
```bash
python -m unittest discover tests
```

### Code Style Check
```bash
pip install flake8
flake8 ft_package/ tests/
```

## 📂 Project Structure

```
ex09/
├── ft_package/
│   ├── __init__.py
│   └── utils.py
├── tests/
│   └── test_utils.py
├── LICENSE
├── README.md
├── pyproject.toml
└── setup.py
```

## 🛠 Build & Install

```bash
# Install build dependencies
pip install --upgrade setuptools wheel build

# Build package
python -m build

# Install locally
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## 📄 License

MIT License. See `LICENSE` file for details.

## 🤝 Contributing

Pull requests are welcome! Please ensure tests pass and code follows Flake8 standards.