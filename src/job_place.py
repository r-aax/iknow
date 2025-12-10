from logging import exception

#===================================================================================================

class JobPlace:
    """
    Job place.
    Organization or subdivision.
    """

    #-----------------------------------------------------------------------------------------------

    def __init__(self, name, short_name, parent=None, name_r='', link=''):
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
        name_r : str
            Name in other form
        """

        self.__name = name
        self.__short_name = short_name
        self.__parent = parent
        self.__name_r = name_r
        self.__link = link

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

    @property
    def name_r(self):
        """
        Get name in other form.

        Returns
        -------
        str
            Name in other form.
        """

        return self.__name_r

    #-----------------------------------------------------------------------------------------------

    @property
    def link(self):
        """
        Get link.

        Returns
        -------
        str
            Link.
        """

        return self.__link

    #-----------------------------------------------------------------------------------------------

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

    #-----------------------------------------------------------------------------------------------

    @property
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

    #-----------------------------------------------------------------------------------------------

    @property
    def half_full_name(self):
        """
        Name up to root but without root
        (all subdivisions but root, because root is organization).

        Returns
        -------
        str
            Half full name.
        """

        if self.parent.is_head:
            return self.name
        else:
            return f'{self.name}, {self.parent.half_full_name}'

    #-----------------------------------------------------------------------------------------------

    @property
    def affiliation_html(self):
        """
        Affiliation HTML.

        Returns
        -------
        str
            Affiliation HTML.
        """

        return f'[<a href="#" title="{self.name} ({self.link})">{self.short_name}</a>]'

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
