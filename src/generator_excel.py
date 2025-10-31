from worksheet import Worksheet
from openpyxl import Workbook
from openpyxl.styles import Font

#===================================================================================================

class GeneratorExcel:
    """
    Master for excel documents generation.
    """

    #-----------------------------------------------------------------------------------------------
    # Common methods.
    #-----------------------------------------------------------------------------------------------

    def __init__(self):
        """
        Constructor.
        """

        self.book = Workbook()
        self.sheet = self.book.active

        # Set default font for all document.
        self.font = Font(name='Arial', size=10, color='00000000')
        self.font_bold = Font(name='Arial', size=10, color='00000000', bold=True)

    #-----------------------------------------------------------------------------------------------

    def txt(self, r, c, t, b=False):
        """
        Write text to cell.

        Parameters
        ----------
        r : str
            Row.
        c : str
            Column.
        t : str
            Text.
        b : bool
            Flag for bold text.
        """

        cn = f'{r}{c}'
        cell = self.sheet[cn]

        # Set common or bold text.
        if b:
            cell.font = self.font_bold
        else:
            cell.font = self.font

        self.sheet[cn] = t

    #-----------------------------------------------------------------------------------------------

    def save(self, name):
        """
        Save excel file.

        Parameters
        ----------
        name : str
            Out file name.
        """

        self.book.save(name)

    #-----------------------------------------------------------------------------------------------
    # PTNI performers book.
    #-----------------------------------------------------------------------------------------------

    def add_PTNI_performers_head_and_prepare(self):
        """
        Add PTNI performers head.
        """

        # Set title.
        self.sheet.title = 'Sheet'

        # Add columns names.
        columns_headers = [('A', '№ п/п'),
                           ('B', 'Фамилия *'),
                           ('C', 'Имя *'),
                           ('D', 'Отчество'),
                           ('E', 'Должность *'),
                           ('F', 'СНИЛС'),
                           ('G', 'ИНН'),
                           ('H', 'Ученая степень'),
                           ('I', 'Ученое звание'),
                           ('J', 'Дата рождения *'),
                           ('K', 'Гражданство *'),
                           ('L', 'ORCID'),
                           ('M', 'WOS Research ID'),
                           ('N', 'Scopus Author ID'),
                           ('O', 'ID РИНЦ'),
                           ('P', 'Ссылка на web-страницу')]
        for ch in columns_headers:
            self.txt(ch[0], 1, ch[1], True)

        # Set columns widths.
        columns_widths = [('A', 9),
                          ('B', 30),
                          ('C', 30),
                          ('D', 30),
                          ('E', 30),
                          ('F', 30),
                          ('G', 30),
                          ('H', 30),
                          ('I', 30),
                          ('J', 30),
                          ('K', 30),
                          ('L', 30),
                          ('M', 30),
                          ('N', 30),
                          ('O', 30),
                          ('P', 30)]
        for cw in columns_widths:
            self.sheet.column_dimensions[cw[0]].width = cw[1]

    #-----------------------------------------------------------------------------------------------

    def add_PTNI_performers(self, team):
        """
        Add performers data.

        Parameters
        ----------
        team : Worksheet
            Worksheet.
        """

        r = 2

        for wsl in team.lines:
            em = wsl.employee
            p = em.personal

            # Write data to fields.
            self.txt('A', r, r - 1)
            self.txt('B', r, p.surname('ru'))
            self.txt('C', r, p.name('ru'))
            self.txt('D', r, p.patronymic('ru'))
            self.txt('E', r, wsl.job_title.name)
            self.txt('F', r, p.snils if p.has_snils else '')
            self.txt('G', r, p.inn if p.has_inn else '')
            self.txt('H', r, 'TODO')
            self.txt('I', r, 'TODO')
            self.txt('J', r, 'TODO')
            self.txt('K', r, 'РОССИЯ')
            self.txt('L', r, p.orcid)
            self.txt('M', r, p.wos)
            self.txt('N', r, p.scopus)
            self.txt('O', r, p.elibrary)
            self.txt('P', r, 'TODO')

            r = r + 1

#===================================================================================================

def generate_PTNI_performers(team, out):
    """
    Generate file of performers (PTNI).

    Parameters
    ----------
    team : Worksheet
        Worksheet.
    out : str
        Out file name.
    """

    e = GeneratorExcel()
    e.add_PTNI_performers_head_and_prepare()
    e.add_PTNI_performers(team)
    e.save(f'{out}.xlsx')

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
