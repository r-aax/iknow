from logging import exception

#===================================================================================================

class JobTitle:
    """
    Job title.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, name, cat, cg, cu):
        """
        Name of position.

        Parameters
        ----------
        name : str
            Name.
        cat : str
            Category.
        cg : str
            CG.
        cu : str
            CU.
        """

        self.__name = name
        self.__cat = cat
        self.__cg = cg
        self.__cu = cu

#---------------------------------------------------------------------------------------------------

    @property
    def name(self):
        """
        Get name.

        Returns
        -------
        str
            Name.
        """

        if self.__name == '':
            raise exception('JobTitle: empty name')

        return self.__name

#---------------------------------------------------------------------------------------------------

    @property
    def full_cat(self):
        """
        Get full category.

        Returns
        -------
        str
            Full category.
        """

        return f'{self.__cat}/{self.__cg}/{self.__cu}'

#===================================================================================================

if __name__ == '__main__':
    t = JobTitle('lead researcher')
    assert t.name == 'lead researcher'

#===================================================================================================
