from pydantic import BaseModel


class SubjectBase(BaseModel):
    title: str
    description: str | None = None


class SubjectCreate(SubjectBase):
    pass


class Subject(SubjectBase):
    id: int
    student_id: int

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    name: str
    email: str


class StudentCreate(StudentBase):
    password: str


class Student(StudentBase):
    index: int
    subjects: list[Subject] = []

    class Config:
        orm_mode = True