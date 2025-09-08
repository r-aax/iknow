from logging import exception

#===================================================================================================

class Journal:
    """
    Journal class.
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self, name, print_issn='', electronic_issn='',
                 rzni='', vak='', web_of_science='', scopus='',
                 astrophysics_data_system='', math_sci_net='', zb_math='',
                 chemical_abstracts='', springer='', agris='', geo_ref='', pub_med='',
                 rinz='', rinz_core='', rsci='', link=''):
        """
        Init journal.

        Parameters
        ----------
        name : str
            Name.
        print_issn : str
            Print ISSN.
        electronic_issn : str
            Electronic ISSN.
        rzni : str
            РЦНИ identifier.
        vak : str
            ВАК identifier.
        web_of_science : str
            Web of science identifier.
        scopus : str
            Scopus identifier.
        astrophysics_data_system : str
            Astrophysics data system identifier.
        math_sci_net : str
            MathSciNet identifier.
        zb_math : str
            zbMath identifier.
        chemical_abstracts : str
            Chemical Abstracts identifier.
        springer : str
            Springer identifier.
        agris : str
            Agris identifier.
        geo_ref : str
            GeoRef identifier.
        pub_med : str
            PubMed identifier.
        rinz : str
            РИНЦ identifier.
        rinz_core : str
            Core РИНЦ identifier.
        rsci : str
            RSCI identifier.
        link : str
            Link.
        """

        self.__name = name
        self.__print_issn = print_issn
        self.__electronic_issn = electronic_issn

        #
        # identifiers
        # usefull links:
        # https://bibl-stgau.ru/images/Files/RVNBD_2023.pdf?ysclid=m6sykfar7b604312357
        #

        # РЦНИ (Белый список)
        # https://journalrank.rcsi.science/ru/
        # Possible values:
        #   1, 2, 3, 4, (and no value)
        if not rzni in ['', '1', '2', '3', '4']:
            raise exception('Journal: РЦНИ value must be one of the following: 1, 2, 3, 4')
        self.__rzni = rzni

        # ВАК
        # https://vak.minobrnauki.gov.ru/documents#tab=_tab:editions~
        # Possible values:
        #   К~, К1, К2, К3, (and no value)
        # К~ mean journal is in VAK but has no category.
        if not vak in ['', 'К~', 'К1', 'К2', 'К3']:
            raise exception('Journal: ВАК value must be one of the following: K~, К1, К2, К3')
        self.__vak = vak

        # Web of science
        # https://www.webofscience.com
        # https://jcr.clarivate.com
        # Possible values:
        #   Q1, Q2, Q3, Q4, (and no value)
        if not web_of_science in ['', 'Q1', 'Q2', 'Q3', 'Q4']:
            raise exception('Journal: WebOfScience value must be one the the Q1, Q2, Q3, Q4')
        self.__web_of_science = web_of_science

        # Scopus.
        # http://www.scopus.com/
        # Possible values:
        #   Q1, Q2, Q3, Q4, (and no value)
        if not scopus in ['', 'Q1', 'Q2', 'Q3', 'Q4']:
            raise exception('Journal: SCOPUS value must be one the the Q1, Q2, Q3, Q4')
        self.__scopus = scopus

        # Astrophysics data system.
        self.__astrophysics_data_system = astrophysics_data_system

        # Math Sci Net.
        # https://mathscinet.ams.org
        self.__math_sci_net = math_sci_net

        # zbMATH
        # https://zbmath.org/
        self.__zb_math = zb_math

        # Chemical abstracts.
        self.__chemical_abstracts = chemical_abstracts

        # Springer.
        self.__springer = springer

        # Agris.
        self.__agris = agris

        # Geo ref.
        self.__geo_ref = geo_ref

        # Pub med.
        self.__pub_med = pub_med

        # РИНЦ.
        # https://elibrary.ru
        # Possible values:
        #   +, (and no data)
        if not rinz in ['', '+']:
            raise exception('Journal: РИНЦ must value value "+" or empty')
        self.__rinz = rinz

        # Core РИНЦ.
        # Possible values:
        #   +, (and no data)
        if not rinz_core in ['', '+']:
            raise exception('Journal: Ядро РИНЦ must value value "+" or empty')
        self.__rinz_core = rinz_core

        # RSCI
        # Possible values:
        #   +, (and no data)
        if not rsci in ['', '+']:
            raise exception('Journal: RSCI must value value "+" or empty')
        self.__rsci = rsci

        # Link.
        self.__link = link

#---------------------------------------------------------------------------------------------------

    @property
    def name(self):
        """
        Get name of journal.

        Returns
        -------
        str
            Name of journal.
        """

        if self.__name == '':
            raise exception('Journal: empty name')

        return self.__name

#---------------------------------------------------------------------------------------------------

    @property
    def print_issn(self):
        """
        Get print ISSN.

        Returns
        -------
        str
            Print ISSN.
        """

        return self.__print_issn

#---------------------------------------------------------------------------------------------------

    @property
    def electronic_issn(self):
        """
        Get electronic ISSN.

        Returns
        -------
        str
            Electronic ISSN.
        """

        return self.__electronic_issn

#---------------------------------------------------------------------------------------------------

    @property
    def rzni(self):
        """
        Get rzni.

        Returns
        -------
        str
            Identifier rzni.
        """

        return self.__rzni

#---------------------------------------------------------------------------------------------------

    @property
    def vak(self):
        """
        Get vak.

        Returns
        -------
        str
            Identifier var.
        """

        return self.__vak

#---------------------------------------------------------------------------------------------------

    @property
    def web_of_science(self):
        """
        Get web of science.

        Returns
        -------
        str
            Identifier web of science.
        """

        return self.__web_of_science

#---------------------------------------------------------------------------------------------------

    @property
    def scopus(self):
        """
        Get scopus.

        Returns
        -------
        str
            Identifier scopus.
        """

        return self.__scopus

#---------------------------------------------------------------------------------------------------

    @property
    def astrophysics_data_system(self):
        """
        Get astrophysics data system.

        Returns
        -------
        str
            Identifier astrophysics data system.
        """

        return self.__astrophysics_data_system

#---------------------------------------------------------------------------------------------------

    @property
    def math_sci_net(self):
        """
        Get math sci net.

        Returns
        -------
        str
            Identifier math sci net.
        """

        return self.__math_sci_net

#---------------------------------------------------------------------------------------------------

    @property
    def zb_math(self):
        """
        Get zb math.

        Returns
        -------
        str
            Identifier zb math.
        """

        return self.__zb_math

#---------------------------------------------------------------------------------------------------

    @property
    def chemical_abstracts(self):
        """
        Get chemical abstracts.

        Returns
        -------
        str
            Identifier chemical abstracts.
        """

        return self.__chemical_abstracts

#---------------------------------------------------------------------------------------------------

    @property
    def springer(self):
        """
        Get springer.

        Returns
        -------
        str
            Identifier springer.
        """

        return self.__springer

#---------------------------------------------------------------------------------------------------

    @property
    def agris(self):
        """
        Get agris.

        Returns
        -------
        str
            Identifier agris.
        """

        return self.__agris

#---------------------------------------------------------------------------------------------------

    @property
    def geo_ref(self):
        """
        Get geo ref.

        Returns
        -------
        str
            Identifier geo ref.
        """

        return self.__geo_ref

#---------------------------------------------------------------------------------------------------

    @property
    def pub_med(self):
        """
        Get pub med.

        Returns
        -------
        str
            Identifier pub med.
        """

        return self.__pub_med

#---------------------------------------------------------------------------------------------------

    @property
    def rinz(self):
        """
        Get rinz.

        Returns
        -------
        str
            Identifier rinz.
        """

        return self.__rinz

#---------------------------------------------------------------------------------------------------

    @property
    def rinz_core(self):
        """
        Get rinz_core.

        Returns
        -------
        str
            Identifier rinz_core.
        """

        return self.__rinz_core

#---------------------------------------------------------------------------------------------------

    @property
    def rsci(self):
        """
        Get rsci.

        Returns
        -------
        str
            Identifier rsci.
        """

        return self.__rsci

#---------------------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        String representation.

        Returns
        -------
        str
            String.
        """

        r = self.name

        if self.print_issn != '':
            r = r + f', Print ISSN: {self.print_issn}'

        if self.electronic_issn != '':
            r = r + f', Electronic ISSN: {self.electronic_issn}'

        if self.rzni != '':
            r = r + f', РЦНИ: {self.rzni}'

        if self.vak != '':
            r = r + f', ВАК: {self.vak}'

        if self.web_of_science != '':
            r = r + f', WoS: {self.web_of_science}'

        if self.scopus != '':
            r = r + f', SCOPUS: {self.scopus}'

        if self.astrophysics_data_system != '':
            raise exception('Journal: not implemented yet')\

        if self.math_sci_net != '':
            r = r + f', MathSciNet: {self.math_sci_net}'

        if self.zb_math != '':
            r = r + f', zbMATH: {self.zb_math}'

        if self.chemical_abstracts != '':
            raise exception('Journal: not implemented yet')

        if self.springer != '':
            raise exception('Journal: not implemented yet')

        if self.agris != '':
            raise exception('Journal: not implemented yet')

        if self.geo_ref != '':
            raise exception('Journal: not implemented yet')

        if self.pub_med != '':
            raise exception('Journal: not implemented yet')

        if self.rinz != '':
            r = r + f', РИНЦ: да'

        if self.rinz_core != '':
            r = r + f', Ядро РИНЦ: да'

        if self.rsci != '':
            r = r + f', RSCI: да'

        return r

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
