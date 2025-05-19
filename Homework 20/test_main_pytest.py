from main import Fibonacci, formatted_name
import pytest


def test_formatted_name():
    assert formatted_name('John', 'Smith', 'Petrovich') == "John Petrovich Smith"
    assert formatted_name('joHn', 'smiTh', ' petroviCh  ') == "John  Petrovich   Smith"
    assert formatted_name('john', 'smith') == "John Smith"
    assert formatted_name('john', 'smith', ' ') == "John   Smith"
    assert formatted_name('', '') == " "
    with pytest.raises(TypeError):
        formatted_name('john', 69), "Need to only use strings"
    with pytest.raises(TypeError):
        formatted_name(1.2, "smith"), "Need to only use strings"
    with pytest.raises(TypeError):
        formatted_name('john', "smith", 13), "Need to only use strings"
    with pytest.raises(TypeError):
        formatted_name(["John", "Adnriyovych"], "Smith"), "Need to only use strings"


def test_fibonacci():
    fibonacci = Fibonacci()
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55
    assert fibonacci(100) == 354224848179261915075
    assert fibonacci(200) == 280571172992510140037611932413038677189525
    with pytest.raises(ValueError, match=f'Positive integer number expected, got "{-1}"'):
        fibonacci(-1)
    with pytest.raises(ValueError, match=f'Positive integer number expected, got "{2.5}"'):
        fibonacci(2.5)
    with pytest.raises(ValueError, match=f'Positive integer number expected, got "{"10"}"'):
        fibonacci("10")
    with pytest.raises(ValueError, match=f'Positive integer number expected, got "{""}"'):
        fibonacci("")
