from complex_theme import ComplexTheme
from html import *

#===================================================================================================

class Thematic:
    """
    Thematic.
    """

    #-----------------------------------------------------------------------------------------------

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
        self.goal = ''
        self.actuality = ''
        self.resources = ''
        self.background = ''
        self.dict_ind_doctors = dict()
        self.dict_ind_candidates = dict()
        self.dict_ind_rids = dict()
        self.dict_ind_publications = dict()
        self.outlay = None

        theme.thematics.append(self)

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

    def print(self):
        """
        Print function.
        """

        print(f'Thematic: {self.title}')

        for result in self.results:
            print(' - ', result)

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

    def funding_part(self, year):
        """
        Get funding part.

        Parameters
        ----------
        year : int
            Year.

        Returns
        -------
        float
            Funding part.
        """

        rs = [r for r in self.results if r.year == year]

        return sum([r.funding_part for r in rs])

    #-----------------------------------------------------------------------------------------------

    def ind_doctors(self, y):
        """
        Get doctors count indicator.

        Parameters
        ----------
        y : int
            Year.

        Returns
        -------
        int
            Doctors count.
        """

        return self.dict_ind_doctors[y]

    #-----------------------------------------------------------------------------------------------

    def ind_candidates(self, y):
        """
        Get candidates count indicator.

        Parameters
        ----------
        y : int
            Year.

        Returns
        -------
        int
            Candidates count.
        """

        return self.dict_ind_candidates[y]

    #-----------------------------------------------------------------------------------------------

    def ind_rids(self, y):
        """
        Get rids count indicator.

        Parameters
        ----------
        y : int
            Year.

        Returns
        -------
        int
            Rids count.
        """

        rs = [r for r in self.results if r.is_rid and (r.year == y)]

        return len(rs)

    #-----------------------------------------------------------------------------------------------

    def ind_publications(self, y):
        """
        Get publications count indicator.

        Parameters
        ----------
        y : int
            Year.

        Returns
        -------
        int
            Publications count.
        """

        return self.dict_ind_publications[y]

    #-----------------------------------------------------------------------------------------------

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
