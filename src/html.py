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

def small(text):
    """
    Tag <small>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <small>.
    """

    return f'<small>{text}</small>'

#---------------------------------------------------------------------------------------------------

def center(text):
    """
    Tag <center>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <center>.
    """

    return f'<center>{text}</center>'

#---------------------------------------------------------------------------------------------------

def h1(text):
    """
    Tag <h1>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <h1>.
    """

    return f'<h1>{text}</h1>'

#---------------------------------------------------------------------------------------------------

def h2(text):
    """
    Tag <h2>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <h2>.
    """

    return f'<h2>{text}</h2>'

#---------------------------------------------------------------------------------------------------

def h3(text):
    """
    Tag <h3>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <h3>.
    """

    return f'<h3>{text}</h3>'

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

def a(href, text):
    """
    Tag <a>.

    Parameters
    ----------
    href : str
        Reference.
    text : str

    Returns
    -------
    str
        Text in <a>.
    """

    return f'<a href="{href}">{text}</a>'

#---------------------------------------------------------------------------------------------------

def p(text, align='left'):
    """
    Tag <p>.

    Parameters
    ----------
    text : str
        Text.
    align : str
        Align.

    Returns
    -------
    str
        Text in <p>.
    """

    return f'<p align="{align}">{text}</p>'

#---------------------------------------------------------------------------------------------------

def title(text):
    """
    Tag <title>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <title.
    """

    return f'<title>{text}</title>'

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

    style_text = '<style type="text/css">body,table,tr,th,rd{font-size:14pt}</style>'

    return f'<head>{style_text}{text}</head>'

#---------------------------------------------------------------------------------------------------

def li(text):
    """
    Tag <li>.

    Parameters
    ----------
    text : str
        Text.

    Returns
    -------
    str
        Text in <li>.
    """

    return f'<li>{text}</li>'

#---------------------------------------------------------------------------------------------------

def ul(lst):
    """
    Get <ul> tag for list of strings.

    Parameters
    ----------
    lst : [str]
        List of strings.

    Returns
    -------
    str
        Text in <ul>.
    """

    texts = [li(x) for x in lst]
    text = ''.join(texts)

    return f'<ul>{text}</ul>'

#---------------------------------------------------------------------------------------------------

def ol(lst):
    """
    Get <ol> tag for list of strings.

    Parameters
    ----------
    lst : [str]
        List of strings.

    Returns
    -------
    str
        Text in <ol>.
    """

    texts = [li(x) for x in lst]
    text = ''.join(texts)

    return f'<ol>{text}</ol>'
#---------------------------------------------------------------------------------------------------

def th(text, width):
    """
    Tag <th>.

    Parameters
    ----------
    text : str
        Text.
    width : str
        Width.

    Returns
    -------
    str
        Text in <th>.
    """

    return f'<th width="{width}">{text}</th>'

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

    return f'<td valign="top">{text}</td>'

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

if __name__ == '__main__':
    pass

#===================================================================================================
