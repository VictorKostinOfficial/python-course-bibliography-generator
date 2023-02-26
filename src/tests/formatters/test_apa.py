"""
Тестирование функций оформления списка источников по ГОСТ Р 7.0.5-2008.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    DissertationModel,
    ArticlesNewspaperModel,
)
from formatters.styles.apa import (
    APABook,
    APAInternetResource,
    APACollectionArticle,
    APANewspaperArticle,
    APADissertation,
)


class TestAPA:
    """
    Тестирование оформления списка источников согласно ГОСТ Р 7.0.5-2008.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = APABook(book_model_fixture)

        assert model.formatted == "Иванов И.М. (2020). Наука как искусство."

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = APAInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Ведомости. (n.d.). Наука как искусство. https://www.vedomosti.ru."
        )

    def test_dissertation(
        self, dissertation_collection_model_fixture: DissertationModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param DissertationModel dissertation_collection_model_fixture: Фикстура модели диссертации
        :return:
        """

        model = APADissertation(dissertation_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М. (2023). Наука как искусство [д-р. / канд. экон. наук]. 1 с."
        )

    def test_newspaper(
        self, newspaper_collection_model_fixture: ArticlesNewspaperModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param DissertationModel newspaper_collection_model_fixture: Фикстура модели диссертации
        :return:
        """

        model = APANewspaperArticle(newspaper_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М. (2023, 01.01.). Наука как искусство. Новая Газета. pp. 1 A."
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели газеты
        :return:
        """

        model = APACollectionArticle(articles_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М. (2020). Наука как искусство in Сборник научных трудов (p. 25-30)."
        )
