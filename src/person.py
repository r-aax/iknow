from datetime import date
from logging import exception

from pkg_resources import working_set

import utils

#===================================================================================================

class Person:
    """
    Person class.
    """

    #-----------------------------------------------------------------------------------------------

    def __init__(self,
                 name, patronymic, surname,
                 name_en='', patronymic_en='', surname_en='',
                 birthdate=None,
                 academic_degree='', academic_title='',
                 snils='', inn='', passport='',
                 phone='', email='',
                 orcid='', wos='', scopus='', elibrary=''):
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
        name_en : str
            Name (english).
        patronymic_en : str
            Patronymic name (english).
        surname_en : str
            Surname (english).
        birthdate : date | int | None
            Date of birth or just year.
        academic_degree : str
            Academic degree.
        academic_title : str
            Academic title.
        snils : str
            SNILS number (11 characters).
        inn : str
            INN number (12 characters).
        passport : str
            Passport.
        phone : str
            Phone number.
        email : str
            E-mail.
        orcid : str
            ORCID.
        wos : str
            Web of Science identifier.
        scopus : str
            SCOPUS identifier.
        elibrary : str
            e-library (spin-code / author id).
        """

        self.__name = name
        self.__patronymic = patronymic
        self.__surname = surname
        self.__name_en = name_en
        self.__patronymic_en = patronymic_en
        self.__surname_en = surname_en
        self.__birthdate = birthdate
        self.__academic_degree = academic_degree
        self.__academic_title = academic_title
        self.__snils = snils
        self.__inn = inn
        self.__passport = passport
        self.__phone = phone
        self.__email = email
        self.__orcid = orcid
        self.__wos = wos
        self.__scopus = scopus
        self.__elibrary = elibrary

    #-----------------------------------------------------------------------------------------------

    def name(self, language='ru'):
        """
        Get name.

        Parameters
        ----------
        language : str
            Language.

        Returns
        -------
        str
            Name.
        """

        if language == 'ru':
            return self.__name
        elif language == 'en':
            return self.__name_en
        else:
            raise exception('Person: wrong language')

    #-----------------------------------------------------------------------------------------------

    def name_first_letter(self, language='ru'):
        """
        Get first letter of name.

        Parameters
        ----------
        language : str
            Language.

        Returns
        -------
        str
            First letter of name or empty.
        """

        n = self.name(language)

        if n == '':
            return ''
        else:
            return n[0]

    #-----------------------------------------------------------------------------------------------

    def patronymic(self, language='ru'):
        """
        Get patronymic.

        Parameters
        ----------
        language : str
            Language.

        Returns
        -------
        str
            Patronymic.
        """

        if language == 'ru':
            return self.__patronymic
        elif language == 'en':
            return self.__patronymic_en
        else:
            raise exception('Person: wrong language')

    #-----------------------------------------------------------------------------------------------

    def patronymic_first_letter(self, language='ru'):
        """
        Get first letter of patronymic.

        Parameters
        ----------
        language : str
            Language.

        Returns
        -------
        str
            First letter of patronymic.
        """

        p = self.patronymic(language)

        if p == '':
            return ''
        else:
            return p[0]

    #-----------------------------------------------------------------------------------------------

    def surname(self, language='ru'):
        """
        Get surname.

        Parameters
        ----------
        language : str
            Language.

        Returns
        -------
        str
            Surname.
        """

        if language == 'ru':
            if self.__surname == '':
                raise exception('Person: empty surname')
            return self.__surname
        elif language == 'en':
            if self.__surname_en == '':
                raise exception(f'Person: empty english surname for {self.__surname}')
            return self.__surname_en
        else:
            raise exception('Person: wrong language')

    #-----------------------------------------------------------------------------------------------

    def surname_first_letter(self, language='ru'):
        """
        Get surname first letter.

        Parameters
        ----------
        language : str
            Language.

        Returns
        -------
        str
            First letter of surname.
        """

        return self.surname(language)[0]

    #-----------------------------------------------------------------------------------------------

    def surname_name_patronymic(self, language='ru'):
        """
        Get surname, name and patronymic at once.

        Parameters
        ----------
        language : str
            Language.

        Returns
        -------
        str
            String.
        """

        return f'{self.surname(language)} {self.name(language)} {self.patronymic(language)}'

    #-----------------------------------------------------------------------------------------------

    def n_p_surname(self, language='ru'):
        """
        Get I. I. Ivanov view of person.

        Parameters
        ----------
        language : str
            Language.

        Returns
        -------
        str
            View of person.
        """

        nfl = self.name_first_letter(language)
        pfl = self.patronymic_first_letter(language)
        s = self.surname(language)

        if nfl == '':
            if pfl == '':
                return f'{s}'
            else:
                raise Exception(f'Person {s} has no first name, but has patronymic')
        else:
            if pfl == '':
                return f'{nfl}. {s}'
            else:
                return f'{nfl}. {pfl}. {s}'

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

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
        elif type(d) is int:
            return f'{d}'
        else:
            raise exception(f'Person: date for {self.__surname} is in wrong format: {d}')

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

    def academic_degree(self, f=''):
        """
        Get academic degree in given format.

        Parameters
        ----------
        f : str
            Format.

        Returns
        -------
        str
            Academic degree.
        """

        d = self.__academic_degree

        if f == '':
            return d

        if f == 'A':
            if d == '':
                return ''
            elif d == 'ктн':
                return 'Кандидат технических наук'
            elif d == 'дтн':
                return 'Доктор технических наук'
            elif d == 'кфмн':
                return 'Кандидат физико-математических наук'
            elif d == 'дфмн':
                return 'Доктор физико-математических наук'
            elif d == 'кхн':
                return 'Кандидат химических наук'
            else:
                raise Exception(f'unexpected academic degree {d}')

        raise Exception(f'unexpected format of academic degree {f}')

    #-----------------------------------------------------------------------------------------------

    def academic_title(self, f):
        """
        Get academic title in given format.

        Parameters
        ----------
        f : str
            Format.

        Returns
        -------
        str
            Academic title.
        """

        t = self.__academic_title

        if f == '':
            return t

        if f == 'A':
            if t == '':
                return ''
            elif t == 'д':
                return 'Доцент'
            elif t == 'п':
                return 'Профессор'
            elif t == 'ч':
                return 'Член-корреспондент РАН'
            elif t == 'а':
                return 'Академик РАН'
            else:
                raise Exception(f'unexpected academic title {t}')

        raise Exception(f'unexpected format of academic title {f}')

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

    @property
    def orcid(self):
        """
        ORCID.

        Returns
        -------
        str
            ORCID.
        """

        return self.__orcid

    #-----------------------------------------------------------------------------------------------

    @property
    def wos(self):
        """
        Web of Science identifier.

        Returns
        -------
        str
            Web of Science identifier.
        """

        return self.__wos

    #-----------------------------------------------------------------------------------------------

    @property
    def scopus(self):
        """
        SCOPUS identifier.

        Returns
        -------
        str
            SCOPUS identifier.
        """

        return self.__scopus

    #-----------------------------------------------------------------------------------------------

    @property
    def elibrary(self):
        """
        E-library data (spin-code / author id).

        Returns
        -------
        str
            E-library data (spin-code / author id).
        """

        return self.__elibrary

    #-----------------------------------------------------------------------------------------------

    @property
    def elibrary_spin(self):
        """
        E-library spin-code.

        Returns
        -------
        str
            E-library spin-code.
        """

        e = self.elibrary

        if e == '':
            return ''
        else:
            s = e.split('/')
            if len(s) > 0:
                return s[0]
            else:
                return ''

    #-----------------------------------------------------------------------------------------------

    @property
    def elibrary_id(self):
        """
        E-library ID.

        Returns
        -------
        str
            E-library ID.
        """

        e = self.elibrary

        if e == '':
            return ''
        else:
            s = e.split('/')
            if len(s) > 1:
                return s[1]
            else:
                return ''

    #-----------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        String representation.

        Returns
        -------
        str
            String.
        """

        return f'{self.surname()} {self.name()} {self.patronymic()}'

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
               birthdate=date(1982, 7, 25), snils='12345678901')
    assert p.name() == 'Ivan'
    assert p.patronymic() == 'Peter'
    assert p.surname() == 'Sidorov'
    assert p.year == 1982
    assert p.snils == '12345678901'

    # collection
    ps = [Person('Ivan', 'Ivan', 'Ivanov',
                 birthdate=2000, snils='12345678901', inn='123456789012'),
          Person('Peter', 'Peter', 'Petrov',
                 birthdate=1999, snils='12345678901', inn='123456789012')]
    assert not all_snils_are_different(ps)
    assert not all_inn_are_different(ps)
    assert not check(ps)

#===================================================================================================
