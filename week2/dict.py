students = {
    "ajay":{
            "house":"house1",
            "patronous":"p1"
            },
    "vijay":{
            "house":"house2",
            "patronous":"p2"
            },
    "dijay":{
            "house":"house3",
            "patronous":"p3"
            },
}

for student in students:
    print(student, students[student]["house"], students[student]["patronous"])