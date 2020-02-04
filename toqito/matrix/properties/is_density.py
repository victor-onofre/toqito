"""Determines whether or not a matrix is a density matrix."""
from typing import Union
import numpy as np

from toqito.matrix.properties.is_psd import is_psd


def is_density(mat: Union[np.ndarray, np.matrix]) -> bool:
    """
    Check if matrix is a density matrix.

    A matrix is a density matrix if its trace is equal to one and it has the
    property of being positive semidefinite (PSD).

    :param mat: Matrix to check.
    :return: Return `True` if matrix is a density matrix, and `False`
             otherwise.
    """
    if not isinstance(mat, np.matrix):
        mat = np.matrix(mat)

    return is_psd(mat) and np.isclose(np.trace(mat), 1)
