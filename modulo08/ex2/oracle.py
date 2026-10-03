import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None  # type: ignore[assignment]


REQUIRED = ['DATABASE_URL', 'API_KEY', 'ZION_ENDPOINT']


def load_configuration() -> dict[str, str | None]:
    if load_dotenv is not None:
        load_dotenv()
    return {
        'MATRIX_MODE': os.getenv('MATRIX_MODE', 'development'),
        'DATABASE_URL': os.getenv('DATABASE_URL'),
        'API_KEY': os.getenv('API_KEY'),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'DEBUG'),
        'ZION_ENDPOINT': os.getenv('ZION_ENDPOINT'),
    }


def main() -> None:
    print('ORACLE STATUS: Reading the Matrix...')
    if load_dotenv is None:
        print(
            'python-dotenv is missing. Install it with '
            'pip install -r requirements.txt'
        )
        sys.exit(1)
    config = load_configuration()
    missing = [name for name in REQUIRED if not config[name]]
    print('Configuration loaded:')
    print(f"Mode: {config['MATRIX_MODE']}")
    database_status = (
        'Connected to local instance'
        if config['DATABASE_URL']
        else 'Missing DATABASE_URL'
    )
    api_status = (
        'Authenticated'
        if config['API_KEY']
        else 'Missing API_KEY'
    )
    print(f'Database: {database_status}')
    print(f'API Access: {api_status}')
    print(f"Log Level: {config['LOG_LEVEL']}")
    zion_status = 'Online' if config['ZION_ENDPOINT'] else 'Offline'
    print(f'Zion Network: {zion_status}')
    print('Environment variables override values from .env.')
    if missing:
        print(f'Missing configuration: {", ".join(missing)}')
    print('The Oracle sees all configurations.')


if __name__ == '__main__':
    main()
