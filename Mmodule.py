#def Pindala (külg1:float,külg2:float)->float:
#	"""Riistküliku pindala leidmine 
#	:param float külg1:Riistkülike esimene külg
#	:param float külg2:Riistkülike teine külg
#	rtype:float
#	"""
#	S=külg1*külg2
#	return S

#def is_year_leap (year:int):
#	"""Teeb tööd
#	Edu korral tagastab tõene.
#	vastasel juhul Vale.
#	:param float year:Aasta
#	:param bool:
#	rtype:bool
#	"""
#	if year%4==0:
#		otvet=True
#	elif year%4!=0:
#		otvet=False
#	return otvet
#Площадь Периметр Диагональ
#import math
#def square (storona=int):
#	"""Teeb tööd leib pindalat,
#	:param int storona:Esimene pool
#	rtype: int
#	"""
#	S=storona*storona
#	P=4*storona
#	D=round(storona*math.sqrt(2))
#	return S,P,D
#Времена года
#def season(kuu=int)->str:
#	"""Teeb tööd otsib mis aastal suunab see kuu.
#	:param int sesson:
#	rtype:str
#	"""
#	if kuu>=1 and kuu<=12:
#		if kuu in [1,2,12]:
#			s="Talv"
#		elif kuu in [3,4,5]:
#			s="Kevad"
#		elif kuu in [6,7,8]:
#			s="Suvi"
#		elif kuu in [9,10,11]:
#			s="Sügis"
#	else:
#		s="Tundamatu kuu"
#	return s

#def date(day=int, month=int, year=int):
#    """
#    :param int day:day
#    :param int month:month
#    :param int year:year
#    rtype:int
#    """
#    import datetime
#    try:
#        datetime.date(year, month, day)
#    except ValueError:
#        return False
#    else:
#        return True