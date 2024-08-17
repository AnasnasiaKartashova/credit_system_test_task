## Запуск

1. Создайте и активируйте виртуальное окружение:

    ```bash
    python3 -m venv venv
    ```

    - Для Linux: `source venv/bin/activate`
    - Для Windows: `venv\Scripts\activate.bat`

2. Создайте файл `.env` с переменными, нужные переменные указаны в файле .env_example

3. Запуск приложения:

   При запуске через docker-compose:

   ```bash
    docker-compose up --build
    ```

    URL для просмотра: [http://127.0.0.1:8001/](http://127.0.0.1:8001/)

    ИЛИ

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    python3 manage.py makemigrations
    python3.manage.py migrate
    python3.manage.py initadmin
    python3 manage.py loaddata fixtures.json
   ```
   Запустите сервер
   ```
    python3 manage.py runserver
    ```
   Если провели команду на создание superuser в админисративной панели Django, логин - root, пароль - 12345678
