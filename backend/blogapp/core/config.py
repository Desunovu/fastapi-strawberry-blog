import os
from pathlib import Path

from dotenv import load_dotenv

# Загрузка переменных окружения из файла .envexample
# без перезаписи если они уже существуют
dotenv_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    ".envexample",
)
load_dotenv_result = load_dotenv(dotenv_path=dotenv_path)

# Определение констант из переменных окружения
SECRET_KEY = os.getenv("SECRET_KEY")
MONGODB_URL = os.getenv("MONGODB_URL", "")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")

# Прочие константы
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Вычисление абсолютных путей приложения
BACKEND_DIR_PATH: Path = Path().parent.parent.absolute()
LOGS_DIR_PATH: Path = BACKEND_DIR_PATH / "logs"
