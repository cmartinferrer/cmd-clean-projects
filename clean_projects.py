import os
import shutil
from pathlib import Path
import stat
import sys

# Folder names to be deleted if found
FOLDERS_TO_DELETE = {"target", ".idea", ".git"}

def force_remove_readonly(func, path, exc_info):
    """
    Fixes permission issues on Windows by removing read-only attribute.
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)

def delete_unwanted_folders(base_directory: Path):
    """
    Recursively deletes unwanted folders (target, .idea, .git) up to depth 2
    within each subdirectory inside the provided base directory.
    """
    for project_dir in base_directory.iterdir():
        if not project_dir.is_dir():
            continue

        print(f"\n📁 Scanning project: {project_dir}")
        folders_deleted = 0

        for root, dirs, _ in os.walk(project_dir):
            relative_depth = Path(root).relative_to(project_dir).parts
            if len(relative_depth) > 2:
                continue  # Only check up to second-level depth

            for folder_name in list(dirs):
                if folder_name in FOLDERS_TO_DELETE:
                    folder_path = Path(root) / folder_name
                    try:
                        shutil.rmtree(folder_path, onerror=force_remove_readonly)
                        print(f"✅ Deleted: {folder_path}")
                        folders_deleted += 1
                    except Exception as e:
                        print(f"❌ Error deleting {folder_path}: {e}")

        if folders_deleted == 0:
            print("ℹ️  No matching folders found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python clean_projects.py <base_directory>")
        sys.exit(1)

    base_dir = Path(sys.argv[1]).resolve()

    if not base_dir.is_dir():
        print(f"❌ The provided path is not a directory: {base_dir}")
        sys.exit(1)

    delete_unwanted_folders(base_dir)

if __name__ == "__main__":
    main()
