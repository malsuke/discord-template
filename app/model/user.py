from sqlalchemy.orm import sessionmaker
from model.db.db_config import engine
from model.db.user import UserModel
from model.point import Point


class User:
    user_discord_id: int
    user_name: str
    session: sessionmaker

    def __init__(self, user_discord_id: int, user_name: str):
        self.user_discord_id = user_discord_id
        self.user_name = user_name
        SessionClass = sessionmaker(engine)
        self.session = SessionClass()

    def exists_or_create(self) -> bool:
        user = self.session.query(UserModel).filter(UserModel.user_discord_id == self.user_discord_id).first()
        if user:
            return False
        else:
            user = UserModel(user_discord_id=self.user_discord_id, user_name=self.user_name)
            self.session.add(user)
            self.session.commit()
            point = Point(user_id=self.user_discord_id)
            point.create_point()
            return True

    def mention(self) -> str:
        return f"<@{self.user_discord_id}>"

    def get_user(self) -> UserModel:
        user = self.session.query(UserModel).filter(UserModel.user_discord_id == self.user_discord_id).first()
        return user
