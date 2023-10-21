from unittest import TestCase
import main

class TestYandex(TestCase):

    def test_create_folder(self):
        result = main.create_folder('Test')

        try:
            self.assertEqual(201, result)
        except AssertionError:
            print("\nОШИБКА")
            match result:
                case 409: print("Ресурс 'path' уже существует")
                case 400: print("Некорректные данные.")
                case 401: print("Не авторизован")
                case 403: print("API недоступно. Ваши файлы занимают больше места, чем у вас есть. Удалите лишнее "
                                "или увеличьте объём Диска")
                case 404: print("Не удалось найти запрошенный ресурс.")
                case 406: print("Ресурс не может быть представлен в запрошенном формате.")
                case 413: print("Загрузка файла недоступна. Файл слишком большой.")
                case 423: print("Технические работы. Сейчас можно только просматривать и скачивать файлы.")
                case 429: print("Слишком много запросов")
                case 503: print("Сервис временно недоступен")
                case 507: print("Недостаточно свободного места")
        else:
            print("\nПапка успешно создана")
        return