import os
from pathlib import Path


def _get_data_dir_path():
    """Return the path of the data's directory.

    Returns:
        str: The data dir path.
    """
    DATA_DIR_PATH = None

    if not DATA_DIR_PATH:
        THIS_DIR = Path(os.path.dirname(__file__))
        BASE_DIR = Path(THIS_DIR.parents[0])
        DATA_DIR_PATH = os.path.join(BASE_DIR, 'data')

    return DATA_DIR_PATH

def get_mode_dir_path(mode):
    DATA_DIR_PATH = _get_data_dir_path()
    mode_dir_path = os.path.join(DATA_DIR_PATH, mode)

    return mode_dir_path

def get_date_dir_path(mode_dir_path, date):
    if not mode_dir_path:
        print('Use get_mode_dir_path.')
    else:
        date_dir_path = os.path.join(mode_dir_path, date)
        return date_dir_path
