from sqlalchemy.orm import sessionmaker
from model.db.db_config import engine
from model.db.point import PointModel


class Point:
    point: int
    user_id: int
    session: sessionmaker

    def __init__(self, user_id: int):
        self.user_id = user_id
        SessionClass = sessionmaker(engine)
        self.session = SessionClass()

    def create_point(self) -> None:
        point = PointModel(user_id=self.user_id)
        self.session.add(point)
        self.session.commit()
        return

    def mention(self) -> str:
        return f"<@{self.user_id}>"

    def get_point(self) -> int:
        point = self.session.query(PointModel).filter(PointModel.user_id == self.user_id).first()
        if point:
            return point.point
        else:
            return 0

    def add_20_point(self) -> None:
        point = self.session.query(PointModel).filter(PointModel.user_id == self.user_id).first()
        if point:
            point.point += 20
            self.session.commit()
        return

    def sub_20_point(self) -> None:
        point = self.session.query(PointModel).filter(PointModel.user_id == self.user_id).first()
        if point:
            point.point -= 20
            self.session.commit()
        return
