import person

#===================================================================================================

class People:
    """
    People class - set of persons.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self):
        """
        Init.
        """

        self.__v = []

#---------------------------------------------------------------------------------------------------

    def add(self, x):
        """
        Add person or list of people.

        Parameters
        ----------
        x : Person | [Person]
            Person or list of persons.
        """

        if type(x) is list:
            for xi in x:
                self.add(xi)
        else:
            self.__v.append(x)

#---------------------------------------------------------------------------------------------------

    def check(self):
        """
        Check people correctness.

        Returns
        -------
        bool
            True - if people list is correct, False - if there are some problems.
        """

        # Check all people have different SNILS.
        d = dict()
        for x in self.__v:
            if x.has_snils:
                s = d.get(x.snils)
                if not s is None:
                    print(f'People: {s} and {x.surname} have the same SNILS {x.snils}')
                    return False
                else:
                    d[x.snils] = x.surname

        return True

#===================================================================================================

if __name__ == '__main__':
    a = person.Person('Ivan', 'Ivan', 'Ivanov',
                      2000, '12345678901')
    b = person.Person('Peter', 'Peter', 'Petrov',
                      1999, '12345678901')
    p = People()
    p.add([a, b])
    assert not p.check()

#===================================================================================================
