from sqlalchemy.orm import Session

import models
import schemas


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.index == student_id).first()


def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def create_student(db: Session, user: schemas.StudentCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_student = models.Student(email=user.email, name=user.name, hashed_password=fake_hashed_password)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_subjects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Subject).offset(skip).limit(limit).all()


def create_student_subject(db: Session, subject: schemas.SubjectCreate, student_id: int):
    db_subject = models.Subject(**subject.dict(), student_id=student_id)
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject