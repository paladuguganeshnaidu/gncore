"""Verify exact release artifact names/hashes without executing an upload."""

import argparse
import hashlib
from pathlib import Path
import re
from zipfile import ZipFile


def verify(directory, version):
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:(?:a|b|rc)\d+)?", version):
        raise ValueError("invalid release version")
    expected = {f"gncore-{version}-py3-none-any.whl", f"gncore-{version}.tar.gz", f"gncore-{version}-skills.zip"}
    checksums = {}
    for line in (directory / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([a-f0-9]{64})  ([A-Za-z0-9_.-]+)", line)
        if not match or match[2] in checksums:
            raise ValueError("invalid or repeated checksum entry")
        checksums[match[2]] = match[1]
    if set(checksums) != expected:
        raise ValueError("release inventory must contain exactly the versioned wheel, source archive and skill ZIP")
    for name, digest in checksums.items():
        path = directory / name
        if path.is_symlink() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError(f"release checksum mismatch: {name}")
    with ZipFile(directory / f"gncore-{version}-py3-none-any.whl") as archive:
        if archive.read("gncore/version.py").decode().find(f'"{version}"') < 0:
            raise ValueError("wheel runtime version does not match release")
    return checksums


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()
    for name in verify(args.directory, args.version):
        print("Verified", name)


if __name__ == "__main__":
    main()
