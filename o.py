from pathlib import Path


current_dir = Path('.')
for el in current_dir.glob('*.txt'):
    print(el)

print(Path.cwd())

