from employee import Employee
from thematic import Thematic
from html import *

#===================================================================================================

class ResearchResult:
    """
    Result of research.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, thematic, year, title, responsible, comment,
                 publications_count='не определено'):
        """
        Init research result.

        Parameters
        ----------
        thematic : Thematic
            Thematic.
        year : int
            Year.
        title : str
            Title of result.
        responsible : Employee
            Responsible employee.
        comment : str
            Arbitrary comment.
        publications_count : int
            Count of publications.
        """

        self.__thematic = thematic
        self.__year = year
        self.__title = title
        self.__responsible = responsible
        self.__comment = comment
        self.__publications_count = publications_count

        thematic.results.append(self)

#---------------------------------------------------------------------------------------------------

    @property
    def thematic(self):
        """
        Get thematic.

        Returns
        -------
        Thematic
            Thematic.
        """

        return self.__thematic

#---------------------------------------------------------------------------------------------------

    @property
    def year(self):
        """
        Get year.

        Returns
        -------
        int
            Year.
        """

        return self.__year

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
    def responsible(self):
        """
        Get responsible.

        Returns
        -------
        Employee
            Responsible.
        """

        return self.__responsible

#---------------------------------------------------------------------------------------------------

    @property
    def comment(self):
        """
        Get comment.

        Returns
        -------
        str
            Comment.
        """

        return self.__comment

#---------------------------------------------------------------------------------------------------

    @property
    def publications_count(self):
        """
        Get publications count.

        Returns
        -------
        int
            Publications count.
        """

        return self.__publications_count

#---------------------------------------------------------------------------------------------------

    @property
    def is_rid(self):
        """
        Check if result is result of intellectual activity.

        Returns
        -------
        bool
            True - if result of intellectual activity,
            False - if it is common result.
        """

        return self.title.startswith('База данных') or self.title.startswith('Программа для ЭВМ')

#---------------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        String representation.

        Returns
        -------
        str
            String.
        """

        return f'{self.year}: {self.title} ({self.responsible}), ({self.comment})'

#---------------------------------------------------------------------------------------------------

    def description_html(self):
        """
        Get description in HTML format.

        Returns
        -------
        str
            HTML description.
        """

        rid_pref = ''
        if self.is_rid:
            rid_pref = b(font('РИД: ', color='darkgreen'))
        resp_html = font(str(self.responsible), color='steelblue')
        main_html = f'{rid_pref}{self.title}<br>({resp_html}) ({self.comment})'
        cnt_html = font(f'(статьи: {self.publications_count})', color='indianred')

        return f'{main_html}<br>{cnt_html}<br><br>'

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
