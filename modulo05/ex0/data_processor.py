from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._next_rank = 0
        self.total_processed = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def _store(self, values: list[str]) -> None:
        self._data.extend(values)
        self.total_processed += len(values)

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError('No processed data available')
        rank = self._next_rank
        self._next_rank += 1
        return rank, self._data.pop(0)

    def remaining(self) -> int:
        return len(self._data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, (int, float)) or (
            isinstance(data, list)
            and all(isinstance(item, (int, float)) for item in data)
        )

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError('Improper numeric data')
        values = data if isinstance(data, list) else [data]
        self._store([str(value) for value in values])


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) or (
            isinstance(data, list)
            and all(isinstance(item, str) for item in data)
        )

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError('Improper text data')
        values = data if isinstance(data, list) else [data]
        self._store(list(values))


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return self._is_log(data) or (
            isinstance(data, list)
            and all(self._is_log(item) for item in data)
        )

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError('Improper log data')
        values = data if isinstance(data, list) else [data]
        self._store([
            f"{item['log_level']}: {item['log_message']}"
            for item in values
        ])

    def _is_log(self, data: Any) -> bool:
        return (
            isinstance(data, dict)
            and all(isinstance(k, str) and isinstance(v, str)
                    for k, v in data.items())
            and 'log_level' in data
            and 'log_message' in data
        )


if __name__ == '__main__':
    print('=== Code Nexus - Data Processor ===')
    numeric = NumericProcessor()
    text = TextProcessor()
    logs = LogProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    try:
        numeric.ingest('foo')  # type: ignore[arg-type]
    except ValueError as error:
        print(f'Got exception: {error}')
    numeric.ingest([1, 2, 3, 4, 5])
    text.ingest(['Hello', 'Nexus', 'World'])
    logs.ingest([
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'},
    ])
    processors = [
        ('Numeric', numeric, 3),
        ('Text', text, 1),
        ('Log', logs, 2),
    ]
    for proc_name, proc, count in processors:
        for _ in range(count):
            rank, value = proc.output()
            print(f'{proc_name} value {rank}: {value}')
