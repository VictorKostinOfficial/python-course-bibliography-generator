"""
Фикстуры для моделей объектов (типов источников).
"""
import pytest

from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, DissertationModel, \
    ArticlesNewspaperModel


@pytest.fixture
def book_model_fixture() -> BookModel:
    """
    Фикстура модели книги.

    :return: BookModel
    """

    return BookModel(
        authors="Иванов И.М.",
        title="Наука как искусство",
        edition="3-е",
        city="СПб.",
        publishing_house="Просвещение",
        year=2020,
        pages=999,
    )


@pytest.fixture
def internet_resource_model_fixture() -> InternetResourceModel:
    """
    Фикстура модели интернет-ресурса.

    :return: InternetResourceModel
    """

    return InternetResourceModel(
        article="Наука как искусство",
        website="Ведомости",
        link="https://www.vedomosti.ru",
        access_date="01.01.2021",
    )


@pytest.fixture
def articles_collection_model_fixture() -> ArticlesCollectionModel:
    """
    Фикстура модели сборника статей.

    :return: ArticlesCollectionModel
    """

    return ArticlesCollectionModel(
        authors="Иванов И.М.",
        article_title="Наука как искусство",
        collection_title="Сборник научных трудов",
        city="СПб.",
        publishing_house="АСТ",
        year=2020,
        pages="25-30",
    )

@pytest.fixture
def dissertation_collection_model_fixture() -> DissertationModel:
    """
    Фикстура модели диссертаций.

    :return: DissertationModel
    """

    return DissertationModel(
        authors="Иванов И.М.",
        article_title="Наука как искусство",
        phd_or_cand="д-р. / канд.",
        branch_of_sciences="экон.",
        specialty_code="111",
        publishing_city="Пермь",
        publishing_year=2023,
        pages="1",
    )

@pytest.fixture
def newspaper_collection_model_fixture() -> ArticlesNewspaperModel:
    """
    Фикстура модели газеты.

    :return: ArticlesNewspaperModel
    """

    return ArticlesNewspaperModel(
        authors="Иванов И.М.",
        article_title="Наука как искусство",
        newspaper_name="Новая Газета",
        publishing_year=2023,
        newspaper_publishing_date="01.01",
        article_number=1,
    )

