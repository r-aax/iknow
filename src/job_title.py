from logging import exception

#===================================================================================================

class JobTitle:
    """
    Job title.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, name):
        """
        Name of position.

        Parameters
        ----------
        name : str
            Name.
        """

        self.__name = name

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

#===================================================================================================

if __name__ == '__main__':
    t = JobTitle('lead researcher')
    assert t.name == 'lead researcher'

#===================================================================================================
