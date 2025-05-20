from pathlib import Path
import geopandas as gpd


def load_geodata(path: Path, layer: str | None = None) -> gpd.GeoDataFrame:
    """Load a geospatial dataset from the given path."""
    return gpd.read_file(path, layer=layer)
