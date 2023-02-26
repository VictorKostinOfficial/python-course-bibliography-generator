"""
Запуск приложения.
"""
from enum import Enum, unique

import click

from formatters.styles.apa import APACitationFormatter
from formatters.styles.gost import GOSTCitationFormatter
from logger import get_logger
from readers.reader import SourcesReader
from renderer import Renderer
from settings import INPUT_FILE_PATH, OUTPUT_FILE_PATH, OUTPUT_FILE_PATH_APA

logger = get_logger(__name__)


@unique
class CitationEnum(Enum):
    """
    Поддерживаемые типы цитирования.
    """

    GOST = "gost"  # ГОСТ Р 7.0.5-2008
    MLA = "mla"  # Modern Language Association
    APA = "apa"  # American Psychological Association


@click.command()
@click.option(
    "--citation",
    "-c",
    "citation",
    type=click.Choice([item.name for item in CitationEnum], case_sensitive=False),
    default=CitationEnum.GOST.name,
    show_default=True,
    help="Стиль цитирования",
)
@click.option(
    "--path_input",
    "-pi",
    "path_input",
    type=str,
    default=INPUT_FILE_PATH,
    show_default=True,
    help="Путь к входному файлу",
)
@click.option(
    "--path_output",
    "-po",
    "path_output",
    type=str,
    default=OUTPUT_FILE_PATH,
    show_default=True,
    help="Путь к выходному файлу",
)
def process_input(
    citation: str = CitationEnum.GOST.name,
    path_input: str = INPUT_FILE_PATH,
    path_output: str = OUTPUT_FILE_PATH,
    path_output_apa: str = OUTPUT_FILE_PATH_APA,
) -> None:
    """
    Генерация файла Word с оформленным библиографическим списком.

    :param str citation: Стиль цитирования
    :param str path_input: Путь к входному файлу
    :param str path_output: Путь к выходному файлу для GHOST
    :param str path_output_apa: Путь к выходному файлу для APA 7th
    """

    logger.info(
        """Обработка команды с параметрами:
        - Стиль цитирования: %s.
        - Путь к входному файлу: %s.
        - Путь к выходному файлу GHOST: %s.
        - Путь к выходному файлу APA: %s.""",
        citation,
        path_input,
        path_output,
        path_output_apa,
    )

    models = SourcesReader(path_input).read()
    formatted_models = tuple(
        str(item) for item in GOSTCitationFormatter(models).format()
    )

    formatted_models_apa = tuple(
        str(item) for item in APACitationFormatter(models).format()
    )

    logger.info("Генерация выходных файлов ...")
    Renderer(formatted_models).render(path_output)
    Renderer(formatted_models_apa).render(path_output_apa)

    logger.info("Команда успешно завершена.")


if __name__ == "__main__":
    try:
        # запуск обработки входного файла
        process_input()
    except Exception as ex:
        logger.error("При обработке команды возникла ошибка: %s", ex)
        raise
