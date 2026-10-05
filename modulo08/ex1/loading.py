import importlib
from types import ModuleType
from typing import Any, cast


REQUIRED = ['pandas', 'numpy', 'matplotlib']
PURPOSES = {
    'pandas': 'Data manipulation ready',
    'numpy': 'Numerical computation ready',
    'matplotlib': 'Visualization ready',
}


def load_module(name: str) -> ModuleType | None:
    try:
        return importlib.import_module(name)
    except ImportError:
        return None


def check_dependencies() -> dict[str, object]:
    loaded: dict[str, object] = {}
    print('Checking dependencies:')
    for name in REQUIRED:
        module = load_module(name)
        if module is None and name in REQUIRED:
            print(
                f'[MISSING] {name} - install with pip install '
                f'-r requirements.txt or poetry install'
            )
        elif module is not None:
            version = getattr(module, '__version__', 'unknown')
            print(f'[OK] {name} ({version}) - {PURPOSES[name]}')
            loaded[name] = module
    return loaded


def main() -> None:
    print('LOADING STATUS: Loading programs...')
    loaded = check_dependencies()
    if any(name not in loaded for name in REQUIRED):
        print('Missing required dependencies.')
        return
    pandas = cast(Any, loaded['pandas'])
    numpy = cast(Any, loaded['numpy'])
    pyplot = cast(Any, importlib.import_module('matplotlib.pyplot'))
    print('Analyzing Matrix data...')
    data = numpy.random.default_rng(42).normal(loc=50, scale=12, size=1000)
    frame = pandas.DataFrame({'signal': data})
    print(f'Processing {len(frame)} data points...')
    print('Generating visualization...')
    frame['signal'].plot(
        kind='hist',
        bins=30,
        title='Matrix Signal Distribution',
    )
    pyplot.xlabel('Signal')
    pyplot.savefig('matrix_analysis.png')
    pyplot.close()
    print('Analysis complete!')
    print('Results saved to: matrix_analysis.png')
    print(
        'pip installs from requirements.txt; Poetry installs from '
        'pyproject.toml and poetry.lock.'
    )


if __name__ == '__main__':
    main()
