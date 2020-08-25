import pikepdf

pdffile = input("\033[96mEnter the name/path of PDF file:\033[0m ")
passwordlist = input("\033[96mEnter the name/path of Dictionary: \033[0m")


with open(passwordlist,'r') as passlist:
	passlist = [password for password in passlist.read().split('\n') if password]
	for passwd in passlist:
		try:
			with pikepdf.open(pdffile, password = passwd) as pdfile:
				pdfile.save('output.pdf')
				print("\033[92m--------------------------------------------")
				print("          Found Password: -->  "+ passwd)
				print("--------------------------------------------")
				exit()


		except pikepdf._qpdf.PasswordError:
			print("\033[91mtrying: \033[0m"+ passwd)