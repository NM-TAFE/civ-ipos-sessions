Create a Queue data structure following the **First In, First Out (FIFO)** principle,
i.e. the first item added to the queue is the first to be removed.

1. **Create a new Python file:**

   - Create a new Python file and name it `queue.py`.

2. **Define the `Queue` class:**

   - Write a class called `Queue`.
   - Add an `__init__` method that initialises an empty list to represent the queue.

3. **Add the `enqueue` method:**

   - Write an `enqueue` method that takes an item as an argument and appends it to the queue.

4. **Add the `dequeue` method:**

   - Write a `dequeue` method that removes and returns the first item from the queue.
   - Before removing, check if the queue is empty using the `is_empty` method.
   - If the queue is empty, return `None`.

5. **Add the `peek` method:**

   - Write a `peek` method that returns the first item in the queue without removing it.
   - Ensure it handles the case when the queue is empty.

6. **Add the `is_empty` method:**

   - Write an `is_empty` method that returns `True` if the queue is empty, otherwise `False`.

7. **Test your Queue implementation:**
   - At the end of your file, create an instance of the `Queue` class.
   - Add some items using the `enqueue` method.
   - Remove and print items using the `dequeue` method.
