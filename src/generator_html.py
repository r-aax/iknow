from logging import exception

from publication import Publication
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

#===================================================================================================

if __name__ == '__main__':
    pass

#===================================================================================================
