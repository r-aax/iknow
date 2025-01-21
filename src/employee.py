from logging import exception

#===================================================================================================

class Employee:
    """
    Employee - person with tabel number.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, personal, tabel):
        """
        Init method.

        Parameters
        ----------
        personal : Person
            Personal data.
        tabel : str
            Tabel number.
        """

        self.__personal = personal
        self.__tabel = tabel

#---------------------------------------------------------------------------------------------------

    @property
    def personal(self):
        """
        Get personal data.

        Returns
        -------
        Person
            Personal data.
        """

        return self.__personal

#---------------------------------------------------------------------------------------------------

    @property
    def tabel(self):
        """
        Get tabel number.

        Returns
        -------
        set
            Tabel number.
        """

        if self.__tabel == '':
            raise exception(f'Employee: empty tabel number for {self.__personal.surname}')

        return self.__tabel

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
