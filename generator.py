from __future__ import annotations

import random
import string

import typer
from random_word import RandomWords
from tenacity import retry, retry_if_exception_type

app = typer.Typer()
random_words = RandomWords()


def _generate_password(
    length: int,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_symbols=True,
):
    password = ''
    letter_pool = []
    if use_uppercase:
        letter_pool.append(string.ascii_uppercase)
    if use_lowercase:
        letter_pool.append(string.ascii_lowercase)
    if use_digits:
        letter_pool.append(string.digits)
    if use_symbols:
        letter_pool.append(string.punctuation)

    # make sure every pool of characters is chosen from
    # the idea is that if a user wants symbols, then at least 1 symbol should be added
    temp_letter_pool = letter_pool.copy()
    for _ in range(length):
        if len(temp_letter_pool) == 0:
            temp_letter_pool = letter_pool.copy()
        password += random.choice(
            temp_letter_pool.pop(random.randint(0, len(temp_letter_pool) - 1))
        )
    return password


def _generate_passphrase(separator: str, word_count=3, capitalize_words=True):
    words = get_random_words(word_count)
    words = [word.replace(' ', '').replace('-', '') for word in words]
    if capitalize_words:
        words: list[str] = [word.capitalize() for word in words]
    else:
        words = [word.lower() for word in words]
    return separator.join(words)


@retry(retry=retry_if_exception_type(ValueError))
def get_random_words(n) -> list:
    words = random_words.get_random_words(
        limit=n, includePartOfSpeech="noun,verb", maxLength=6
    )
    if words is None:
        raise ValueError
    return words


@app.command()
def password(
    length: int,
    use_uppercase: bool = typer.Option(False, '-u', '--uppercase'),
    use_digits: bool = typer.Option(False, '-d', '--digits'),
    use_symbols: bool = typer.Option(False, '-s', '--symbols'),
):
    print(
        _generate_password(
            length,
            use_uppercase=use_uppercase,
            use_digits=use_digits,
            use_symbols=use_symbols,
        )
    )


@app.command()
def passphrase(
    separator: str = typer.Argument(' '),
    word_count: int = typer.Option(3, '-w', '--word-count'),
    capitalize_words: bool = typer.Option(False, '-c', '--capitalize'),
):
    print(
        _generate_passphrase(
            separator, word_count=word_count, capitalize_words=capitalize_words
        )
    )


if __name__ == '__main__':
    app()
