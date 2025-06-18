### **5. Binary Distribution with PyInstaller**

**Project structure:**

```
flask_tic_tac_toe/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css

```

#### **Complete the Steps**

Generate a binary using `PyInstaller`:

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Run:

   If app.py is in the root directory, you should run from the root alone:

```bash
pyinstaller --onefile flask_tic_tac_toe/app.py
```

3. The executable will be created in the `dist/` folder.

### **1. Locate the `dist/` Folder**

- **`--onefile`**: This option bundles everything into a single executable file.
- After running this command, a `dist/` folder is created in the same directory where you ran the PyInstaller command.

### **2. Navigate to the `dist/` Folder**

3. **Run the binary**:
   - On **Windows**:
     ```bash
     .\app.exe
     ```
   - On **Linux/macOS**:
     `bash
./app
`
     If your app uses templates/ or static/, those won’t be automatically bundled with PyInstaller unless you handle it.

Add a note or optional section:

## Note: If your Flask app uses templates/ or static/, you must bundle those folders using PyInstaller’s --add-data option.

Example for Linux/macOS:

```bash

pyinstaller --onefile app.py --add-data "templates:templates" --add-data "static:static"
```

```bash

pyinstaller --onefile app.py --add-data "templates;templates" --add-data "static;static"
```
