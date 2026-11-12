# Скопируйте этот файл в config.py и подставьте свои значения.
# config.py не попадает в git: там лежат токены.

# Токен сообщества VK с доступом к сообщениям.
comunity_token = 'community_token_here'

# Токен пользователя VK: от него выполняются users.search и photos.get.
acces_token = 'user_token_here'

# Строка подключения SQLAlchemy. Файл базы создастся автоматически.
db_url_object = 'sqlite:///viewed.db'
