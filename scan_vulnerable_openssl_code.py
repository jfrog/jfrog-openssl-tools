import sys
import enum
from pathlib import Path


class Diag(enum.Enum):
    NotRelevant = 0
    Vuln = 1
    Updated = 2


MESSAGE = {
    Diag.Vuln: "potentially vulnerable version of OpenSSL",
    Diag.Updated: "updated version of OpenSSL",
}


def diagnose_file(fname):
    with open(fname, "rb") as f:
        if b"ELF" in f.read(5):
            content = f.read()
            if b"ossl_punycode_decode" in content:
                if b"ripemd160_newctx" in content:
                    return Diag.Updated
                return Diag.Vuln
    return Diag.NotRelevant


if __name__ == "__main__":
    try:
        path = Path(sys.argv[1])
    except:
        print(f"Usage: {sys.argv[0]} ROOT_DIR")
        exit(-1)
    for p in path.glob("**/*"):
        if p.is_file():
            fname = str(p.absolute())
            try:
                diag = diagnose_file(fname)
            except:
                continue
            if diag in {Diag.Vuln, Diag.Updated}:
                print(f"{fname}: {MESSAGE[diag]}")
