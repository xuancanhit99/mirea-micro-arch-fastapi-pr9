from fastapi import FastAPI, HTTPException
# from students_service.app.student import Student # for IDE Pycharm
from app.student import Student # for Docker

students: list[Student] = [
    Student("0", "Xuan Canh", "23", "95", "100", "99"),
    Student("1", "Hoang Anh", "25", "100", "98", "70")
]


app = FastAPI()


@app.get("/v1/stu")
async def get_stu():
    return students


@app.get("/v1/stu/{id_}")
async def get_stu_by_id(id_: str):
    result = [item for item in students if item.id == id_]
    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code=404, detail="Student not found")
