### **5. Binary Distribution with PyInstaller**

**Project structure:**

```
flask_tic_tac_toe/
│
└── app.py
```

#### **Complete the Steps**

Generate a binary using `PyInstaller`:

1. Install PyInstaller:

   ```
   pip install pyinstaller
   ```

2. Run:

   ```
   pyinstaller --onefile flask_tic_tac_toe/app.py
   ```

3. The executable will be created in the `dist/` folder.

4. Install PyInstaller using `pip install pyinstaller`.
5. Build the binary with `pyinstaller --onefile flask_tic_tac_toe/app.py`.
6. Run the generated binary from the `dist/` folder.
   To **run the generated binary** from the `dist/` folder after using **PyInstaller** to create the executable, follow these steps:

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
     ```bash
     ./app
     ```
