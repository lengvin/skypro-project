import pytest

from src.decorators import log


@pytest.mark.parametrize('test_data', [
    (1, 2, f'example_func ok. результат выполнения: \n 3'),
    (3, 3, f'example_func ok. результат выполнения: \n 6'),
    (1, '1', f"example_func error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '1')\n")
])
def test_console_log(test_data, capsys):
    a1, b1, result = test_data

    @log()
    def example_func(a, b):
        return a + b
    example_func(a1, b1)
    captured = capsys.readouterr()

    assert result in captured.out


@pytest.mark.parametrize('test_data', [
    (1, 2, f'example_func ok. результат выполнения: \n 3'),
    (3, 3, f'example_func ok. результат выполнения: \n 6'),
    (1, '1', f"example_func error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '1') \n")
])
def test_file_log(test_data):
    a1, b1, result = test_data

    @log('testLog.txt')
    def example_func(a, b):
        return a + b
    example_func(a1, b1)

    with open('testLog.txt', 'r', encoding='windows-1251') as file:
        file_result = file.read()
        assert result in file_result
