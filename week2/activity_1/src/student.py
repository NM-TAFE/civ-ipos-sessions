class Student:
    def __init__(self, name, student_id, units, address):
        self.name = name
        self.student_id = student_id
        self.units = units
        self.address = address

    def getId(self):
        return self.student_id
    
    def setId(self, newId):
        self.student_id = newId
    
    def getUnits(self):
        for unit in self.units:
            print(unit)

    def setUnits(self, newUnits):
        return newUnits