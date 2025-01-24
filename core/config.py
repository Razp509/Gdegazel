import os

class Settings:
    """Считывание переменных окружения из файла .env"""
    PROJECT_NAME: str = "GdeGAZel"
    PROJECT_VERSION: str = "0.0.0"

    # Токен доступа к Google Sheets
    TOKEN = os.environ.get('BOT_TOKEN')

    # Список разрешенных пользователей
    ALLOWED_USERS = [int(user_id) for user_id in os.getenv('ALLOWED_USERS').split(',')]

    # Название таблицы в Google Sheets
    TABLE_NAME = os.environ.get('TABLE_NAME')

    # Номер листа Google Sheets
    SHEET_TITLE = os.environ.get('SHEET_TITLE')

    # Ссылки на таблицы
    TABLE_LINK_GAZ_TOTAL = os.environ.get('TABLE_LINK_GAZ_TOTAL')
    TABLE_LINK_GAZ_TRANSFER = os.environ.get('TABLE_LINK_GAZ_TRANSFER')
    TABLE_LINK_HIJET_TOTAL = os.environ.get('TABLE_LINK_HIJET_TOTAL')

    DISPATCH_LINK = os.environ.get('DISPATCH_LINK')

    G_DISK = os.environ.get('G_DISK')

    # Ячейки таблицы для подсчета сумм
    CELL_TOTAL_DAYS = os.environ.get('CELL_TOTAL_DAYS')
    CELL_TOTAL_AMOUNT = os.environ.get('CELL_TOTAL_AMOUNT')
    FLOATING_CELL_COUNT = os.environ.get('FLOATING_CELL_COUNT')


settings = Settings()