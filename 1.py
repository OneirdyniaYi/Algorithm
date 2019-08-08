#$language = "Python"
#$interface = "1.0"

import time
import os,sys
crt.Screen.Synchronous = True



def fun():
	try:
		while 1:
			crt.Screen.Send('\n')
			patt = crt.Screen.Get(1,1,69,233)
			if crt.Screen.WaitForString("local",40):
				crt.Screen.Send('\n')
				if crt.Screen.WaitForString("local",1):	
					crt.Screen.Send("system\n")
					if crt.Screen.WaitForString("Password",1):
						crt.Screen.Send("system\n")
					crt.Screen.WaitForString("ZZZZZZZZZZZZZ",70)
					crt.Screen.Send('\n')
					if crt.Screen.WaitForString("[system",1):
						crt.Screen.Send('toolbox reboot\n')
						crt.Screen.Send('\n')
			elif crt.Screen.Get(1,1,69,233) == patt:
				if patt.find('RAMDUMP') != -1:
					tim = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
					crt.Screen.WaitForString("ZZZZZZZZZZZZZ",10)
					with open("C:/Users/Administrator/Desktop/test/log1.txt","a+") as fp:
						str = crt.Screen.Get(68,1,69,233)
						ss = "1号机出现Error。时间:" + tim + '\n'
						fp.write(ss)
						fp.write(str+'\n')
					if not crt.Dialog.MessageBox("1号机绿屏","Error",BUTTON_OK):
						pass
				else:
					crt.Screen.WaitForString("ZZZZZZZZZZZZZ",20)
					crt.Screen.Send('\n')
					crt.Screen.Send('\n')
					crt.Screen.Send('\n')
					if crt.Screen.Get(1,1,69,233) == patt:
						crt.Dialog.MessageBox("1号机卡死","Error",BUTTON_OK)
			else:
				for i in range(1,3):
					crt.Screen.Send('\n')
	except:
		pass

def main():
	fun()
main()

