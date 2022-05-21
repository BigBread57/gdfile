from gdfile.helpers import AbstractGenerate, Helper


class GenerateTests(AbstractGenerate, Helper):
    """Генерация тестов."""

    def __init__(self, dict_params: dict, path: str, *args, **kwargs) -> None:
        """Инициализируем переменные (параметры для вставки, название файла)."""
        self.params = dict_params
        self.name_file = dict_params.get('{{main_class}}').lower()
        self.path = path

    def start_generate(self):
        """Генерация файла."""
        # Вызываем функцию, где открываем пример файла для теста и
        # считываем его, в заданные поля вставляем нужную информацию.
        initial_file = self.generate_context(
            f'{self.path}/sample/example_tests.py',
            self.params,
        )

        # Открываем конечный файл для записи. Записываем то, что сформировали.
        with open(
            f'done/tests/test_app/test_api_{self.name_file}.py',
            'w',
            encoding='utf-8',
        ) as f:
            f.write(initial_file)
