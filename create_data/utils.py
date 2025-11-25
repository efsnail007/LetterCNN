import shutil
import random
from pathlib import Path

# исходные папки
source_dirs = {
    "p": "p",    # папка с файлами буквы п
    "t": "t",    # папка с файлами буквы т
    "sh": "sh"   # папка с файлами буквы ш
}

# куда сохраняем
base_out = Path("../data")
train_out = base_out / "train"
test_out = base_out / "test"

# создаём структуру
for split in [train_out, test_out]:
    for cls in source_dirs.keys():
        (split / cls).mkdir(parents=True, exist_ok=True)

# пропорции
train_ratio = 0.8

for cls, src in source_dirs.items():
    src_path = Path(src)
    files = [f for f in src_path.glob("*.png")]

    # перемешиваем
    random.shuffle(files)

    # делим
    train_count = int(len(files) * train_ratio)
    train_files = files[:train_count]
    test_files = files[train_count:]

    # копирование файлов
    for f in train_files:
        shutil.copy(f, train_out / cls / f.name)

    for f in test_files:
        shutil.copy(f, test_out / cls / f.name)

    print(f"{cls}: train={len(train_files)}, test={len(test_files)}")

print("Готово. Теперь хотя бы есть шанс, что сеть чему-то научится.")
