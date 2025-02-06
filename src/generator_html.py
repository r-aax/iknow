from logging import exception

from publication import Publication
from html import *
import utils

#===================================================================================================

def doi_inner_link(p):
    """
    Inner link by DOI.

    Parameters
    ----------
    p : Publication
        Publication.

    Returns
    -------
    str
        Text with inner link.
    """

    link = p.doi.replace('/', '~')

    return f'<a href="../data/publications/{link}.pdf">внутренняя ссылка</a>'

#---------------------------------------------------------------------------------------------------

def doi_extern_link(p):
    """
    Extern link.

    Parameters
    ----------
    p : Publication
        Publication.

    Returns
    -------
    str
        Text with inner link.
    """

    if p.extern_link == '':
        return font(b('нет внешней ссылки'), 'indianred')
    else:
        return f'<a href="{p.extern_link}">{p.extern_link}</a>'

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
        text_links = td(f'{doi_inner_link(p)}, {doi_extern_link(p)}')
        text_metrics = td(p.journal)
        text_support = td(p.support)
        table_lines = table_lines + tr(f'{text_publ}{text_links}{text_metrics}{text_support}')

    bt = body(table(''.join(table_lines)))
    ht = head('')
    text = html(f'{ht}{bt}')

    utils.write_to_file(fn, text)

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
