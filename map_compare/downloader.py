import requests
from pathlib import Path


def download_file(url: str, dest: Path, chunk_size: int = 8192) -> Path:
    """Download a file from ``url`` to ``dest``.

    Parameters
    ----------
    url : str
        The URL of the file to download.
    dest : Path
        Destination path where the file will be saved.
    chunk_size : int, optional
        Size of the download chunks, by default 8192.

    Returns
    -------
    Path
        The destination path.
    """
    dest.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
    return dest
