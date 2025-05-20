from main import formatted_name
import pytest


@pytest.mark.parametrize("test, expected", [
    (('John', 'Smith', 'Petrovich'), "John Petrovich Smith"),
    (('joHn', 'smiTh', ' petroviCh  '), "John  Petrovich   Smith"),
    (('john', 'smith'), "John Smith"),
    (('john', 'smith', ' '), "John   Smith"),
])
def test_formatted_name_normal(test, expected):
    assert formatted_name(*test) == expected


def test_formatted_name_empty():
    assert formatted_name('', '') == " "


@pytest.mark.parametrize("test", [
    ('john', 69),
    (1.2, "smith"),
    ('john', "smith", 13),
    (["John", "Adnriyovych"], "Smith"),
])
def test_formatted_name_wrong_data_type(test):
    with pytest.raises(TypeError):
        formatted_name(*test), "Need to only use strings"
