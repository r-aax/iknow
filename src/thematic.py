from complex_theme import ComplexTheme
from html import *

#===================================================================================================

class Thematic:
    """
    Thematic.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, theme, title):
        """
        Init thematic.

        Parameters
        ----------
        theme : ComplexTheme
            Complex theme.
        title : str
            Title of thematic.
        """

        self.__theme = theme
        self.__title = title
        self.__results = []

        theme.thematics.append(self)

#---------------------------------------------------------------------------------------------------

    @property
    def theme(self):
        """
        Get theme.

        Returns
        -------
        ComplexTheme
            Complex theme.
        """

        return self.__theme

#---------------------------------------------------------------------------------------------------

    @property
    def title(self):
        """
        Get title.

        Returns
        -------
        str
            Title.
        """

        return self.__title

#---------------------------------------------------------------------------------------------------

    @property
    def results(self):
        """
        Get results.

        Returns
        -------
        [ResearchResult]
            List of research results.
        """

        return self.__results

#---------------------------------------------------------------------------------------------------

    def print(self):
        """
        Print function.
        """

        print(f'Thematic: {self.title}')

        for result in self.results:
            print(' - ', result)

#---------------------------------------------------------------------------------------------------

    def publications_count(self, year):
        """
        Get publications count in year.

        Parameters
        ----------
        year : int
            Year.

        Returns
        -------
        int
            Count of publications.
        """

        rs = [r for r in self.results if r.year == year]

        cnt = 0

        for r in rs:
            if type(r.publications_count) is int:
                cnt = cnt + r.publications_count

        return cnt

#---------------------------------------------------------------------------------------------------

    def year_results_html(self, year):
        """
        Get HTML for results in year.

        Parameters
        ----------
        year : int
            Year.

        Returns
        -------
        str
            Year results in HTML form.
        """

        rs = [r for r in self.results if r.year == year]
        texts = [r.description_html() for r in rs]
        ol_text = ol(texts)
        publications_count = self.publications_count(year)
        publications_text = font(f' статьи: {publications_count}', color='indianred')
        sum_text = b(f'Суммарно:{publications_text}')

        return f'{sum_text}{ol_text}'

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
