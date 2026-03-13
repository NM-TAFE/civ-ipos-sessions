```python
# Create a file: math_game.py
import random
a = random.randint(1,20)
b = random.randint(1,20)
print(f"What is {a} × {b}?")
```

1. **Create a venv, Install & Start IPython**  
   Open terminal → type

   ```bash
   python -m pip install IPython
   python -m IPython
   ```

2. **Tab completion**
   Type these slowly and press TAB at each •

   ```
   In [1]: import math
   In [2]: math.   → TAB # see all functions!
   In [3]: math.sq   → TAB → math.sqrt
   In [4]: math.sqrt(  → TAB shows signature: sqrt(x, /)
   In [5]: math.sqrt?
   ```

   → press **q** to exit the help

3. **? and ?? – quick help**

   ```
   len?
   len??
   sorted??
   ```

4. **Up-arrow history + reverse search**

   ```
   3+12
   "hello"*5
   print(99)
   x = [1,2,3]
   ```

   → press ↑ a few times  
   → then press **Ctrl + r** and type `pri` → it finds `print(99)`

5. **Shell commands with !**

   ```
   !pwd
   !ls -l
   !echo "Hello from bash inside Python!"
   !python -m pip list | grep numpy    # or pandas, etc.
   ```

6. **iPython Magic commands**

   | Command   | What to type                         | What students see / learn                      |
   | --------- | ------------------------------------ | ---------------------------------------------- |
   | %run      | %run greet.py                        | Runs the fileasks for name                     |
   | %run -i   | %run -i math_game.py                 | Runs it, but keeps variables afterwards        |
   | %who      | %who                                 | Lists all variables you created                |
   | %timeit   | %timeit [x**2 for x in range(10000)] | Times code – very useful later for speed tests |
   | %hist     | %hist -n 1-15                        | Shows your recent commands with numbers        |
   | %quickref | %quickref                            | Shows a cheat-sheet of all magics              |
