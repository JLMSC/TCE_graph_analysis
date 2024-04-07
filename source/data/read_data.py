"""Read requested data from TCE."""
import json
from typing import Any


def read_data(file_name: str) -> Any:
    """Load the .json file data requested from TCE.

    Parameters
    ----------
    file_name : str
        The file name.
    
    Returns
    -------
    Any
        The .json file's content.
    """
    with open(file=file_name, mode='r', encoding='utf-8') as file:
        file_data = json.load(fp=file)
        file.close()
    return file_data
