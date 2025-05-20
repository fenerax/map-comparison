from pathlib import Path
import argparse

from .downloader import download_file
from .loader import load_geodata
from .compare import compare_boundaries


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare boundary datasets")
    parser.add_argument("source1", help="Path or URL to first dataset")
    parser.add_argument("source2", help="Path or URL to second dataset")
    parser.add_argument("--id1", default="id", help="Identifier column for first dataset")
    parser.add_argument("--id2", default="id", help="Identifier column for second dataset")
    parser.add_argument(
        "--download-dir",
        type=Path,
        default=Path("data"),
        help="Directory where downloaded files are stored",
    )
    args = parser.parse_args()

    path1 = prepare_source(args.source1, args.download_dir)
    path2 = prepare_source(args.source2, args.download_dir)

    gdf1 = load_geodata(path1)
    gdf2 = load_geodata(path2)

    diff = compare_boundaries(gdf1, gdf2, args.id1, args.id2)
    if diff["missing_in_second"]:
        print("Missing in second dataset:")
        for val in diff["missing_in_second"]:
            print("  ", val)
    if diff["missing_in_first"]:
        print("Missing in first dataset:")
        for val in diff["missing_in_first"]:
            print("  ", val)


def prepare_source(source: str, download_dir: Path) -> Path:
    """Return a local path to the dataset, downloading if necessary."""
    if source.startswith("http://") or source.startswith("https://"):
        filename = download_dir / Path(source).name
        return download_file(source, filename)
    return Path(source)


if __name__ == "__main__":
    main()
