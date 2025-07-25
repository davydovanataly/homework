import pytest
from string_utils import StringUtils

utils = StringUtils()

# Тесты для capitalize


def test_capitalize_regular_string():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_already_capitalized():
    assert utils.capitalize("SkyPro") == "Skypro"
    # capitalize приводит к 1 заглавному символу


def test_capitalize_empty_string():
    assert utils.capitalize("") == ""


def test_capitalize_non_alpha_first_char():
    assert utils.capitalize("123abc") == "123abc"


def test_capitalize_typical_word_cyrillic():
    assert utils.capitalize("Тест") == "Тест"


def test_capitalize_numbers_as_string():
    assert utils.capitalize("123") == "123"


def test_capitalize_none_raises():
    with pytest.raises(AttributeError):
        utils.capitalize(None)

# Тесты для trim


def test_trim_leading_spaces():
    assert utils.trim("   skypro") == "skypro"


def test_trim_no_spaces():
    assert utils.trim("skypro") == "skypro"


def test_trim_only_spaces():
    assert utils.trim("     ") == ""


def test_trim_empty_string():
    assert utils.trim("") == ""


def test_trim_string_with_leading_spaces_and_date():
    assert utils.trim("  04 апреля 2023") == "04 апреля 2023"


def test_trim_none_raises():
    with pytest.raises(AttributeError):
        utils.trim(None)

# Тесты для contains


def test_contains_symbol_in_string():
    assert utils.contains("SkyPro", "S") is True


def test_contains_symbol_not_in_string():
    assert utils.contains("SkyPro", "U") is False


def test_contains_empty_string():
    assert utils.contains("", "a") is False


def test_contains_empty_symbol():
    # Поиск пустой подстроки всегда True
    assert utils.contains("SkyPro", "") is True


def test_contains_symbol_longer_than_one_char():
    assert utils.contains("SkyPro", "Pro") is True
    assert utils.contains("SkyPro", "pro") is False  # регистрозависимый поиск


def test_contains_symbol_positive_cyrillic():
    assert utils.contains("Тест", "Т") is True

# Тесты для delete_symbol


def test_delete_symbol_single_char_present():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring_present():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_symbol_not_present():
    s = "SkyPro"
    assert utils.delete_symbol(s, "x") == s


def test_delete_symbol_empty_symbol():
    s = "SkyPro"
    assert utils.delete_symbol(s, "") == s


def test_delete_symbol_empty_string():
    assert utils.delete_symbol("", "a") == ""


def test_delete_symbol_remove_substring_cyrillic():
    assert utils.delete_symbol("04 апреля 2023", "апреля ") == "04 2023"
