
# Swag Labs (Python+Selenium)


[![Build Status](https://travis-ci.org/k-bamboo-cyber/final_project.svg?branch=master)](https://travis-ci.org/k-bamboo-cyber/final_project)


Проект предназначен для демонстрации навыков автоматизации тестирования на примере [интернет-магазина](https://www.saucedemo.com/) Swag Labs

#Используемые фреймворки

- Pytest (среда тестирования)
- Selenium WebDriver (инструмент для автоматизации)
- Allure (отчёты)
- Travis CI (проверка кода)

# Контроль качества кода

Реализован с помощью pre-commit hook, который проверяет и форматирует код перед коммитом.

### Установка

    pip install pre-commit
    pre-commit install

### Использование

Хук запускается автоматически перед коммитом. Принудительный запуск:

    pre-commit run --all-files

# Отчёты

Для удобного анализа результатов тестирования, добавлен функционал построения очётов

## Отчёты в Allure

### Установка

**Scoop**

В powershell выполнить две команды для установки scoop:

    Set-ExecutionPolicy RemoteSigned -scope CurrentUser

    Invoke-Expression (New-Object System.Net.WebClient).DownloadString('[https://get.scoop.sh]')

**Allure**

C помощью scoop установить Allure:

       scoop install allure

>Необходимо проверить, установлена ли Java. Для этого ввести allure и нажать enter. Если не установлена, то необходимо установить и добавить в переменные окружения.

### Запуск

    pytest --alluredir <dir_name>

### Просмотр отчёта

> Запустить команду в powershell в той папке, где лежит <dir_name>

    allure serve <dir_name>


#Для настройки окружения

 + Установить Python 3.8


 + Создать виртуальное окружение с помощью команды (подробнее https://docs.python.org/3/library/venv.html):


    python3 -m venv /path/to/new/virtual/environment

 + Выполнить в командной строке:


    pip install -r requirements.txt

# Запуск тестов
Тесты можно запускать с опциональными параметрами:

    pytest --headless==false --username=ansh120022 --password=1234

Для быстрого прогона часть тестов помечена меткой smoke, для запуска из директории tests:


    pytest -m smoke standard_user
