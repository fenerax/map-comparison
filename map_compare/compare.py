import geopandas as gpd


def compare_boundaries(
    df1: gpd.GeoDataFrame,
    df2: gpd.GeoDataFrame,
    id_col1: str,
    id_col2: str,
):
    """Compare two datasets and return differences.

    Parameters
    ----------
    df1, df2 : GeoDataFrame
        The datasets to compare.
    id_col1, id_col2 : str
        Column names that identify subdivisions in each dataset.
    """
    ids1 = set(df1[id_col1].astype(str))
    ids2 = set(df2[id_col2].astype(str))

    missing_in_df2 = ids1 - ids2
    missing_in_df1 = ids2 - ids1

    return {
        "missing_in_second": sorted(missing_in_df2),
        "missing_in_first": sorted(missing_in_df1),
    }
