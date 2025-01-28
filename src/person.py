from datetime import date
from logging import exception
import utils

#===================================================================================================

class Person:
    """
    Person class.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self,
                 name, patronymic, surname,
                 birthdate=None,
                 snils='', inn=''):
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
        birthdate : date | int | None
            Date of birth or just year.
        snils : str
            SNILS number (11 characters).
        inn : str
            INN number (12 characters).
        """

        self.__name = name
        self.__patronymic = patronymic
        self.__surname = surname
        self.__birthdate = birthdate
        self.__snils = snils
        self.__inn = inn

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
    def surname_name_patronymic(self):
        """
        Get surname, name and patronymic at once.

        Returns
        -------
        str
            String.
        """

        return f'{self.surname} {self.name} {self.patronymic}'

#---------------------------------------------------------------------------------------------------

    @property
    def birthdate(self):
        """
        Get birthdate.

        Returns
        -------
        date
            Birthdate.
        """

        if not type(self.__birthdate) is date:
            raise exception(f'Person: {self.surname} has no full birthdate')

        return self.__birthdate

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
            raise exception(f'Person: date is in wrong format: {d}')

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
        elif type(d) is int:
            return d
        else:
            raise exception(f'Person: date for {self.__surname} is in wrong format: {d}')

#---------------------------------------------------------------------------------------------------

    def age_in_the_end_of_year(self, y=0):
        """
        Age to the end of year "y".

        Parameters
        ----------
        y : int
            Target year.

        Returns
        -------
        int
            Age.
        """

        if y == 0:
            y = date.today().year

        return y - self.year

#---------------------------------------------------------------------------------------------------

    @property
    def has_snils(self):
        """
        Check if person has SNILS.

        Returns
        -------
        bool
            True - if has SNILS,
            False - if not.
        """

        return self.__snils != ''

#---------------------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------------------

    @property
    def has_inn(self):
        """
        Check if person has INN.

        Returns
        -------
        bool
            True - if person has INN,
            False - if person has no INN.
        """

        return self.__inn != ''

#---------------------------------------------------------------------------------------------------

    @property
    def inn(self):
        """
        Get INN.

        Returns
        -------
        str
            INN string.
        """

        if len(self.__inn) != 12:
            raise exception('Person: INN number must contain 12 characters')

        return self.__inn

#---------------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        String representation.

        Returns
        -------
        str
            String.
        """

        return f'{self.surname} {self.name} {self.patronymic}'

#===================================================================================================

def mean_age_in_the_end_of_year(ps, y=0):
    """
    Mean age in the end of year.

    Parameters
    ----------
    ps : [Person]
        People list.
    y : int
        Year.

    Returns
    -------
    float
        Mean age in the end of year.
    """

    return sum([p.age_in_the_end_of_year(y) for p in ps]) / len(ps)

#---------------------------------------------------------------------------------------------------

def percent_le_age_in_the_end_of_year(ps, lim, y=0):
    """
    Percent of people whose age is less or equal of limit in the end of given year.

    Parameters
    ----------
    ps : [Person]
        People list.
    lim : int
        Limit.
    y : int
        Year for age calculating.

    Returns
    -------
    float
        Percent of young people.
    """

    cnt = 0

    for p in ps:
        if p.age_in_the_end_of_year(y) <= lim:
            cnt += 1

    return (cnt / len(ps)) * 100.0

#---------------------------------------------------------------------------------------------------

def all_snils_are_different(ps):
    """
    Check different snils.

    Parameters
    ----------
    ps : [Person]
        People list.

    Returns
    -------
    bool
        True - if all elements have different snils (or have empty snils),
        False - two people with equal snils are found.

    """

    r = utils.find_keys_have_same_values([p.surname for p in ps if p.has_snils],
                                         [p.snils for p in ps if p.has_snils])

    if r == []:
        return True
    else:
        print(f'People: {r[0]} and {r[1]} have the same SNILS {r[2]}')
        return False

#---------------------------------------------------------------------------------------------------

def all_inn_are_different(ps):
    """
    Check if people have different INN.

    Parameters
    ----------
    ps : [Person]
        People list.

    Returns
    -------
    bool
        True - if all elements have different inn (or have empty inn),
        false - two people with equal inn are found.
    """

    r = utils.find_keys_have_same_values([p.surname for p in ps if p.has_inn],
                                         [p.inn for p in ps if p.has_inn])

    if r == []:
        return True
    else:
        print(f'People: {r[0]} and {r[1]} have the same INN {r[2]}')
        return False

#---------------------------------------------------------------------------------------------------

def check(ps):
    """
    Check persons.

    Parameters
    ----------
    ps : [Person]

    Returns
    -------
    bool
        True - all check are completed successfully,
        False - some checks are failed.
    """

    check_snils = all_snils_are_different(ps)
    check_inn = all_inn_are_different(ps)

    return check_snils and check_inn

#===================================================================================================

if __name__ == '__main__':

    # single person
    p = Person('Ivan', 'Peter', 'Sidorov',
               date(1982, 7, 25), '12345678901')
    assert p.name == 'Ivan'
    assert p.patronymic == 'Peter'
    assert p.surname == 'Sidorov'
    assert p.year == 1982
    assert p.snils == '12345678901'

    # collection
    ps = [Person('Ivan', 'Ivan', 'Ivanov',
                 2000, '12345678901', '123456789012'),
          Person('Peter', 'Peter', 'Petrov',
                 1999, '12345678901', '123456789012')]
    assert not all_snils_are_different(ps)
    assert not all_inn_are_different(ps)
    assert not check(ps)

#===================================================================================================
