#===================================================================================================

class ComplexTheme:
    """
    Complex theme.
    """

#---------------------------------------------------------------------------------------------------

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
    def short_title(self):
        """
        Get short title.

        Returns
        -------
        str
            Short title.
        """

        return self.title[0:7]

#---------------------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------------------

    def all_thematics_titles(self):
        """
        Get all thematics titles.

        Returns
        -------
        str
            All thematics titles in single string.
        """

        return ', '.join([th.title for th in self.thematics])

#---------------------------------------------------------------------------------------------------

    def print(self):
        """
        Print.
        """

        print(f'Complex theme : {self.title}')

        for thematic in self.thematics:
            thematic.print()

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
