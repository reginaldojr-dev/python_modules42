import os
import site
import sys


def inside_virtualenv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if inside_virtualenv():
        print('Inside the Construct')
        print('MATRIX STATUS: Welcome to the construct')
        print(f'Current Python: {sys.executable}')
        print(f'Virtual Environment: {os.path.basename(sys.prefix)}')
        print(f'Environment Path: {sys.prefix}')
        print(f'sys.base_prefix: {sys.base_prefix}')
        print("SUCCESS: You're in an isolated environment!")
        print('Safe to install packages without affecting')
        print('the global system.')
        print('Package installation path:')
        for path in site.getsitepackages():
            print(path)
    else:
        print('Outside the Matrix')
        print("MATRIX STATUS: You're still plugged in")
        print(f'Current Python: {sys.executable}')
        print(f'sys.prefix: {sys.prefix}')
        print(f'sys.base_prefix: {sys.base_prefix}')
        print('Virtual Environment: None detected')
        print("WARNING: You're in the global environment!")
        print('The machines can see everything you install.')
        print('Global package locations:')
        for path in site.getsitepackages():
            print(path)
        print('To enter the construct, run:')
        print('python -m venv matrix_env')
        print('source matrix_env/bin/activate # On Unix')
        print(r'matrix_env\Scripts\activate # On Windows')
        print('Then run this program again.')


if __name__ == '__main__':
    main()
