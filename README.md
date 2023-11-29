# first

Простий flask-проєкт

## Інструкція по розгортанню

1. **Крок 1: Клонування репозиторію**
   ```bash
     git clone https://github.com/MirraRed/first-lab.git

2. **Крок 2: Перейдіть у папку проекту**
   ```bash
     cd ваш_шлях\first-lab

3. **Крок 3: Активація віртуального середовища**
     Для користувачів Windows:
   ```bash
     .\venv\Scripts\activate
   ```
   Для користувачів UNIX-систем:
   ```bash
     source venv/bin/activate
   ```

   Для виходу з віртуального середовища:
    ```bash
      deactivate
    ```

4. **Крок 4: Запуск проєкту:**
   Переходимо до папки з кодом:
     cd ваш_шлях\first-lab\my_project

   Запускаємо просту адресу
  ```bash
    python main.py
  ```

   Переходимо за посиланням:
   ```bash
    http://localhost:5000/api/v1/hello-world-ваш_варіант
   ```

  Для зупинки серверу: ``` Ctrl + C ```

5. **Крок 5: Запуск через WSGI сервер (використовується waitress, працює на всіх системах)**
   ```bash
     poetry run python run.py
   ```

  Переходимо за посиланням:   
  ```bash
    http://localhost:8080/api/v1/hello-world-ваш_варіант
   ```

  Для зупинки серверу: ``` Ctrl + C ```
