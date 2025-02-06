from ctypes import windll
from logging import exception

from publication import Publication
from complex_theme import ComplexTheme
from html import *
import utils

#===================================================================================================


#---------------------------------------------------------------------------------------------------

def generate_publications_info(ps, fn):
    """
    Generate information about publications.

    Parameters
    ----------
    ps : [Publication]
        Publications list.
    fn : str
        Name of file.
    """

    table_lines = ''
    for p in ps:
        text_publ = td(p)
        text_links = td(f'{p.doi_inner_link_html}, {p.doi_extern_link_html}')
        text_metrics = td(p.journal)
        text_support = td(p.support)
        table_lines = table_lines + tr(f'{text_publ}{text_links}{text_metrics}{text_support}')

    bt = body(table(''.join(table_lines)))
    ht = head('')
    text = html(f'{ht}{bt}')

    utils.write_to_file(fn, text)

#---------------------------------------------------------------------------------------------------

def generate_plan(cx, fn, year_from=2025, year_to=2028):
    """
    Generate plan for complex theme.

    Parameters
    ----------
    cx : ComplexTheme
        Complex theme.
    fn : str
        Name of file.
    year_from : int
        Year from.
    year_to : int
        Year to.
    """

    # head
    text_head = head(title(cx.title))
    text_header = center(h3(f'План по комплексной теме<br>{cx.title}'))

    # main table
    text_trh = th('&nbsp;', width='1%')
    for thematic in cx.thematics:
        text_trh = text_trh + th(b(thematic.title), width='33%')
    text_trs = ''
    for year in range(year_from, year_to + 1):
        text_tr = td(b(str(year)))
        for thematic in cx.thematics:
            text_tr = text_tr + td(thematic.year_results_html(year))
        text_trs = text_trs + tr(text_tr)
    text_table = table(f'{text_trh}{text_trs}')

    # body
    text_body = body(f'{text_header}{text_table}')
    text_html = html(f'{text_head}{text_body}')

    utils.write_to_file(fn, text_html)

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
