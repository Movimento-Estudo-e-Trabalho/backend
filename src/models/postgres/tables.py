# Definições do banco de dados

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional, List
from sqlalchemy import Enum, JSON, ForeignKey
from sqlalchemy.ext.mutable import MutableList

class Base(DeclarativeBase):
    ...
    
class Companies(Base):
    __tablename__ = "companies"
    __table_args__ = {"schema": "api"}

    id: Mapped[str] = mapped_column(nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    cnpj: Mapped[str] = mapped_column(nullable=False)
    id_reviews: Mapped[list[str]] = mapped_column(
        MutableList.as_mutable(JSON), nullable=True, default=[]
    )
    id_complains: Mapped[list[str]] = mapped_column(
        MutableList.as_mutable(JSON), nullable=True, default=[]
    )

    def to_domain(self):
        return {
            "id": self.id,
            "name": self.name,
            "cnpj": self.cnpj,
            "id_reviews": self.id_reviews,
            "id_complains": self.id_complains
        }


# class Review(Base):
#     ...


class Users(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "api"}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True)
    cpf: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=False)

    def to_domain(self):
        return {
            "id": self.id,
            "name": self.name,
            "cpf": self.cpf,
            "phone": self.phone
        }
