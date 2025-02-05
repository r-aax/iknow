from logging import exception

#===================================================================================================

class Publication:
    """
    Publication class.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, authors_affiliations,
                 title, journal, year, volume, issue, pages,
                 doi, extern_link,
                 support):
        """
        Publication.

        Parameters
        ----------
        authors_affiliations : [(Person, [JobPlace])]
            List of tuples, each tuple performs author and its affiliation.
        title : str
            Title.
        journal : Journal
            Journal.
        year : int
            Year.
        volume : str
            Volume (may have various view).
        issue : int
            Issue.
        pages : str
            Pages.
        doi : str
            DOI.
        extern_link : str
            Extern link.
        support : str
            Financial support string.
        """

        self.__authors_affiliations = authors_affiliations
        self.__title = title
        self.__journal = journal
        self.__year = year
        self.__volume = volume
        self.__issue = issue
        self.__pages = pages
        self.__doi = doi
        self.__extern_link = extern_link
        self.__support = support

#---------------------------------------------------------------------------------------------------

    @property
    def authors_affiliations(self):
        """
        Get authors affiliations.

        Returns
        -------
        [(Person, [JobPlace])]
            Authors and affiliations information.
        """

        if self.__authors_affiliations == []:
            raise exception('Publication: no information about authors and affiliations')

        return self.__authors_affiliations

#---------------------------------------------------------------------------------------------------

    def authors_information(self):
        """
        Authors information.

        Returns
        -------
        str
            Authors information.
        """

        # join all authors.
        j = ', '.join([a[0].n_p_surname for a in self.authors_affiliations])

        return j + '.'

#---------------------------------------------------------------------------------------------------

    @property
    def title(self):
        """
        Get title.

        Returns
        -------
        str
            Title.
        """

        if self.__title == '':
            raise exception('Publication: empty title')

        return self.__title

#---------------------------------------------------------------------------------------------------

    @property
    def journal(self):
        """
        Get journal.

        Returns
        -------
        Journal
            Journal.
        """

        if self.__journal is None:
            raise exception('Publication: no journal')

        return self.__journal

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

        return self.__year

#---------------------------------------------------------------------------------------------------

    @property
    def volume(self):
        """
        Get volume.

        Returns
        -------
        str
            Volume.
        """

        if self.__volume == '':
            raise exception('Publication: empty volume')

        return self.__volume

#---------------------------------------------------------------------------------------------------

    @property
    def issue(self):
        """
        Get issue.

        Returns
        -------
        int
            Issue.
        """

        return self.__issue

#---------------------------------------------------------------------------------------------------

    @property
    def pages(self):
        """
        Get pages.

        Returns
        -------
        str
            Pages.
        """

        if self.__pages == '':
            raise exception('Publication: empty pages')

        return self.__pages

#---------------------------------------------------------------------------------------------------

    @property
    def doi(self):
        """
        Get DOI.

        Returns
        -------
        str
            DOI.
        """

        if self.__doi == '':
            raise exception('Publication: empty DOI')

        return self.__doi

#---------------------------------------------------------------------------------------------------

    @property
    def extern_link(self):
        """
        Extern link.

        Returns
        -------
        str
            Extern link.
        """

        return self.__extern_link

#---------------------------------------------------------------------------------------------------

    @property
    def support(self):
        """
        Get support string.

        Returns
        -------
        str
            Support string.
        """

        if self.__support == '':
            raise exception('Publication: empty support string')

        return self.__support

#---------------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        String representation.

        Returns
        -------
        str
            String representation.
        """

        at = f'{self.authors_information()} {self.title}'
        ji1 = f'{self.journal.name}, '
        ji2 = f'{self.year}, Т. {self.volume}, № {self.issue}, стр. {self.pages}'
        ji = ji1 + ji2

        return f'{at} // {ji}. DOI: {self.doi}'

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
