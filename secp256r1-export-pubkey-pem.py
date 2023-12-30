import sys
from argparse import ArgumentParser
from rich import print, box
from rich.panel import Panel
from Crypto.PublicKey import ECC

FORMATS = ["DER", "PEM", "OpenSSH", "SEC1", "raw"]
parser = ArgumentParser(description="Export Secp256r1 Pubkey")
parser.add_argument("--format", choices=FORMATS, default="PEM", help="output format")
parser.add_argument("--hex", action="store_true", help="read input as hex string")
parser.add_argument(
    "input", help="read input from arg or stdin", nargs="?", default="-"
)
args = parser.parse_args()

input = args.input if args.input != "-" else sys.stdin.buffer.read()
try:
    input = input.decode("utf-8")
except UnicodeDecodeError:
    pass

if args.hex:
    input = bytes.fromhex(input)

key = ECC.import_key(input, curve_name="secp256r1")
pubkey = key.public_key()

print(Panel("pubkey.pem", box=box.SQUARE))
exported = pubkey.export_key(format=args.format)
if isinstance(exported, bytes):
    exported = exported.hex()
print(exported)
