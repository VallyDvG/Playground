class Student():
    
    '''Class that represents a student with a name and a grade.'''
    passing_grade=5 # Minimum grade required to pass

    def __init__(self,name:str,grade:int):
        '''Initialize Student with name and grade, and validate grade'''
        self.name=name
        self.grade=grade
        if not (1<=self.grade<=10):
            raise ValueError("Grade must be between 1 and 10")
        
    
    def has_passed(self:int) ->bool:
        '''Return True if the student's grade is equal to or above the passing grade, otherwise False'''

        if self.grade>=self.passing_grade:
            return True
        else:
            return False
    
cristi=Student("Cristi",5)
ion=Student("Ion",4)
maria=Student("Maria",8)

print(cristi.has_passed())
print(ion.has_passed())
print(maria.has_passed())