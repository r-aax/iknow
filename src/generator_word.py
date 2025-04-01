from complex_theme import ComplexTheme
from worksheet import Worksheet
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt, Cm

#===================================================================================================

class GeneratorWord:
    """
    Master for word documents generation.
    """

    """
    document = Document()

    document.add_heading('Document Title', 0)

    p = document.add_paragraph('A plain paragraph having some ')
    p.add_run('bold').bold = True
    p.add_run(' and some ')
    p.add_run('italic.').italic = True

    document.add_heading('Heading, level 1', level=1)
    document.add_paragraph('Intense quote', style='Intense Quote')

    document.add_paragraph(
        'first item in unordered list', style='List Bullet'
    )
    document.add_paragraph(
        'first item in ordered list', style='List Number'
    )

    #document.add_picture('monty-truth.png', width=Inches(1.25))

    records = (
        (3, '101', 'Spam'),
        (7, '422', 'Eggs'),
        (4, '631', 'Spam, spam, eggs, and spam')
    )

    table = document.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Qty'
    hdr_cells[1].text = 'Id'
    hdr_cells[2].text = 'Desc'
    for qty, id, desc in records:
        row_cells = table.add_row().cells
        row_cells[0].text = str(qty)
        row_cells[1].text = id
        row_cells[2].text = desc

    document.add_page_break()

    document.save('demo.docx')
    """

#---------------------------------------------------------------------------------------------------

    def __init__(self):
        """
        Init document.
        """

        self.doc = Document()
        sections = self.doc.sections

        for section in sections:
            section.top_margin = Cm(2.0)
            section.bottom_margin = Cm(2.0)
            section.left_margin = Cm(2.25)
            section.right_margin = Cm(1.25)

#---------------------------------------------------------------------------------------------------

    def save(self, name):
        """
        Save document.

        Parameters
        ----------
        name : str
            File name.
        """

        self.doc.save(name)

#---------------------------------------------------------------------------------------------------

    def add_empty_line(self):
        """
        Add empty line.
        """

        self.doc.add_paragraph('')

#---------------------------------------------------------------------------------------------------

    def add_corner_inscription_supplement_to_order(self, n):
        """
        Add inscription to corner of document.
        Inscription contains text about supplement of order.

        Parameters
        ----------
        n : int
            Number of supplement.
        """

        p = self.doc.add_paragraph('Приложение № 4\n'
                                   'к приказу НИЦ «Курчатовский институт»\n'
                                   'от «___» ____________ ____ г. № ______')
        p.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
        f = p.style.font
        f.name = 'Times New Roman'
        f.size = Pt(12)

#---------------------------------------------------------------------------------------------------

    def add_temporary_team_title(self, cx, y):
        """
        Add title for temporary team.

        Parameters
        ----------
        cx : ComplexTheme
            Complex theme.
        y : int
            Start year.
        """

        pre_text = 'СОСТАВ\n'\
                   'временного трудового коллектива\n'\
                   'для выполнения научно-исследовательской работы по комплексной теме\n'
        post_text = f' на очередной {y} год и плановый период {y + 1} и {y + 2} годов'
        p = self.doc.add_paragraph()
        r = p.add_run(pre_text + cx.title + post_text)
        r.bold = True
        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

#---------------------------------------------------------------------------------------------------

    def add_temporay_team_table(self, w, cx):
        """
        Add table for temporary team.

        Parameters
        ----------
        w : Worksheet
            Worksheet.
        cx : ComplexTheme
            Complex theme.
        """

        # number of people
        n = len(w.lines)

        # table and its style
        t = self.doc.add_table(rows = n + 1, cols = 7)
        t.style = 'Table Grid'

        # head
        h = t.rows[0].cells
        h[0].text = '№ п/п'
        h[1].text = 'ФИО'
        h[2].text = 'Должность'
        h[3].text = 'Табельный номер'
        h[4].text = 'Год рождения'
        h[5].text = 'Подразделение'
        h[6].text = 'Наименование подтем/тематик исследований'

        # add rest rows
        for i in range(n):
            r = t.rows[i + 1].cells
            wl = w.lines[i]
            e = wl.employee
            p = e.personal
            r[0].text = str(i + 1) + '.'
            r[1].text = p.surname_name_patronymic()
            r[2].text = wl.job_title.name
            r[3].text = e.tabel
            r[4].text = str(p.year)
            r[5].text = wl.job_place.half_full_name()
            r[6].text = cx.all_thematics_titles()

#===================================================================================================

def generate_temporary_team(n, cx, team, y, out):
    """
    Geterate temporary team dicument.

    Parameters
    ----------
    n : int
        Supplement number.
    cx : ComplexTheme
        Complex theme.
    team : Worksheet
        Team working on this theme.
    y : int
        Start year.
    out : str
        Out file name.
    """

    w = GeneratorWord()
    w.add_corner_inscription_supplement_to_order(n)
    w.add_empty_line()
    w.add_temporary_team_title(cx, y)
    w.add_empty_line()
    w.add_temporay_team_table(team, cx)
    w.save(out + '.docx')

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
