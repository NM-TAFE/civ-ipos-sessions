### **2. Managing Dependencies with `requirements.txt`**

```
flask_tic_tac_toe/
│
├── flask_tic_tac_toe/
│   ├── __init__.py
│   └── app.py
│   └── templates/
│     └── index.html
└── requirements.txt
```

**`requirements.txt`:**

```txt
flask
```

#### **Complete the Steps**

The following steps will install the dependencies and run the app:

1. Create the virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate
   ```

2. Install the dependencies:

   ```python
   pip install -r requirements.txt
   ```

3. Run the Flask app:

   ```python
   python -m flask_tic_tac_toe.app

   ```
