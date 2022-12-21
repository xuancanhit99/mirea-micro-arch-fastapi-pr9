from fastapi import FastAPI, HTTPException
# from students_service.app.student import Student, CreateStudentModel  # for IDE Pycharm

from app.student import Student, CreateStudentModel  # for Docker

students: list[Student] = [
    # Student("0", "Xuan Canh", "23", "95", "100", "99"),
    # Student("1", "Hoang Anh", "25", "100", "98", "70")
]


def add_student(context: CreateStudentModel):
    id_ = len(students)
    students.append(Student(
        id_,
        context.name,
        context.age,
        context.math,
        context.literature,
        context.english))
    return id_


app = FastAPI()


@app.get("/v1/stu")
async def get_stu():
    return students


@app.post("/v1/stu")
async def add_stu(content: CreateStudentModel):
    add_student(content)
    return students[-1]


@app.get("/v1/stu/{id_}")
async def get_stu_by_id(id_: str):
    result = [item for item in students if item.id == id_]
    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code=404, detail="Student not found")


@app.get("/__health")
async def check_service():
    return
