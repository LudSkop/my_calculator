from pathlib import Path


current_dir = Path('.')
for el in current_dir.glob('**/*.txt'):
    print(el)

print(Path.cwd())
print(current_dir)


tnp = Path('new.txt')
if tnp.exists():
    tnp.unlink()


