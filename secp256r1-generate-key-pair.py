from rich import print, box
from rich.console import Console
from rich.panel import Panel
from Crypto.PublicKey import ECC

console = Console()

key = ECC.generate(curve="secp256r1")
pubkey = key.public_key()

print(Panel("prikey.pem", box=box.SQUARE))
print(key.export_key(format="PEM"))

print(Panel("pubkey.pem", box=box.SQUARE))
print(pubkey.export_key(format="PEM"))

print(Panel("pubkey.sec1", box=box.SQUARE))
console.print(pubkey.export_key(format="SEC1").hex(), width=66)
