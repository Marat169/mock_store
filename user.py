import hashlib
import uuid

class User:
    users = []  # Список всех пользователей

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.salt = uuid.uuid4().hex  # Создаём уникальную соль
        self.password = self.hash_password(password)

    def hash_password(self, password):
        """Хеширование пароля с использованием соли."""
        return hashlib.sha256((password + self.salt).encode()).hexdigest()

    def check_password(self, provided_password):
        """Проверка пароля."""
        return self.password == hashlib.sha256((provided_password + self.salt).encode()).hexdigest()
    
    def get_details(self):
        """Возвращает детали пользователя"""
        return f"Username: {self.username}\nEmail: {self.email}"
    
class Customer(User):
    """Класс, представляющий клиента, наследуется от User"""
    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address
        
    def get_details(self):
        """Возвращает детали пользователя"""
        return f"{super().get_details()}, Address: {self.address}"
               
class Admin(User):
    """""Класс, представляющий администратора, наследуется от User"""
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level
        
    def get_details(self):
        """Возвращает детали пользователя"""
        return f"{super().get_details()}, Admin Level: {self.admin_level}"
    
    @staticmethod
    def list_users():
        """Возвращает список пользователей"""
        return [user.get_details() for user in User.users]
    
    @staticmethod
    def delete_user(username):
        """Удаляет пользователя по имени"""
        for user in User.users:
           if user.username == username:
               User.users.remove(user)
               return f"User {username} deleted successfully."
        return f"User {username} not found." 