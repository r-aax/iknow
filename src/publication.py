from logging import exception
from html import *

#===================================================================================================

class Publication:
    """
    Publication class.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, authors_affiliations,
                 title, journal, year, volume, issue, pages,
                 doi, extern_link,
                 support, language, comment='', problem=''):
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
        issue : str
            Issue.
        pages : str
            Pages.
        doi : str
            DOI.
        extern_link : str
            Extern link.
        support : str
            Financial support string.
        language : str
            Language ('ru', 'en').
        comment : str
            Comment.
        problem : str
            Problem.
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
        self.__language = language
        self.__comment = comment
        self.__problem = problem

#---------------------------------------------------------------------------------------------------

    @property
    def has_authors_affiliations(self):
        """
        Check if publication has authors and affiliation information.

        Returns
        -------
        bool
            True - if has information,
            False - otherwise.
        """

        return self.__authors_affiliations != []

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

    def authors_information(self, language='ru'):
        """
        Authors information.

        Parameters
        ----------
        language : str
            Language.

        Returns
        -------
        str
            Authors information.
        """

        # join all authors.
        j = ', '.join([a[0].n_p_surname(language) for a in self.authors_affiliations])

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

        return self.__support

#---------------------------------------------------------------------------------------------------

    @property
    def language(self):
        """
        Language.

        Returns
        -------
        str
            Language.
        """

        if not self.__language in ['ru', 'en']:
            raise exception(f'Publication: wrong language {self.__language}')

        return self.__language

#---------------------------------------------------------------------------------------------------

    @property
    def has_language(self):
        """
        Check if article has language.

        Returns
        -------
        bool
            True - if has language,
            False - if empty language.
        """

        return self.__language != ''

#---------------------------------------------------------------------------------------------------

    @property
    def comment(self):
        """
        Comment.

        Returns
        -------
        str
            Comment.
        """

        return self.__comment

#---------------------------------------------------------------------------------------------------

    @property
    def problem(self):
        """
        Problem.

        Returns
        -------
        str
            Problem.
        """

        return self.__problem

#---------------------------------------------------------------------------------------------------

    @property
    def is_bad(self):
        """
        Check if publication bad.

        Returns
        -------
        bool
            True - if publication is bad,
            False - otherwise.
        """

        return self.problem != ''

#---------------------------------------------------------------------------------------------------

    @property
    def is_complete(self):
        """
        Check if publication is complete.

        Returns
        -------
        bool
            True - if publication is complete,
            False - otherwise.
        """

        # issue may be empty
        return (self.volume != '') and (self.pages != '')

#---------------------------------------------------------------------------------------------------

    def year_volume_issue_pages_str(self):
        """
        String, containing year, volume, issue, pages.

        Returns
        -------
        str
            String.
        """

        r = f'{self.year}'

        if self.language == 'ru':
            r = r + f', Т. {self.volume}'
        else:
            r = r + f', Vol. {self.volume}'

        if self.issue != '':
            if self.language == 'ru':
                r = r + f', №. {self.issue}'
            else:
                r = r + f', N. {self.issue}'

        if self.language == 'ru':
            r = r + f', с. {self.pages}'
        else:
            r = r + f', p. {self.pages}'

        return r

#---------------------------------------------------------------------------------------------------

    @property
    def doi_inner_link_html(self):
        """
        Inner link by DOI.

        Returns
        -------
        str
            Text with inner link.
        """

        link = self.doi.replace('/', '~')

        return f'<a href="../data/publications/{link}.pdf">{self.doi}</a>'

#---------------------------------------------------------------------------------------------------

    @property
    def doi_extern_link_html(self):
        """
        Extern link.

        Returns
        -------
        str
            Text with inner link.
        """

        if self.extern_link == '':
            return font(b('нет внешней ссылки'), color='indianred')
        else:
            return f'<a href="{self.extern_link}">{self.extern_link}</a>'

#---------------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        String representation.

        Returns
        -------
        str
            String representation.
        """

        at = f'{self.authors_information(self.language)} {self.title}'
        ji1 = f'{self.journal.name}, '
        ji2 = self.year_volume_issue_pages_str()
        ji = ji1 + ji2

        return f'{at} // {ji}. DOI: {self.doi}'

#---------------------------------------------------------------------------------------------------

    @property
    def repr_html(self):
        """
        String representation in HTML.

        Returns
        -------
        str
            String representation in HTML.
        """

        at = f'{self.authors_information(self.language)} {self.title}'
        ji1 = f'{self.journal.name}, '
        ji2 = self.year_volume_issue_pages_str()
        ji = ji1 + ji2

        return f'{at} // {ji}. DOI: {self.doi_inner_link_html}'

#---------------------------------------------------------------------------------------------------

    @property
    def repr_for_plan_html(self):
        """
        Get representation for plan in HTML form.

        Returns
        -------
        str
            Representation.
        """

        if self.has_language:
            short_text = f'{self.repr_html}'
            color='darkgreen'
            if not self.is_complete:
                color='indianred'
            return small(font(short_text, color=color))
        else:
            if self.has_authors_affiliations:
                return small(font(f'{self.authors_information()}', color='indianred'))
            else:
                return small(font(f'нет информации', color='silver'))

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
