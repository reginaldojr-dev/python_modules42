from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print('CSV Output:')
        print(','.join(value for _, value in data))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = []
        for rank, value in data:
            escaped = value.replace('\\', '\\\\').replace('"', '\\"')
            items.append(f'"item_{rank}": "{escaped}"')
        print('JSON Output:')
        print('{' + ', '.join(items) + '}')


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    break
            else:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            data: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    data.append(processor.output())
                except IndexError:
                    break
            if data:
                plugin.process_output(data)

    def print_processors_stats(self) -> None:
        print('== DataStream statistics ==')
        if not self.processors:
            print('No processor found, no data')
            return
        for processor in self.processors:
            name = processor.__class__.__name__.replace(
                'Processor',
                ' Processor',
            )
            print(
                f'{name}: total {processor.total_processed} items processed, '
                f'remaining {processor.remaining()} on processor'
            )


if __name__ == '__main__':
    print('=== Code Nexus - Data Pipeline ===')
    stream = DataStream()
    for processor in (NumericProcessor(), TextProcessor(), LogProcessor()):
        stream.register_processor(processor)
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead',
            },
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'},
        ],
        42,
        ['Hi', 'five'],
    ]
    stream.process_stream(batch)
    stream.print_processors_stats()
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()
    stream.process_stream([
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR',
             'log_message': '500 server crash'},
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days',
            },
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello',
    ])
    stream.print_processors_stats()
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()
