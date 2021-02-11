import string
from time import sleep

from generator import _generate_password, _generate_passphrase, get_random_words

# defaults
LENGTH = 20
SEPARATOR = '-'


def test_generate_password():
    password = _generate_password(LENGTH)
    assert isinstance(password, str)
    assert len(password) == LENGTH

    # test uppercase and no lowercase
    password2 = _generate_password(LENGTH, True, False)
    assert any(letter in string.ascii_uppercase for letter in password2)
    assert not any(letter in string.ascii_lowercase for letter in password2)

    # test lowercase and no uppercase
    password3 = _generate_password(LENGTH, False, True)
    assert any(letter in string.ascii_lowercase for letter in password3)
    assert not any(letter in string.ascii_uppercase for letter in password3)

    # test digits
    password4 = _generate_password(
        LENGTH,
        use_digits=True,
    )
    assert any(letter in string.digits for letter in password4)

    # test symbols
    password5 = _generate_password(
        LENGTH,
        use_uppercase=True,
        use_lowercase=True,
        use_digits=True,
        use_symbols=True,
    )
    assert any(letter in string.punctuation for letter in password5)


def test_get_words():
    num_words = 5
    for _ in range(5):
        words: list[str] = get_random_words(n=num_words)
        assert words is not None
        assert len(words) == num_words
        sleep(0.5)


def test_generate_passphrase():
    word_count = 5
    password = _generate_passphrase(
        SEPARATOR, word_count=word_count, capitalize_words=True
    )
    assert isinstance(password, str)
    assert SEPARATOR in password
    assert len(password.split(SEPARATOR)) == word_count
    assert any(letter in string.ascii_uppercase for letter in password)

    password2 = _generate_passphrase(
        SEPARATOR, word_count=word_count, capitalize_words=False
    )
    assert not any(letter in string.ascii_uppercase for letter in password2)
