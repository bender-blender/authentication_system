


class System:
    """Система аунтификации на сайте
    """
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._password = input("Создайте пароль:")
        return cls._instance
    
    def login_to_the_site(self):
        """Вход на сайт
        """
        request = input("Введите пароль:")
        if self._password != request:
            print("Неверный пароль!")
        else:
            print("Доступ разрешен")

a = System()
a.login_to_the_site()

b = System()
b.login_to_the_site()