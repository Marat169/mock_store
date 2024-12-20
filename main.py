from user import User
from user import Admin
from user import Customer

class AuthenticationService:
    """Сервис для управления регистрацией и аутентификацией пользователей."""

    def __init__(self):
        self.current_user = None  # Текущий вошедший пользователь

    def register(self, user_class, username, email, password, *args):
        """Регистрация нового пользователя."""
        # Проверка уникальности имени пользователя
        if any(user.username == username for user in User.users):
            return "Username already exists."

        # Создание нового пользователя
        new_user = user_class(username, email, password, *args)
        User.users.append(new_user)  # Добавлен в список пользователей
        return f"User {username} registered successfully."

    def login(self, username, password):  # Исправление опечатки
        """Аутентификация пользователя."""
        for user in User.users:
            if user.username == username and user.check_password(password):
                self.current_user = user  # Установка текущего вошедшего пользователя
                return f"User {username} logged in successfully."
        return "Invalid username or password."

    def logout(self):
        """Выход пользователя из системы."""
        if self.current_user:
            self.current_user = None
            return "User logged out successfully."
        return "No user is currently logged in."

    def get_current_user(self):
        """Возвращает информацию о текущем вошедшем пользователе."""
        if self.current_user:
            return self.current_user.get_details()
        return "No user is currently logged in."

# Создаем сервис аутентификации
auth_service = AuthenticationService()

# Регистрируем пользователей
print(auth_service.register(Customer, "user1", "user1@example.com", "password123", "123 Main St"))
print(auth_service.register(Admin, "admin1", "admin1@example.com", "adminpassword", "super"))

# Пытаемся залогиниться
print(auth_service.login("user1", "password123"))
print(auth_service.get_current_user())  # Информация о текущем пользователе

# Выходим из системы
print(auth_service.logout())
print(auth_service.get_current_user())  # Должно вывести сообщение, что никто не вошел

# Логинимся как админ
print(auth_service.login("admin1", "adminpassword"))
print(auth_service.get_current_user()) # Информация об админе

# Просматриваем список пользователей
admin = auth_service.current_user # Текущий пользователь - админ
if isinstance(admin, Admin):
    print("List of users:")
    print(Admin.list_users())
    
# Удаляем пользователя customer1
if isinstance(admin, Admin):
    print(Admin.delete_user("user1"))
    
# Снова выводим список пользователей 
if isinstance(admin, Admin):
    print("List of users after deletion:")
    print(Admin.list_users())
    
# Логаут
print(auth_service.logout())