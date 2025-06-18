class ConfigManager:
    # Class-level attribute to store the single instance
    _instance = None

    def __new__(my_singleton_class):
        # Check if an instance already exists
        if my_singleton_class._instance is None:
            # If not, create a new instance using the superclass's __new__ method
            my_singleton_class._instance = super().__new__(my_singleton_class)
            # Initialise a settings dictionary on the instance
            my_singleton_class._instance.settings = {}
        # Return the single shared instance
        return my_singleton_class._instance


a = ConfigManager()
b = ConfigManager()
a.settings["theme"] = "dark"
print(b.settings["theme"])  # "dark"