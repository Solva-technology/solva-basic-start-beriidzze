import subprocess
import sys
import os

def run_main_script():
    """Helper function to run main.py and capture its output."""
    command = [sys.executable, "main.py"]
    
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    env['PYTHONUTF8'] = '1'

    process = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding='utf-8',
        env=env
    )
    return process

def test_script_runs_successfully():
    """Тест проверяет, что скрипт main.py запускается без ошибок."""
    process = run_main_script()
    assert process.returncode == 0, f"Скрипт завершился с ошибкой:\n{process.stderr}"

def test_output_is_not_empty():
    """Тест проверяет, что скрипт что-то выводит в stdout."""
    process = run_main_script()
    assert process.stdout, "Скрипт ничего не вывел."

def test_output_contains_three_lines():
    """Тест проверяет, что в выводе ровно три строки."""
    process = run_main_script()
    lines = process.stdout.strip().split('\n')
    assert len(lines) == 3, f"Ожидалось 3 строки вывода, но получено {len(lines)}."

def test_name_line_is_filled():
    """Тест проверяет, что строка с именем заполнена и не содержит плейсхолдер."""
    process = run_main_script()
    name_line = process.stdout.strip().split('\n')[0]
    assert name_line.startswith("Меня зовут: "), "Первая строка должна начинаться с 'Меня зовут: '"
    assert "[вставьте сюда свое имя]" not in name_line, "Пожалуйста, вставьте свое имя в файле main.py"
    assert len(name_line.replace("Меня зовут: ", "").strip()) > 0, "Имя не может быть пустым."

def test_age_line_is_filled():
    """Тест проверяет, что строка с возрастом заполнена и не содержит плейсхолдер."""
    process = run_main_script()
    age_line = process.stdout.strip().split('\n')[1]
    assert age_line.startswith("Мой возраст: "), "Вторая строка должна начинаться с 'Мой возраст: '"
    assert "[вставьте сюда свой возраст]" not in age_line, "Пожалуйста, вставьте свой возраст в файле main.py"
    assert len(age_line.replace("Мой возраст: ", "").strip()) > 0, "Возраст не может быть пустым."

def test_color_line_is_filled():
    """Тест проверяет, что строка с цветом заполнена и не содержит плейсхолдер."""
    process = run_main_script()
    color_line = process.stdout.strip().split('\n')[2]
    assert color_line.startswith("Мой любимый цвет: "), "Третья строка должна начинаться с 'Мой любимый цвет: '"
    assert "[вставьте сюда свой любимый цвет]" not in color_line, "Пожалуйста, вставьте свой любимый цвет в файле main.py"
    assert len(color_line.replace("Мой любимый цвет: ", "").strip()) > 0, "Любимый цвет не может быть пустым."