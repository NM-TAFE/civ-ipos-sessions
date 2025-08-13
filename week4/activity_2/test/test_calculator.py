import unittest
from src.calculator import add

class TestaddFunction(unittest.TestCase):

    pass
    # Types
    # int
    # act

    # float


    # complex


    # use case - whats left???
    # string
    # boolean
    # collections othe robject
    # null values

        # arrange

            # act - string
    
            # act - string
  
        # assert
        with self.assertRaises(TypeError):

            add([3,4,5], 3)
            
if __name__ == "__main__":
    unittest.main()