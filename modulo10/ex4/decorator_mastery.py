import time
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar, cast


F = TypeVar('F', bound=Callable[..., Any])


def spell_timer(func: F) -> F:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f'Casting {func.__name__}...')
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'Spell completed in {elapsed:.3f} seconds')
        return result
    return cast(F, wrapper)


def power_validator(min_power: int) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power')
            if power is None and args:
                power = args[-1]
            if not isinstance(power, int):
                return 'Insufficient power for this spell'
            if power < min_power:
                return 'Insufficient power for this spell'
            return func(*args, **kwargs)
        return cast(F, wrapper)
    return decorator


def retry_spell(max_attempts: int) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f'Spell failed, retrying... '
                            f'(attempt {attempt}/{max_attempts})'
                        )
            return f'Spell casting failed after {max_attempts} attempts'
        return cast(F, wrapper)
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            char.isalpha() or char.isspace()
            for char in name
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f'Successfully cast {spell_name} with {power} power'


if __name__ == '__main__':
    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return 'Fireball cast!'

    @retry_spell(3)
    def unstable_spell() -> str:
        raise RuntimeError('failed')

    @power_validator(5)
    def war_cry(power: int) -> str:
        return 'Waaaaaaagh spelled !'

    print('Testing spell timer...')
    print(f'Result: {fireball()}')
    print('Testing retrying spell...')
    print(unstable_spell())
    print(war_cry(5))
    guild = MageGuild()
    print('Testing MageGuild...')
    print(MageGuild.validate_mage_name('Gandalf'))
    print(MageGuild.validate_mage_name('Al'))
    print(guild.cast_spell('Lightning', 15))
    print(guild.cast_spell('Spark', 5))
