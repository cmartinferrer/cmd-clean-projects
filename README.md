# 🧹 Project Cleaner

A simple and portable Python script to recursively clean up multiple development projects by deleting unwanted folders like `target`, `.idea`, and `.git`.

## ✨ Features

- Deletes:
  - `target` (build folder)
  - `.idea` (JetBrains IDE settings)
  - `.git` (version control metadata)
- Scans each project directory up to **2 levels deep**
- Supports **Windows, macOS, and Linux**
- Handles read-only permissions on Windows

## 📦 Requirements

- Python 3.6 or newer
- No external dependencies

## 🚀 Usage

### 1. Clone or download this repository

```bash
git clone https://github.com/your-username/project-cleaner.git
cd project-cleaner
```

### 2. Run the script
```bash
python clean_projects.py /path/to/your/projects
```
Replace /path/to/your/projects with the folder containing all your sub-projects.

## 📝 Example
python clean_projects.py ~/dev
This will look inside each folder in ~/dev and remove all target, .idea, and .git folders found at depth 1 or 2.

## 🧪 What it does

For each subdirectory inside your base folder, it scans:

.
├── project1/
│   ├── target/       ✅ deleted
│   └── source/
│       └── target/   ✅ deleted
├── project2/
│   └── .idea/        ✅ deleted
├── project3/
│   └── .git/         ✅ deleted

## ⚠️ Notes

The .git folder will be permanently removed. Make sure you back up anything important before running the script.
If any files are write-protected (common on Windows), the script will remove those protections and proceed.

## 🛠 License

MIT License © [cmartinferrer](https://github.com/cmartinferrer/)
