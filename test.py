from password.new_password import generate_password
import random
import string
import unittest

def generate_password(length=12):
    """Генерация случайного пароля заданной длины."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

class TestPasswordGeneration(unittest.TestCase):

    def test_password_length(self):
        """Проверка, что длина сгенерированного пароля соответствует заданной."""
        password = generate_password(12)
        self.assertEqual(len(password), 12)

    def test_password_has_special_characters(self):
        """Проверка, что сгенерированный пароль содержит специальные символы."""
        password = generate_password(12)
        special_characters = string.punctuation
        self.assertTrue(any(char in special_characters for char in password))

    def test_password_contains_uppercase(self):
        """Проверка, что сгенерированный пароль содержит заглавные буквы."""
        password = generate_password(12)
        self.assertTrue(any(char.isupper() for char in password))

    def test_password_contains_lowercase(self):
        """Проверка, что сгенерированный пароль содержит строчные буквы."""
        password = generate_password(12)
        self.assertTrue(any(char.islower() for char in password))

    def test_password_contains_digits(self):
        """Проверка, что сгенерированный пароль содержит цифры."""
        password = generate_password(12)
        self.assertTrue(any(char.isdigit() for char in password))

if __name__ == "__main__":
    unittest.main()
