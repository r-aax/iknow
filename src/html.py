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

if __name__ == '__main__':
    pass

#===================================================================================================
