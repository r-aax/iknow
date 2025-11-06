from employee import Employee
from thematic import Thematic
from publication import Publication
from html import *

#===================================================================================================

class ResearchResult:
    """
    Result of research.
    """

    #-----------------------------------------------------------------------------------------------

    def __init__(self, thematic, year,
                 title, content, description,
                 responsible, comment,
                 funding_part, publications=[]):
        """
        Init research result.

        Parameters
        ----------
        thematic : Thematic
            Thematic.
        year : int
            Year.
        title : str
            Title of result.
        content : str
            Content of work.
        description : str
            Description.
        responsible : Employee
            Responsible employee.
        comment : str
            Arbitrary comment.
        funding_part : float
            Funding part.
        publications : [Publication]
            Publications.
        """

        self.__thematic = thematic
        self.__year = year
        self.__title = title
        self.__content = content
        self.__description = description
        self.__responsible = responsible
        self.__comment = comment
        self.__funding_part = funding_part
        self.__publications = publications

        thematic.results.append(self)

    #-----------------------------------------------------------------------------------------------

    @property
    def thematic(self):
        """
        Get thematic.

        Returns
        -------
        Thematic
            Thematic.
        """

        return self.__thematic

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

        return self.__year

    #-----------------------------------------------------------------------------------------------

    @property
    def title(self):
        """
        Get title.

        Returns
        -------
        str
            Title.
        """

        return self.__title

    #-----------------------------------------------------------------------------------------------

    @property
    def content(self):
        """
        Get content.

        Returns
        -------
        str
            Content.
        """

        return self.__content

    #-----------------------------------------------------------------------------------------------

    @property
    def description(self):
        """
        Get description.

        Returns
        -------
        str
            Description.
        """

        return self.__description

    #-----------------------------------------------------------------------------------------------

    @property
    def responsible(self):
        """
        Get responsible.

        Returns
        -------
        Employee
            Responsible.
        """

        return self.__responsible

    #-----------------------------------------------------------------------------------------------

    @property
    def comment(self):
        """
        Get comment.

        Returns
        -------
        str
            Comment.
        """

        return self.__comment

    #-----------------------------------------------------------------------------------------------

    @property
    def funding_part(self):
        """
        Get funding part.

        Returns
        -------
        float
            Funding part.
        """

        return self.__funding_part

    #-----------------------------------------------------------------------------------------------

    @property
    def publications(self):
        """
        Get publications.

        Returns
        -------
        [Publication]
            Publications.
        """

        return self.__publications

    #-----------------------------------------------------------------------------------------------

    @property
    def publications_count(self):
        """
        Get publications count.

        Returns
        -------
        int
            Publications count.
        """

        return len(self.publications)

    #-----------------------------------------------------------------------------------------------

    @property
    def is_rid(self):
        """
        Check if result is result of intellectual activity.

        Returns
        -------
        bool
            True - if result of intellectual activity,
            False - if it is common result.
        """

        return self.title.startswith('База данных') or self.title.startswith('Программа для ЭВМ')

    #-----------------------------------------------------------------------------------------------

    @property
    def rid_type(self):
        """
        Get rid type.

        Returns
        -------
        str
            Rid type.
        """

        if self.title.startswith('База данных'):
            return 'База данных'
        elif self.title.startswith('Программа для ЭВМ'):
            return 'Программа для ЭВМ'
        else:
            raise Exception(f'research_result.rid_type: result {title} is not rid')

    #-----------------------------------------------------------------------------------------------

    @property
    def rid_name(self):
        """
        Get rid name.

        Returns
        -------
        str
            Rid name.
        """

        p = self.title.split('«')
        return p[1]

    #-----------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        String representation.

        Returns
        -------
        str
            String.
        """

        return f'{self.year}: {self.title} ({self.responsible}), ({self.comment})'

    #-----------------------------------------------------------------------------------------------

    def description_html(self):
        """
        Get description in HTML format.

        Returns
        -------
        str
            HTML description.
        """

        rid_pref = ''
        if self.is_rid:
            rid_pref = b(font('РИД: ', color='darkgreen'))
        resp_html = font(str(self.responsible), color='steelblue')
        comm_html = font(self.comment, color='silver')
        fund_html = font(str(self.funding_part) + ' %', color='orange')
        descr_html = font(small('описание: ' + self.description), color='silver')
        #main_html = f'{rid_pref}{self.title}<br>({resp_html}) ({comm_html}) ({fund_html})<br>{descr_html}'
        main_html = f'{rid_pref}{self.title}<br>{descr_html}'

        # Form publications html.
        publ_html = f'статьи: {self.publications_count}'
        publ_texts = [publ.repr_for_plan_html for publ in self.publications]
        publ_html = publ_html + ul(publ_texts)

        return f'{main_html}<br>{publ_html}<br>'

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
