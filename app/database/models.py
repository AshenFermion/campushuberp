from datetime import datetime, timezone
from sqlalchemy import (
    String,
    Integer,
    ForeignKey,
    UniqueConstraint,
    DateTime,
)
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db import Base

def now():
    return datetime.now(timezone.utc)

class StudentRow(Base):
    __tablename__ = "students"

    student_id: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    department: Mapped[str] = mapped_column(String(120), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=now, onupdate=now
    )

class FacultyRow(Base):
    __tablename__ = "faculty"

    faculty_id: Mapped[str] = mapped_column(String(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    department: Mapped[str] = mapped_column(String(120), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=now, onupdate=now
    )

class CourseRow(Base):
    __tablename__ = "courses"

    course_code: Mapped[str] = mapped_column(String(20), primary_key=True)
    course_name: Mapped[str] = mapped_column(String(160), nullable=False)
    credits: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=now, onupdate=now
    )

class EnrollmentRow(Base):
    __tablename__ = "enrollments"

    enrollment_id: Mapped[str] = mapped_column(String(20), primary_key=True)
    student_id: Mapped[str] = mapped_column(
        ForeignKey("students.student_id"), nullable=False
    )
    course_code: Mapped[str] = mapped_column(
        ForeignKey("courses.course_code"), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)

    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "course_code",
            name="uq_student_course",
        ),
    )