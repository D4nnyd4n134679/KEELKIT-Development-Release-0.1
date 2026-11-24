
import argparse
import json

from keelkit.core import (
    rename_preview,
    organise_preview,
    generate_manifest
)


def main():
    parser = argparse.ArgumentParser(
        description="KEELKIT Automation Toolkit"
    )

    sub = parser.add_subparsers(
        dest="command",
        required=True
    )

    rename = sub.add_parser("rename")
    rename.add_argument("directory")
    rename.add_argument("--prefix", required=True)

    organise = sub.add_parser("organise")
    organise.add_argument("directory")

    manifest = sub.add_parser("manifest")
    manifest.add_argument("directory")

    args = parser.parse_args()

    if args.command == "rename":
        result = rename_preview(
            args.directory,
            args.prefix
        )

    elif args.command == "organise":
        result = organise_preview(
            args.directory
        )

    else:
        result = generate_manifest(
            args.directory
        )

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
