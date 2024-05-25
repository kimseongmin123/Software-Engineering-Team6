import json
import bcrypt
from datetime import datetime, timezone

DB_PATH = 'data/users/users.json'
TIME_NOW = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # User.last_login의 포맷

# 사용자 모델 정의 및 캡슐화
class User:
    def __init__(self, id, password, last_login): 
        self.id = id
        self.password = self.hash_password(password)
        self.last_login = last_login

    def hash_password(self, password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), b'$2b$12$eP7wJ79QgvF6v1d1h0FgIe') # salt는 추후 secrets.json으로 관리
        return hashed.decode('utf-8')

    def check_password(self, password):
        hased = self.hash_password(password)
        return bcrypt.checkpw(hased.encode('utf-8'), self.password.encode('utf-8'))

    def set_password(self, new_password):
        self.password = self.hash_password(new_password)

    @classmethod
    def deserializing(cls, user_dict): # dict -> instance
        return cls(user_dict.get('id'), user_dict.get('password'), user_dict.get('last_login'))

    def serializing(self): # instance -> dict
        return {"id": self.id, "password": self.password, "last_login": self.last_login}

    @staticmethod
    def load_users(): # User DB 로드
        with open(DB_PATH, "r") as f:
            user_list = json.load(f)["users"]
        users = [User.deserializing(user_dict) for user_dict in user_list]
        return users
    
    @staticmethod
    def does_exists(id, users): # users에 id 존재 여부 조회
        for user in users:
            if id == user.id:
                return True
        return False
    
    @staticmethod
    def get_user(id, users): # users에 특정 User 객체 반환
        for user in users:
            if id == user.id:
                return user
        return None
    
    @staticmethod
    def save(user_list): # User DB를 user_list로 동기화
        user_dict_list = []
        for user in user_list:
            user_dict_list.append(User.serializing(user))
        with open(DB_PATH, 'w') as f:
            f.write(json.dumps({'users': user_dict_list}, indent=4))
            
    def add(self): # 로드된 User DB에 자신 추가
        users = User.load_users()
        users.append(self)
        return users
        
    def update(self, password=None): # 특정 User 업데이트
        users = self.load_users()
        user = self.get_user(self.id, users)
        if password is not None:
            user.password = user.set_password(password)
        user.last_login = TIME_NOW
        return users
        
    def __repr__(self):
        return f"<User(id='{self.id}', last_login='{self.last_login}')>"
    
if __name__ == "__main__":
        pass
