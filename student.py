from models.student import Student
# this methord id for converting the db responce without address
def student_to_dict_without_address(student) -> dict:
    return {
        "name": student["name"],
        "age": student["age"],
    }
# This is a methord to convert the database responces to dict
def student_to_dict(student) -> dict:
    return {
        "name": student["name"],
        "age": student["age"],
        "address": dict(student["address"])
    }

# this is the methord to convert a list of database responces
def students_to_list(students):
    return [student_to_dict_without_address(student) for student in students]


# this methord for converting student model to dict for inserting it into the database
def student_model_to_dict(student : Student) -> dict:
    return {
        "name": student.name.lower(),
        "age": student.age,
        "address": {
            "city": student.address.city.lower(),
            "country": student.address.country.lower()
        }
    }