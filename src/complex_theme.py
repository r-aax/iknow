from worksheet_line import WorksheetLine
import outlay_tree

#===================================================================================================

class ComplexTheme:
    """
    Complex theme.
    """

    #-----------------------------------------------------------------------------------------------

    def __init__(self, title):
        """
        Init complex theme.

        Parameters
        ----------
        title : str
            Title.
        """

        self.__title = title
        self.__thematics = []
        self.goal = ''
        self.actuality = ''
        self.manager = None
        self.deputy = None
        self.bdw_need = 0
        self.knl_need = 0
        self.clk_need = 0
        self.icl_need = 0
        self.a100_need = 0
        self.outlay = None

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
    def short_title(self):
        """
        Get short title.

        Returns
        -------
        str
            Short title.
        """

        return self.title[0:7]

    #-----------------------------------------------------------------------------------------------

    @property
    def thematics(self):
        """
        Get thematics.

        Returns
        -------
        [Thematic]
            Thematics list.
        """

        return self.__thematics

    #-----------------------------------------------------------------------------------------------

    def all_thematics_titles(self):
        """
        Get all thematics titles.

        Returns
        -------
        str
            All thematics titles in single string.
        """

        return ', '.join([th.title for th in self.thematics])

    #-----------------------------------------------------------------------------------------------

    def print(self):
        """
        Print.
        """

        print(f'Complex theme : {self.title}')

        for thematic in self.thematics:
            thematic.print()

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

        return sum([th.ind_doctors(y) for th in self.thematics])

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

        return sum([th.ind_candidates(y) for th in self.thematics])

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

        return sum([th.ind_rids(y) for th in self.thematics])

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

        return sum([th.ind_publications(y) for th in self.thematics])

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
