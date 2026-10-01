# 🎯 Python Safe File Organizer & Renamer
A Python script that organizes files into categorized folders based on their extensions.
**Version:** V1

## ✨ Features

- Scan the folder
- Classify files by their extensions
- Preview the organization before making changes
- Request user confirmation
- Create folders based on file categories
- Move files and handle duplicate file names
- Generate a report of the results

## ⚙️ How It Works

1. The user enters the file path.
2. The program verifies that the path exists and is a folder.
3. It categorizes the files based on their extensions.
4. It displays a preview of the changes.
5. It requests user confirmation.
6. Upon confirmation, it creates the folders, moves the files, and handles duplicate names.
7. It generates the final report.

## 📋 Requirements

- Python 3.x

## 🚀 How to Run
1. Make sure Python 3.x is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python file_organizer.py
```
5. Enter the path of the folder you want to organize when prompted.
6. Review the preview and confirm the operation.
## 📁 Project Structure
```text
python-safe-file-organizer/
├── file_organizer.py
├── README.md
└── .gitignore
```
## 🧪 Example
### Before
```text
Test/
├── photo.jpg
├── report.pdf
├── song.mp3
└── video.mp4
```
### After
```text
Test/
└── Organized_Files/
    ├── Audio/
    │   └── song.mp3
    ├── Documents/
    │   └── report.pdf
    ├── Images/
    │   └── photo.jpg
    └── Videos/
        └── video.mp4
```
## 🔮 Future Improvements

- Support organizing files inside subfolders.
- Allow the user to choose the location for the `Organized_Files` folder
