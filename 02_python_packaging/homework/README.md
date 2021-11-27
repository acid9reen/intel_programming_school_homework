# Homework 2
Python packaging showcase

## Task

- [x] 1. Разделить библиотеку которая была написана на практике на две части:
    1. Первая получает время консолькой командой get_time в формате unixtime
    2. Вторая использует функционал первой библтотеки и выводит отформатированное время командой get_time_pp
- [x] 2. использовать namespace внутри наших библиотек. Нужно не забыть указать namespace_packages=['your_namespace_name'], и добавить имя namespace перед именем пакета packages=['your_namespace_name.your_package_name'],
- [x] 3. Изменить код первого и второго пакета так, чтобы добиться такого поведения.
    1. Устанавливаем первый пакет get_time_package. Консольная команда get_time выводит 1637756935.
    2. Устанавливаем второй пакет pretty_print_package. Таже самая консольная команда get_time выводит отформатированную строку, например 2021-11-24 12:15:35.

## Usage
To get time in unix format:
```bash
pip install ./acid9reen.get_time
get_time
```

To get time in human-readable format:
```bash
pip install ./acid9reen.get_time ./acid9reen.pretty_print
get_time
```
With both packages installed `get_time_pp` terminal command also can be used.
