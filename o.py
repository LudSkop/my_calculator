# Створення директорій за допомогою pathlib.
from pathlib import Path

new_dir = Path('hello')
new_dir.mkdir(exist_ok=True)
new_dir.rmdir()
new_dir = Path('Hello/World/Test')
new_dir.mkdir(exist_ok=True, parents=True)