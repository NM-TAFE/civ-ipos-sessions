### **Encapsulation** (Present)

- **Definition:** Encapsulation is the concept of **bundling data (attributes) and methods** that operate on the data into a single unit (class) and restricting direct access to some details.
- **Where it's used:**
  - Attributes like `name`, `contacts` in `Organisation`, `Contact`, and `Project` are encapsulated within their respective classes.
  - Methods like `add_contact()` and `get_contacts()` **control access** to the data rather than exposing it directly.

### **Abstraction** (Present)

- **Definition:** Abstraction hides complex implementation details and **only exposes necessary features**.
- **Where it's used:**
  - The `Organisation` class **abstracts** how contacts are stored and only provides methods (`add_contact()` and `get_contacts()`) to interact with them.
  - The `Project` class **abstracts** the logic of ensuring only valid contacts (those already in an `Organisation`) are added.
  - The user interacts with high-level methods without needing to know how data is stored internally.

### 3**Inheritance** (Not Present)

- **Definition:** Inheritance allows a class to derive properties and behavior from another class (parent-child relationship).
- **Why it’s missing:**
  - None of the classes (`Organisation`, `Contact`, or `Project`) inherit from another class.
  - Each class is self-contained without extending another class.

### **Polymorphism** (Not Present)

- **Definition:** Polymorphism allows different classes to **implement the same method in different ways**.
- **Why it’s missing:**
  - There are **no overridden methods** in different classes.
  - `add_contact()` exists in both `Organisation` and `Project`, but they do not override a shared parent method (e.g., from an abstract base class).
