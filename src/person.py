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
                 birthdate,
                 snils):
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
        birthdate : date | int
            Date of birth or just year.
        snils : str
            SNILS number.
        """

        self.__name = name
        self.__patronymic = patronymic
        self.__surname = surname
        self.__birthdate = birthdate
        self.__snils = snils

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
    def date_str(self):
        """
        Get date in string format.

        Returns
        -------
        str
            Date in string format.
        """

        d = self.__birthdate

        if type(d) is date:
            return f'{d.day:02d}.{d.month:02d}.{d.year:02d}'
        else:
            raise exception('Person: date is in wrong format')

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

        d = self.__birthdate

        if type(d) is date:
            return d.year
        else:
            return d

#---------------------------------------------------------------------------------------------------

    @property
    def has_snils(self):
        """
        Check if person has SNILS.

        Returns
        -------
        bool
            True - if has SNILS, False - if not.
        """

        return self.__snils != ''

# ---------------------------------------------------------------------------------------------------

    @property
    def snils(self):
        """
        Get SNILS.

        Returns
        -------
        str
            SNILS.
        """

        if len(self.__snils) != 11:
            raise exception('Person: SNILS number must contain 11 digits')

        return self.__snils

#===================================================================================================

if __name__ == '__main__':
    p = Person('Иван', 'Петрович', 'Сидоров',
               date(1982, 7, 25), '12345678901')
    assert p.name == 'Иван'
    assert p.patronymic == 'Петрович'
    assert p.surname == 'Сидоров'
    assert p.year == 1982
    assert p.snils == '12345678901'

#===================================================================================================
