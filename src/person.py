from datetime import date
from logging import exception

#===================================================================================================

class Person:
    """
    Person class.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self,
                 name, patronymic, surname,
                 birthdate):
        """
        Init person.

        Parameters
        ----------
        name : str
            First name.
        patronymic : str
            Patronymic name.
        surname : str
            Surname.
        birthdate : date
            Date of birth.
        """

        self.__name = name
        self.__patronymic = patronymic
        self.__surname = surname
        self.__birthdate = birthdate

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
            raise exception('Person: empty name')

        return self.__name

#---------------------------------------------------------------------------------------------------

    @property
    def patronymic(self):
        """
        Get patronymic.

        Returns
        -------
        str
            Patronymic.
        """

        if self.__patronymic == '':
            raise exception('Person: empty patronymic')

        return self.__patronymic

#---------------------------------------------------------------------------------------------------

    @property
    def surname(self):
        """
        Get surname.

        Returns
        -------
        str
            Surname.
        """

        if self.__surname == '':
            raise exception('Person: empty surname')

        return self.__surname

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

        return self.__birthdate.year

#===================================================================================================

if __name__ == '__main__':
    p = Person('Иван', 'Петрович', 'Сидоров',
               date(1982, 7, 25))
    assert p.name == 'Иван'
    assert p.patronymic == 'Петрович'
    assert p.surname == 'Сидоров'
    assert p.year == 1982

#===================================================================================================
