import threading
from typing import Any
from typing import Dict

from core.logger import log


class Database:
    def __init__(self):
        self.tasks = []
        self._last_used_id = 0
        self._ids_set = set()
        self._lock = threading.Lock()

    def generate_new_id(self):
        # Блокируем доступ для других потоков
        with self._lock:
            new_id = self._last_used_id
            self._last_used_id += 1
            self._ids_set.add(new_id)
            return new_id

    def add_new_record(self, data: Dict[str, Any]) -> Dict[str, Any]:
        new_id = self.generate_new_id()
        data["id"] = new_id
        self.tasks.append(data)
        log.info("Запись с id=%d успешно добавлена в базу данных: %s", new_id, data)
        return data

    def find_record_by_id(self, id: int) -> Dict[str, Any] | None:
        if id not in self._ids_set:
            return None

        for record in self.tasks:
            if record["id"] == id:
                return record


db = Database()
