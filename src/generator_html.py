from logging import exception

from publication import Publication
import utils

#===================================================================================================

def b(text):
    """
    Tag <b>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <b>.
    """

    return f'<b>{text}</b>'

#---------------------------------------------------------------------------------------------------

def i(text):
    """
    Tag <i>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <i>.
    """

    return f'<i>{text}</i>'

#---------------------------------------------------------------------------------------------------

def font(text, color):
    """
    Tag <font>.

    Parameters
    ----------
    text : str
        Text.
    color : str
        Color.

    Returns
    -------
    str
        Text in <font>.
    """

    return f'<font color="{color}">{text}</font>'

#---------------------------------------------------------------------------------------------------

def head(text):
    """
    Tag <head>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <head>.
    """

    style_text = '<style type="text/css">body,table,tr,th,rd{font-size:16pt}</style>'

    return f'<head>{style_text}{text}</head>'

#---------------------------------------------------------------------------------------------------

def th(text):
    """
    Tag <th>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <th>.
    """

    return f'<th>{text}</th>'

#---------------------------------------------------------------------------------------------------

def td(text):
    """
    Tag <td>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <td>.
    """

    return f'<td>{text}</td>'

#---------------------------------------------------------------------------------------------------

def tr(text):
    """
    Tag <tr>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <tr>.
    """

    return f'<tr>{text}</tr>'

#---------------------------------------------------------------------------------------------------

def table(text):
    """
    Tag <table>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <table>.
    """

    return f'<table border="1">{text}</table>'

#---------------------------------------------------------------------------------------------------

def body(text):
    """
    Tag <body>

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <body>.
    """

    return f'<body>{text}</body>'

#---------------------------------------------------------------------------------------------------

def html(text):
    """
    Tag <html>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <html>.
    """

    return f'<html>{text}</html>'

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
