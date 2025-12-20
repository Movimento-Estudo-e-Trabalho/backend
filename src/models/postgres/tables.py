# Definições do banco de dados

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional
from typing import List
from sqlalchemy import JSON
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import Enum


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "api"}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True)
    cpf: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=False)

    def to_domain(self):
        return {"id": self.id, "name": self.name, "cpf": self.cpf, "phone": self.phone}
