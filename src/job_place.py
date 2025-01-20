from logging import exception

#===================================================================================================

class JobPlace:
    """
    Job place.
    Organization or subdivision.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, name, short_name, parent=None):
        """
        Init job.

        Parameters
        ----------
        name : str
            Name of job.
        short_name : str
            Short name.
        parent : Job
            Link to parent job (or None for head).
        """

        self.__name = name
        self.__short_name = short_name
        self.__parent = parent

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
            raise exception('JobPlace: empty name')

        return self.__name

#---------------------------------------------------------------------------------------------------

    @property
    def short_name(self):
        """
        Get short name.

        Returns
        -------
        str
            Short name.
        """

        if self.__short_name == '':
            raise exception('JobPlace: empty short name')

        return self.__short_name

#---------------------------------------------------------------------------------------------------

    @property
    def parent(self):
        """
        Get parent.

        Returns
        -------
        Job | None
            Parent.
        """

        return self.__parent

#---------------------------------------------------------------------------------------------------

    @property
    def is_head(self):
        """
        Check if job has head (no parent).

        Returns
        -------
        bool
            True - if job is head,
            False - if job is not head.
        """

        return self.parent is None

#---------------------------------------------------------------------------------------------------

    def full_name(self):
        """
        Full name with all chain up to head.

        Returns
        -------
        str
            Full name.
        """

        if self.is_head:
            return self.name
        else:
            return f'{self.name}, {self.parent.full_name()}'

#===================================================================================================

if __name__ == '__main__':
    org = JobPlace('Organization', 'Org')
    dep = JobPlace('Sales department', 'SD', org)
    assert org.is_head
    assert not dep.is_head
    assert org.name == 'Organization'
    assert org.short_name == 'Org'
    assert dep.name == 'Sales department'
    assert dep.short_name == 'SD'
    assert dep.full_name() == 'Sales department, Organization'

#===================================================================================================
