from fastapi import FastAPI, HTTPException
# from students_service.app.student import Student, CreateStudentModel  # for IDE Pycharm

from app.student import Student, CreateStudentModel  # for Docker
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

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

##########
# Jaeger
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

resource = Resource(attributes={
    SERVICE_NAME: "stu-service"
})

jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(jaeger_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

FastAPIInstrumentor.instrument_app(app)

#
##########

##########
# Prometheus

from prometheus_fastapi_instrumentator import Instrumentator


@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)


#
##########


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
