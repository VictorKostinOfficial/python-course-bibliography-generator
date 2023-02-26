"""
Описание схем объектов (DTO).
"""

from typing import Optional

from pydantic import BaseModel, Field


class BookModel(BaseModel):
    """
    Модель книги:

    .. code-block::

        BookModel(
            authors="Иванов И.М., Петров С.Н.",
            title="Наука как искусство",
            edition="3-е",
            city="СПб.",
            publishing_house="Просвещение",
            year=2020,
            pages=999,
        )
    """

    authors: str
    title: str
    edition: Optional[str]
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class InternetResourceModel(BaseModel):
    """
    Модель интернет ресурса:

    .. code-block::

        InternetResourceModel(
            article="Наука как искусство",
            website="Ведомости",
            link="https://www.vedomosti.ru/",
            access_date="01.01.2021",
        )
    """

    article: str
    website: str
    link: str
    access_date: str


class ArticlesCollectionModel(BaseModel):

    """
    Модель сборника статей:

    .. code-block::

        ArticlesCollectionModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            collection_title="Сборник научных трудов",
            city="СПб.",
            publishing_house="АСТ",
            year=2020,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    collection_title: str
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: str


class DissertationModel(BaseModel):

    """
    Модель диссертации:

    .. code-block::

        DissertationModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            phd_or_cand="д-р. / канд."
            branch_of_sciences="экон."
            specialty_code="01.01.01"
            publishing_city="СПб."
            publishing_year=2020
            pages="199-200"

        )
    """

    authors: str
    article_title: str
    phd_or_cand: str
    branch_of_sciences: str
    specialty_code: str
    publishing_city: str
    publishing_year: int = Field(..., gt=0)
    pages: str


class ArticlesNewspaperModel(BaseModel):

    """
    Модель газетной статьи:

    .. code-block::

        ArticlesNewspaperModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            newspaper_name="Южный Урал"
            publishing_year=1980
            newspaper_publishing_date="01.10"
            article_number=5
        )
    """

    authors: str
    article_title: str
    newspaper_name: str
    publishing_year: int = Field(..., gt=0)
    newspaper_publishing_date: str
    article_number: int = Field(..., gt=0)
