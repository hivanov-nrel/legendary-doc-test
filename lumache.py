"""
Updating description to see what changes!!!
"""

__version__ = "0.2.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.
    
    Parameters
    ----------
    kind : list[str] or None
        Optional "kind" of ingredients.
    
    Returns
    -------
    return : list[str]
        The ingredients list.
    """
    return ["shells", "gorgonzola", "paprika"]