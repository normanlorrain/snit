from pathlib import Path
import shutil
import click
import difflib

#
# Create and manage simple backups, where files are numbered.
# Much like https://en.wikipedia.org/wiki/Versioning_file_system#Files-11_(RSX-11_and_OpenVMS)
#

_archive_dir: Path = None


def createBackupFolderName(path: Path):
    # for old,new in [(r'\\','_')]
    path = path.as_posix()
    path = path.replace("/", "_")
    path = path.replace(":", "_")
    return path


def backup(source_path: Path):
    _archive_dir.mkdir(parents=True, exist_ok=True)

    # Backups are numbered, e.g. foo.bar becomes foo.1.bar, subsequent backup creates foo.2.bar, etc
    # For each file to be archived, look for all the backups
    # Get the latest one if it exists, and check if it has changed before creating a new version.
    for source_file in source_path.iterdir():
        backups = sorted(_archive_dir.glob(f"{source_file.stem}*{source_file.suffix}"))
        if len(backups):
            with open(source_file) as current, open(backups[-1]) as latest:
                if current.readlines() == latest.readlines():
                    click.echo(f"{source_file.name}: no change")
                    continue

        version = len(backups) + 1
        suffix = f".{version}{source_file.suffix}"
        backup_name = source_file.with_suffix(suffix).name
        backupFile = _archive_dir / backup_name
        shutil.copyfile(source_file, backupFile)
        click.echo(f"{source_file.name}: saved")


def restore():
    pass


def compare():
    pass
