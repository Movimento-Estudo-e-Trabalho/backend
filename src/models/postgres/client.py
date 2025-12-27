# Queries do banco de dados
from .tables import Users
from sqlalchemy import create_engine, select, Select
from sqlalchemy.orm import Session
from core import config


engine = create_engine(config.settings.postgres_url, echo=True)

def add_user(name: str, cpf: str, phone: int, email: str):
    with Session(engine) as session:
        user = Users(
            name=name,
            cpf=cpf,
            phone=phone,
            email=email
        )

        session.add(user)

        session.commit()


def get_users() -> list:
    with engine.connect() as conn:
        result = conn.execute(select(Users)).all()

        return [
            dict(
                id=user.id,
                name=user.name,
                phone=user.phone,
                email=user.email
            )
            for user in result
        ]
