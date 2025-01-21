from complex_theme import ComplexTheme

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

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
