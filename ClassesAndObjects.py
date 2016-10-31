
class Student(object):
    """
    This class will describe a MCC college students information and will including their student
    ID number, First name , Last name, and Email.
    """
id = Student()


id.student_ID = "0438872"
id.first_name = 'Steve'
id.last_name = "Jobs"
id.email = "Steve@apple.com"



print '\n'


def create_student():
    s = Student()
    s.student_ID = raw_input("Please enter student ID:  ")
    s.first_name = raw_input("Please enter student first name:  ")
    s.last_name = raw_input("Please enter students last name:  ")
    s.email = raw_input("Please enter students email address:  ")
    return s

id1 = create_student()

print ("\n\n" + id1.student_ID + " " + id1.first_name + " " + id1.last_name + " " + id1.email + "\n\n")

id2 = create_student()

print ("\n\n" + id2.student_ID + " " + id2.first_name + " " + id2.last_name + " " + id2.email + "\n\n")

id3 = create_student()

print ("\n\n" + id3.student_ID + " " + id3.first_name + " " + id3.last_name + " " + id3.email + "\n\n")


