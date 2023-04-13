class Student:
    def __init__(self, f_name, l_name, s_id, address):
        self.first_name = f_name
        self.last_name = l_name
        self.student_id = s_id
        self.student_address = address
    def __str__(self):
        return "Student's name:\n" + self.first_name + " " + self.last_name + "\n" + "Student's ID:\n" + str(self.student_id) + " \nStudent's Address:\n" + str(self.student_address)

mystudent = Student('Mohamad', 'Elwan', 903182, "865 North County St")
print(mystudent)