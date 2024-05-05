import json
from pathlib import Path
from typing import Any, Optional


def _init(file: Optional[Path] = None, data: Optional[dict] = None) -> None:
    """Инициализация конфига"""
    # Создание каталога
    catalog = Path("data/")
    catalog.mkdir(exist_ok=True)

    # Проверка файла
    if not file or (catalog / file).exists():
        return

    if data is None:
        data = {}

    # Запись
    with open(catalog / file, "w") as f:
        json.dump(data, f)


class Data:
    file: Path
    data: dict

    def read(self) -> dict:
        """Чтение файла"""
        _init(self.file, self.data)

        with open("data" / self.file) as file:
            data = json.load(file)

        return data

    def update(self, data: dict) -> None:
        """Обновление файла"""
        _init(self.file, self.data)

        with open("data" / self.file, "w") as file:
            json.dump(data, file, indent=4)


class UserStatistic(Data):
    """Статистика пользователя"""

    file = Path("userStatistic.json")
    data = {"clicks": 0, "errors": 0, "best_time": "00:00:00"}

    @property
    def clicks(self) -> int:
        """Количество сделанных кликов"""
        data = self.read()
        return data["clicks"]

    @clicks.setter
    def clicks(self, obj: Any):
        data = self.read()
        data["clicks"] = obj
        self.update(data)

    @property
    def errors(self) -> int:
        """Количество ошибок"""
        data = self.read()
        return data["errors"]

    @errors.setter
    def errors(self, obj: Any):
        data = self.read()
        data["errors"] = obj
        self.update(data)

    @property
    def best_time(self) -> str:
        """Лучшее время"""
        data = self.read()
        return data["best_time"]

    @best_time.setter
    def best_time(self, obj: Any):
        data = self.read()
        data["best_time"] = obj
        self.update(data)


__all__ = (
    "UserStatistic",
)
