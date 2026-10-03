import site
import sys


def inside_virtualenv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    print(f'Python executable: {sys.executable}')
    print(f'sys.prefix: {sys.prefix}')
    print(f'sys.base_prefix: {sys.base_prefix}')
    print('Package locations:')
    for path in site.getsitepackages():
        print(path)
    if inside_virtualenv():
        print('Inside the Construct')
        print('Virtual environment detected.')
    else:
        print('Outside the Matrix')
        print('Create and activate a virtual environment:')
        print('python -m venv matrix_env')
        print('source matrix_env/bin/activate # On Unix')
        print(r'matrix_env\Scripts\activate # On Windows')


if __name__ == '__main__':
    main()
