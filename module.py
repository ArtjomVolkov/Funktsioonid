#def znaki (a=float,b=float,c=str):
#	"""Saab teha +,-,*,/ ja tagastab arv kui vastus on arv ja "Tundmate tehe" kui ei saa vastust leida.
#	:param float a :Esimene arv
#	:param float b :Teine arv
#	:param float c :Aritmeetilise tehe
#	rtype:var
#	"""
#	if c=="/":
#		if c==0:
#			vastus="Tundmatu tehe"
#		else:
#			vastus=a/b
#	elif c == "*":
#		vastus=a*b
#	elif c == "-":
#		vastus=a-b
#	elif c == "+":
#		vastus=a+b
#	return vastus

#Банковский вклад
#def bank(a=float,years=int)->float:
#	"""arvutab sissemakse protsendi
#	:param float a : euro
#	:param int years :aastat
#	rtype:float
#	"""
#	for i in range(years):
#		a*=1.1
#	return a
#Простые числа 
#def is_prime(arv:int)->bool:
#	"""teeb tööd
#	:param arv:
#	rtype:bool
#	"""
#	t=0
#	for i in range(1,arv+1):
#		if arv%i==0: t+=1
#		if t==2:
#			t=True
#		else:
#			t=False
#	return t