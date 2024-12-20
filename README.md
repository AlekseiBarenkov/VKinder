# VKinder: Чат-бот для социальной сети VK

Добро пожаловать в **VKinder** — чат-бот для платформы VK, который упрощает поиск анкет, соответствующих вашим предпочтениям, и автоматизирует процесс общения. 😊

---

## 📌 Описание проекта

VKinder — это умный помощник для социальной сети VK. Он позволяет находить анкеты пользователей на основе заданных критериев и предоставляет удобный интерфейс для работы с полученными результатами.

---

## 🚀 Функционал

1. **Приветственное сообщение**  
   Чат-бот приветствует пользователя по имени и предлагает свои услуги.

2. **Поиск анкет**  
   - Поиск анкет выполняется на основе:
     - Города
     - Половой принадлежности
     - Возраста
   - Учитываются только открытые профили с фотографиями.
   - Сортировка и вывод лучших фотографий анкет.

3. **Сохранение данных**  
   - Отслеживание просмотренных анкет.
   - Исключение повторного показа уже просмотренных профилей.

4. **Команды**  
   - **`Привет`** — приветствие от бота.
   - **`Поиск`** — запускает процесс поиска анкет.
   - **`Пока`** — завершение общения с ботом.

5. **Работа с фотографиями**  
   - Получение и сортировка фотографий по количеству лайков и комментариев.

6. **Интерактивное общение**  
   - Запрос недостающих данных у пользователя (город, возраст, пол).

---

## 🛠️ Используемые технологии

### Бэкенд
- **Python** — основа логики работы бота.
- **SQLAlchemy** — ORM для работы с базой данных SQLite.

### API и интеграции
- **VK API** — взаимодействие с социальной сетью VK.
- **vk_api** — библиотека для работы с VK API.

### Хранение данных
- **SQLite** — база данных для хранения просмотренных анкет.

### Другие технологии
- **datetime** — для вычисления возраста пользователя.
- **pprint** — для форматированного вывода данных.

---

## 🔧 Настройка проекта

### 1. Получение токенов
1. Создайте группу в VK.
2. Получите токен для группы, следуя [инструкции](https://github.com/netology-code/py-advanced-diplom/blob/new_diplom/group_settings.md).
3. Зарегистрируйтесь в VK API, чтобы получить токен для пользователя.

### 2. Настройка переменных окружения
1. В корне проекта создайте файл `config.py`.
2. Укажите свои токены:
   ```python
   comunity_token = '<ваш токен группы>'
   acces_token = '<ваш токен пользователя>'
   db_url_object = 'sqlite:///viewed.db'

### 3. Запуск проекта

1. Убедитесь, что установлены все зависимости:  
   ```bash
   pip install -r requirements.txt
2. Запустите бота:  
   ```bash
   python interface.py

## 🛡️ Как работает VKinder?

1. Пользователь пишет сообщение в группу VK.  
2. Бот отвечает и предоставляет следующие команды:  
   - **`Привет`**: бот приветствует пользователя и сообщает его имя.  
   - **`Поиск`**: бот начинает поиск подходящих анкет.  
   - **`Пока`**: бот завершает диалог с пользователем.  
   - Для любых других сообщений бот отправляет подсказку с доступными командами.  

3. Если выбрана команда `Поиск`:  
   - Бот проверяет наличие необходимых данных (город, возраст, пол).  
   - Если данных не хватает, бот запрашивает их у пользователя.  
   - После получения всех данных бот делает запрос к VK API для поиска анкет.  

4. Анкеты обрабатываются следующим образом:  
   - Каждая анкета содержит имя, ссылку на профиль и лучшие фото.  
   - Лучшие фото выбираются на основе количества лайков и комментариев.  
   - Анкеты проверяются на уникальность с помощью базы данных (чтобы не показывать повторно).  

5. После успешного поиска бот отправляет пользователю информацию:  
   - **Имя анкеты**  
   - **Ссылка на профиль**  
   - **Топ-3 лучших фото**  

6. После просмотра анкета сохраняется в базе данных, чтобы исключить повторный показ.  

Вот и всё! Теперь VKinder заботится о том, чтобы ваш опыт поиска был максимально удобным и эффективным. 🚀
