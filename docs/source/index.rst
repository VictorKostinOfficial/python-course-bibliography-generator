
Оформление библиографического списка
*************************************

Консольное приложение для создания библиографического списка.
Приложение позволяет автоматизировать процесс формирования библиографического списка по заданному стандарту цитирования.

Поддерживаемые стили цитирования:
    - ГОСТ Р 7.0.5-2008
    - APA 7th

Установка
=========

Установите требуемое ПО:

1. Docker для контейнеризации – |link_docker|

.. |link_docker| raw:: html

   <a href="https://www.docker.com" target="_blank">Docker Desktop</a>

2. Для работы с системой контроля версий – |link_git|

.. |link_git| raw:: html

   <a href="https://github.com/git-guides/install-git" target="_blank">Git</a>

3. IDE для работы с исходным кодом – |link_pycharm|

.. |link_pycharm| raw:: html

    <a href="https://www.jetbrains.com/ru-ru/pycharm/download" target="_blank">PyCharm</a>

Клонируйте репозиторий проекта в свою рабочую директорию:

    .. code-block:: console

        git clone https://github.com/mnv/python-course-bibliography-generator.git

Использование
=============

Перед началом использования приложения необходимо его сконфигурировать.

.. note::

    Для конфигурации выполните команды, описанные ниже, находясь в корневой директории проекта (на уровне с директорией `src`).

1. Скопируйте исходный Excel-файл шаблона (`template.xlsx`), создав новый файл (`input.xlsx`):
    .. code-block:: console

        cp media/template.xlsx media/input.xlsx

    Файл `input.xlsx` будет подаваться на вход программе. Заполните его информацией о списке источников.

2. Скопируйте файл настроек `.env.sample`, создав файл `.env`:
    .. code-block:: console

        cp .env.sample .env

    Этот файл содержит преднастроенные переменные окружения, значения которых будут общими для всего приложения.
    Файл примера (`.env.sample`) содержит набор переменных со значениями по умолчанию.
    Созданный файл `.env` можно настроить в зависимости от окружения.

    .. warning::

        Никогда не добавляйте в систему контроля версий заполненный файл `.env` для предотвращения компрометации информации о конфигурации приложения.

3. Соберите Docker-контейнер с помощью Docker Compose:
    .. code-block:: console

        docker compose build

    Данную команду необходимо выполнять повторно в случае обновления зависимостей в файле `requirements.txt`.

4. Чтобы просмотреть документацию по использованию консольного приложения, выполните:
    .. code-block:: console

        docker compose run app python main.py --help

    Данная команда выведет на экран список доступных аргументов и их значения по умолчанию.

5. Для запуска приложения выполните:
    .. code-block:: console

        docker compose run app python main.py

    Запустится программа. Она считает исходный файл `media/input.xlsx`, выполнит обработку данных и сгенерирует выходной файл – `media/output.docx`.
    Откройте этот файл и проверьте результат работы приложения.

    .. note::

       Для настройки параметров запуска следует передать консольной команде аргументы в соответствии с её документацией:
        .. code-block:: console

            docker compose run app python main.py --citation gost --path_input /media/input.xlsx --path_output /media/output.docx

        Таким образом можно определять стиль цитирования и пути ко входному и выходному файлам.

Автоматизация
=============

Проект содержит специальный файл (`Makefile`) для автоматизации выполнения команд:

1. Сборка Docker-контейнера.
2. Генерация документации.
3. Запуск форматирования кода.
4. Запуск статического анализа кода (выявление ошибок типов и форматирования кода).
5. Запуск автоматических тестов.
6. Запуск всех функций поддержки качества кода (форматирование, линтеры, автотесты).

Инструкция по запуску этих команд находится в файле `README.md`.

Тестирование
============

Для запуска автоматических тестов выполните команду:

.. code-block:: console

    docker compose run app pytest --cov=/src --cov-report html:htmlcov --cov-report term --cov-config=/src/tests/.coveragerc -vv

Также существует аналогичная `make`-команда:

.. code-block:: console

    make test

Отчет о тестировании находится в файле `src/htmlcov/index.html`.

Документация к исходному коду
*****************************

.. toctree::
   :maxdepth: 2
   :caption: Содержимое:

Запуск приложения
=================
.. automodule:: main
   :members:

.. currentmodule:: main
.. autofunction:: process_input

Чтение входного файла
=====================
.. automodule:: readers.reader
   :members:

Генерация выходного файла
=========================
.. automodule:: renderer
   :members:

Модели объектов
===============

.. automodule:: formatters.models
    :members:
