from pathlib import Path
import shutil

_dir: Path = None


def createFileNameFromPath(path: Path):
    # for old,new in [(r'\\','_')]
    path = path.as_posix()
    path = path.replace("/", "_")
    path = path.replace(":", "-")
    return path


def backup(path: Path):
    if not _dir.exists():
        _dir.mkdir(parents=True, exist_ok=True)

    for child in path.iterdir():
        version = 1
        backups = list(_dir.glob("*"))
        # if child.name in _dir.glob()
        suffix = f".{version}{child.suffix}"
        backupFile = _dir / (child.with_suffix(suffix).name)
        shutil.copyfile(child, backupFile)
    pass


def restore():
    pass


def compare():
    pass
