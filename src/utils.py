
from logging import exception

#===================================================================================================

def unzip_2_lists(q):
    """
    Unzip.
    There is list q of elements, each element is list [x, y].
    Unzip it into list of two elements, [x] and [y].

    Parameters
    ----------
    q : list(list())
        List of lists.

    Returns
    -------
    [list(), list()]
        List of two lists.
    """

    a, b = [], []

    for qi in q:
        a.append(qi[0])
        b.append(qi[1])

    return [a, b]

#---------------------------------------------------------------------------------------------------

def find_keys_have_same_values(ks, vs):
    """
    Find keys ka, kb, so v(ka) = v(kb).

    Parameters
    ----------
    ks : list()
        List of keys.
    vs : list()
        List of values.

    Returns
    -------
    list()
        [ka, kb, v] - if ks and kb have the same value v,
        [] - if there is no conflict keys.
    """

    d = dict()
    n = len(ks)

    if len(vs) != n:
        raise exception('utils: keys and values lengths differ')

    for i in range(n):
        k = d.get(vs[i])
        if not k is None:
            return [k, ks[i], vs[i]]
        else:
            d[vs[i]] = ks[i]

    return []

#---------------------------------------------------------------------------------------------------

def write_to_file(fn, text):
    """
    Write to file.

    Parameters
    ----------
    fn : str
        File name.
    text : str
        Text.
    """

    with open(fn, 'w') as f:
        f.write(text)
        f.close()

#---------------------------------------------------------------------------------------------------

def norm_digits(x, n):
    """
    Norm value to n digits.

    Parameters
    ----------
    x : float
        Value.
    n : int
        Digits count.

    Returns
    -------
    float
        Value after norm.
    """

    t = 10**n

    return int(x * t) / t

#===================================================================================================

if __name__ == '__main__':

    # unzip_2_lists
    q = [[1, 2], [3, 4], [5, 6]]
    assert unzip_2_lists(q) == [[1, 3, 5], [2, 4, 6]]

    # find_keys_have_same_values
    assert find_keys_have_same_values([1, 2, 3], [1, 2, 3]) == []
    assert find_keys_have_same_values([1, 2, 3], [1, 2, 1]) == [1, 3, 1]

#===================================================================================================
