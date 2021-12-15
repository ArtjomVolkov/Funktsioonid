def znaki (a=float,b=float,c=str):
	"""Saab teha +,-,*,/ ja tagastab arv kui vastus on arv ja "Tundmate tehe" kui ei saa vastust leida.
	:param float a :Esimene arv
	:param float b :Teine arv
	:param float c :Aritmeetilise tehe
	rtype:var
	"""
	if c=="/":
		if c==0:
			vastus="Tundmatu tehe"
		else:
			vastus=a/b
	elif c == "*":
		vastus=a*b
	elif c == "-":
		vastus=a-b
	elif c == "+":
		vastus=a+b
	return vastus