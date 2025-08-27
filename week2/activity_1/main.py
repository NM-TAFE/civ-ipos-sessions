# a basic import
from src.greeter import greet as gt
from src.student import Student

def greet(name):
    print(name)

def main():
    # gt('John')
    student = Student('John', 20, ['Javascript', 'Python'], '10 Somewhere St. WA')
    print(student.student_id)
    student.setId(30)
    print(student.student_id)

if __name__ == '__main__':
    main()


# print(greet)
# use an alias - consider why might we do this?

    
    # def mergeUnits(self ,newUnits, oldUnits):

        
# sometimes we only want to import what we need

# create a calculator class in the module

# use the new class to return a score to a user


