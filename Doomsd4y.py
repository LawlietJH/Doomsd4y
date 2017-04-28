# -*- Coding: UTF-8 -*-
# Python 3
#
#  ██████╗  ██████╗  ██████╗ ███╗   ███╗███████╗██████╗ ██╗  ██╗██╗   ██╗
#  ██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║██╔════╝██╔══██╗██║  ██║╚██╗ ██╔╝
#  ██║  ██║██║   ██║██║   ██║██╔████╔██║███████╗██║  ██║███████║ ╚████╔╝ 
#  ██║  ██║██║   ██║██║   ██║██║╚██╔╝██║╚════██║██║  ██║╚════██║  ╚██╔╝  
#  ██████╔╝╚██████╔╝╚██████╔╝██║ ╚═╝ ██║███████║██████╔╝     ██║   ██║   
#  ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═════╝      ╚═╝   ╚═╝   
#                                                         By: LawlietJH
#                                                               v1.0.4
# Fuente: 'ANSI Shadow' - Desde: http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Doomsd4y
import os



Autor = "LawlietJH"
Versión = "v1.0.4"



def getFecha(Fecha):
	
	if Fecha == "": print("\n\n\t\t [!] Escribe Una Fecha...", end="")
	
	Fecha = Fecha.replace(" ", "").replace("-", "/").replace(".", "/").replace("_", "/").replace(",", "/").replace("|", "/").replace("\\", "/")
	Fecha = Fecha.split("/")
	
	return Fecha



def getDiaBaseSiglo(Anio):
	
	DiaBaseSiglo = 0		# La Doble Diagonal Devuelve solo el Número Entero De La División: '69 // 100 = 0', '69 / 100 = 0.69'
	Siglo = Anio // 100		# Así, Obtenemos Todos Los Digitos Excepto Los 2 Ultimos: '123456 // 100 = 1234'
	
	if Siglo % 4 == 0: DiaBaseSiglo = 2
	elif Siglo % 4 == 1: DiaBaseSiglo = 0
	elif Siglo % 4 == 2: DiaBaseSiglo = 5
	elif Siglo % 4 == 3: DiaBaseSiglo = 3
	
	return DiaBaseSiglo



def getDiaBaseDecada(Anio):
	
	DiaBase = Anio % 100		# Obtenemos Los Dos Ultimos Digitos: '123456 % 100 = 56'
	
	A1 = DiaBase // 12
	A2 = DiaBase % 12
	A3 = A2 // 4
	A4 = A1 + A2 + A3
	DiaBaseDecada = A4 % 7
	
	return DiaBaseDecada


def getDoomsday(DBD, DBS):
	
	global DoomAnio
	
	DoomAnio = (DBD + DBS) % 7



def Bisiesto(Anio):
	
    # Analizamos Si El Año Solicitado Es Bisiesto.
	
    if (Anio % 4 == 0 and Anio % 100 != 0 or Anio % 400 == 0): EsBisiesto = True
        
    else: EsBisiesto = False

    return EsBisiesto



def ValidarFecha(Dia, Mes, EsBisiesto):

	# Comprobamos Si La Fecha Solicitada Es Valida.
	
	FValida = False;
	
	if((Mes==1 and (Dia>=1 and Dia <= 31))\
	
	or (EsBisiesto == False and Mes == 2 and (Dia >= 1 and Dia <= 28))\
	or (EsBisiesto == True  and Mes == 2 and (Dia >= 1 and Dia <= 29))\
	
	or (Mes == 3  and (Dia >= 1 and Dia <= 31))\
	or (Mes == 5  and (Dia >= 1 and Dia <= 31))\
	or (Mes == 7  and (Dia >= 1 and Dia <= 31))\
	or (Mes == 8  and (Dia >= 1 and Dia <= 31))\
	or (Mes == 10 and (Dia >= 1 and Dia <= 31))\
	or (Mes == 12 and (Dia >= 1 and Dia <= 31))\
	
	or (Mes == 4  and (Dia >= 1 and Dia <= 30))\
	or (Mes == 6  and (Dia >= 1 and Dia <= 30))\
	or (Mes == 9  and (Dia >= 1 and Dia <= 30))\
	or (Mes == 11 and (Dia >= 1 and Dia <= 30))): FValida = True
	
	else: FValida = False
	
	return FValida



def CalcularDD(Dia, Mes, Bisiesto):
	
	global DiaSem, DoomAnio
	
	
	# Esto Solo Lo Pongo Para Que Sepan Con Exactitud Que Dias Son Doomsday.
	# Más Adelante Veran Donde Los Coloque, No Era Necesario, Pero Se Ve Bien.
	
	# Estos Dias Son Doomsday:
	
	Ene = 3
	Feb = 28
	Mar = 7
	Abr = 4
	May = 9
	Jun = 6	
	Jul = 11
	Ago = 8
	Sep = 5
	Oct = 10
	Nov = 7
	Dic = 12
	
	if(Bisiesto == False and Mes == 1 and (Dia >= 1 and Dia <= 31)):
		
		if(    Dia==1 or Dia==8  or Dia==15 or Dia==22 or Dia==29):	DiaSem = (DoomAnio + 5) % 7
		elif(  Dia==2 or Dia==9  or Dia==16 or Dia==23 or Dia==30):	DiaSem = (DoomAnio + 6) % 7
		elif(Dia==Ene or Dia==10 or Dia==17 or Dia==24 or Dia==31):	DiaSem =  DoomAnio % 7
		elif(  Dia==4 or Dia==11 or Dia==18 or Dia==25):			DiaSem = (DoomAnio + 1) % 7
		elif(  Dia==5 or Dia==12 or Dia==19 or Dia==26):			DiaSem = (DoomAnio + 2) % 7
		elif(  Dia==6 or Dia==13 or Dia==20 or Dia==27):			DiaSem = (DoomAnio + 3) % 7
		elif(  Dia==7 or Dia==14 or Dia==21 or Dia==28):			DiaSem = (DoomAnio + 4) % 7
		
	elif(Bisiesto == True and Mes == 1 and (Dia >= 1 and Dia <= 31)):
		
		if(      Dia==1 or Dia==8  or Dia==15 or Dia==22 or Dia==29):	DiaSem = (DoomAnio + 4) % 7
		elif(    Dia==2 or Dia==9  or Dia==16 or Dia==23 or Dia==30):	DiaSem = (DoomAnio + 5) % 7
		elif(    Dia==3 or Dia==10 or Dia==17 or Dia==24 or Dia==31):	DiaSem = (DoomAnio + 6) % 7
		elif(Dia==Ene+1 or Dia==11 or Dia==18 or Dia==25):				DiaSem =  DoomAnio % 7
		elif(    Dia==5 or Dia==12 or Dia==19 or Dia==26):				DiaSem = (DoomAnio + 1) % 7
		elif(    Dia==6 or Dia==13 or Dia==20 or Dia==27):				DiaSem = (DoomAnio + 2) % 7
		elif(    Dia==7 or Dia==14 or Dia==21 or Dia==28):				DiaSem = (DoomAnio + 3) % 7
		
	elif(Bisiesto == False and Mes == 2 and (Dia >= 1 and Dia <= 28)):
		
		if(  Dia==1 or Dia==8 or Dia==15 or Dia==22):		DiaSem = (DoomAnio + 1) % 7
		elif(Dia==2 or Dia==9 or Dia==16 or Dia==23):		DiaSem = (DoomAnio + 2) % 7
		elif(Dia==3 or Dia==10 or Dia==17 or Dia==24):		DiaSem = (DoomAnio + 3) % 7
		elif(Dia==4 or Dia==11 or Dia==18 or Dia==25):		DiaSem = (DoomAnio + 4) % 7
		elif(Dia==5 or Dia==12 or Dia==19 or Dia==26):		DiaSem = (DoomAnio + 5) % 7
		elif(Dia==6 or Dia==13 or Dia==20 or Dia==27):		DiaSem = (DoomAnio + 6) % 7
		elif(Dia==7 or Dia==14 or Dia==21 or Dia==Feb):		DiaSem =  DoomAnio % 7
		
	elif(Bisiesto == True and Mes == 2 and (Dia >= 1 and Dia <= 29)):

		if(  Dia==1 or Dia==8  or Dia==15 or Dia==22 or Dia==Feb+1):	DiaSem = DoomAnio % 7
		elif(Dia==2 or Dia==9  or Dia==16 or Dia==23):		DiaSem = (DoomAnio+1) % 7
		elif(Dia==3 or Dia==10 or Dia==17 or Dia==24):		DiaSem = (DoomAnio+2) % 7
		elif(Dia==4 or Dia==11 or Dia==18 or Dia==25):		DiaSem = (DoomAnio+3) % 7
		elif(Dia==5 or Dia==12 or Dia==19 or Dia==26):		DiaSem = (DoomAnio+4) % 7
		elif(Dia==6 or Dia==13 or Dia==20 or Dia==27):		DiaSem = (DoomAnio+5) % 7
		elif(Dia==7 or Dia==14 or Dia==21 or Dia==28):		DiaSem = (DoomAnio+6) % 7
		
	elif(Mes == 3 and (Dia >= 1 and Dia <= 31)):
		
		if(    Dia==1 or Dia==8  or Dia==15 or Dia==22 or Dia==29):	DiaSem = (DoomAnio + 1) % 7
		elif(  Dia==2 or Dia==9  or Dia==16 or Dia==23 or Dia==30):	DiaSem = (DoomAnio + 2) % 7
		elif(  Dia==3 or Dia==10 or Dia==17 or Dia==24 or Dia==31):	DiaSem = (DoomAnio + 3) % 7
		elif(  Dia==4 or Dia==11 or Dia==18 or Dia==25):			DiaSem = (DoomAnio + 4) % 7
		elif(  Dia==5 or Dia==12 or Dia==19 or Dia==26):			DiaSem = (DoomAnio + 5) % 7
		elif(  Dia==6 or Dia==13 or Dia==20 or Dia==27):			DiaSem = (DoomAnio + 6) % 7
		elif(Dia==Mar or Dia==14 or Dia==21 or Dia==28):			DiaSem =  DoomAnio % 7
		
	elif(Mes == 4 and (Dia >= 1 and Dia <= 30)):
		
		if(  Dia==1   or Dia==8  or Dia==15 or Dia==22 or Dia==29):	DiaSem = (DoomAnio + 4) % 7
		elif(Dia==2   or Dia==9  or Dia==16 or Dia==23 or Dia==30):	DiaSem = (DoomAnio + 5) % 7
		elif(Dia==3   or Dia==10 or Dia==17 or Dia==24):			DiaSem = (DoomAnio + 6) % 7
		elif(Dia==Abr or Dia==11 or Dia==18 or Dia==25):			DiaSem =  DoomAnio % 7
		elif(Dia==5   or Dia==12 or Dia==19 or Dia==26):			DiaSem = (DoomAnio + 1) % 7
		elif(Dia==6   or Dia==13 or Dia==20 or Dia==27):			DiaSem = (DoomAnio + 2) % 7
		elif(Dia==7   or Dia==14 or Dia==21 or Dia==28):			DiaSem = (DoomAnio + 3) % 7
		
	elif(Mes == 5 and (Dia >= 1 and Dia <= 31)):
		
		if(  Dia==1 or Dia==8   or Dia==15 or Dia==22 or Dia==29):	DiaSem = (DoomAnio + 6) % 7
		elif(Dia==2 or Dia==May or Dia==16 or Dia==23 or Dia==30):	DiaSem =  DoomAnio % 7
		elif(Dia==3 or Dia==10  or Dia==17 or Dia==24 or Dia==31):	DiaSem = (DoomAnio + 1) % 7
		elif(Dia==4 or Dia==11  or Dia==18 or Dia==25):				DiaSem = (DoomAnio + 2) % 7
		elif(Dia==5 or Dia==12  or Dia==19 or Dia==26):				DiaSem = (DoomAnio + 3) % 7
		elif(Dia==6 or Dia==13  or Dia==20 or Dia==27):				DiaSem = (DoomAnio + 4) % 7
		elif(Dia==7 or Dia==14  or Dia==21 or Dia==28):				DiaSem = (DoomAnio + 5) % 7
		
	elif(Mes == 6 and (Dia >= 1 and Dia <= 30)):
		
		if(  Dia==1   or Dia==8  or Dia==15 or Dia==22 or Dia==29):	DiaSem = (DoomAnio + 2) % 7
		elif(Dia==2   or Dia==9  or Dia==16 or Dia==23 or Dia==30):	DiaSem = (DoomAnio + 3) % 7
		elif(Dia==3   or Dia==10 or Dia==17 or Dia==24):			DiaSem = (DoomAnio + 4) % 7
		elif(Dia==4   or Dia==11 or Dia==18 or Dia==25):			DiaSem = (DoomAnio + 5) % 7
		elif(Dia==5   or Dia==12 or Dia==19 or Dia==26):			DiaSem = (DoomAnio + 6) % 7
		elif(Dia==Jun or Dia==13 or Dia==20 or Dia==27):			DiaSem =  DoomAnio % 7
		elif(Dia==7   or Dia==14 or Dia==21 or Dia==28):			DiaSem = (DoomAnio + 1) % 7
		
	elif(Mes == 7 and (Dia >= 1 and Dia <= 31)):
		
		if(  Dia==1 or Dia==8   or Dia==15 or Dia==22 or Dia==29):	DiaSem = (DoomAnio + 4) % 7
		elif(Dia==2 or Dia==9   or Dia==16 or Dia==23 or Dia==30):	DiaSem = (DoomAnio + 5) % 7
		elif(Dia==3 or Dia==10  or Dia==17 or Dia==24 or Dia==31):	DiaSem = (DoomAnio + 6) % 7
		elif(Dia==4 or Dia==Jul or Dia==18 or Dia==25):				DiaSem =  DoomAnio % 7
		elif(Dia==5 or Dia==12  or Dia==19 or Dia==26):				DiaSem = (DoomAnio + 1) % 7
		elif(Dia==6 or Dia==13  or Dia==20 or Dia==27):				DiaSem = (DoomAnio + 2) % 7
		elif(Dia==7 or Dia==14  or Dia==21 or Dia==28):				DiaSem = (DoomAnio + 3) % 7
		
	elif(Mes==8 and (Dia >= 1 and Dia <= 31)):
		
		if(  Dia==1 or Dia==Ago or Dia==15 or Dia==22 or Dia==29):	DiaSem =  DoomAnio % 7
		elif(Dia==2 or Dia==9   or Dia==16 or Dia==23 or Dia==30):	DiaSem = (DoomAnio + 1) % 7
		elif(Dia==3 or Dia==10  or Dia==17 or Dia==24 or Dia==31):	DiaSem = (DoomAnio + 2) % 7
		elif(Dia==4 or Dia==11  or Dia==18 or Dia==25):				DiaSem = (DoomAnio + 3) % 7
		elif(Dia==5 or Dia==12  or Dia==19 or Dia==26):				DiaSem = (DoomAnio + 4) % 7
		elif(Dia==6 or Dia==13  or Dia==20 or Dia==27):				DiaSem = (DoomAnio + 5) % 7
		elif(Dia==7 or Dia==14  or Dia==21 or Dia==28):				DiaSem = (DoomAnio + 6) % 7
		
	elif(Mes==9 and (Dia >= 1 and Dia <= 30)):
		
		if(  Dia==1   or Dia==8  or Dia==15 or Dia==22 or Dia==29):	DiaSem = (DoomAnio + 3) % 7
		elif(Dia==2   or Dia==9  or Dia==16 or Dia==23 or Dia==30):	DiaSem = (DoomAnio + 4) % 7
		elif(Dia==3   or Dia==10 or Dia==17 or Dia==24):			DiaSem = (DoomAnio + 5) % 7
		elif(Dia==4   or Dia==11 or Dia==18 or Dia==25):			DiaSem = (DoomAnio + 6) % 7
		elif(Dia==Sep or Dia==12 or Dia==19 or Dia==26):			DiaSem =  DoomAnio % 7
		elif(Dia==6   or Dia==13 or Dia==20 or Dia==27):			DiaSem = (DoomAnio + 1) % 7
		elif(Dia==7   or Dia==14 or Dia==21 or Dia==28):			DiaSem = (DoomAnio + 2) % 7
		
	elif(Mes == 10 and (Dia >= 1 and Dia <= 31)):
		
		if(  Dia==1 or Dia==8   or Dia==15 or Dia==22 or Dia==29):	DiaSem = (DoomAnio + 5) % 7
		elif(Dia==2 or Dia==9   or Dia==16 or Dia==23 or Dia==30):	DiaSem = (DoomAnio + 6) % 7
		elif(Dia==3 or Dia==Oct or Dia==17 or Dia==24 or Dia==31):	DiaSem =  DoomAnio % 7
		elif(Dia==4 or Dia==11  or Dia==18 or Dia==25):				DiaSem = (DoomAnio + 1) % 7
		elif(Dia==5 or Dia==12  or Dia==19 or Dia==26):				DiaSem = (DoomAnio + 2) % 7
		elif(Dia==6 or Dia==13  or Dia==20 or Dia==27):				DiaSem = (DoomAnio + 3) % 7
		elif(Dia==7 or Dia==14  or Dia==21 or Dia==28):				DiaSem = (DoomAnio + 4) % 7
		
	elif(Mes==11 and (Dia >= 1 and Dia <= 30)):
		
		if(  Dia==1   or Dia==8  or Dia==15 or Dia==22 or Dia==29):	DiaSem = (DoomAnio + 1) % 7
		elif(Dia==2   or Dia==9  or Dia==16 or Dia==23 or Dia==30):	DiaSem = (DoomAnio + 2) % 7
		elif(Dia==3   or Dia==10 or Dia==17 or Dia==24):			DiaSem = (DoomAnio + 3) % 7
		elif(Dia==4   or Dia==11 or Dia==18 or Dia==25):			DiaSem = (DoomAnio + 4) % 7
		elif(Dia==5   or Dia==12 or Dia==19 or Dia==26):			DiaSem = (DoomAnio + 5) % 7
		elif(Dia==6   or Dia==13 or Dia==20 or Dia==27):			DiaSem = (DoomAnio + 6) % 7
		elif(Dia==Nov or Dia==14 or Dia==21 or Dia==28):			DiaSem =  DoomAnio % 7
		
	elif(Mes==12 and (Dia >= 1 and Dia <= 31)):
		
		if(  Dia==1 or Dia==8   or Dia==15 or Dia==22 or Dia==29):	DiaSem = (DoomAnio + 3) % 7
		elif(Dia==2 or Dia==9   or Dia==16 or Dia==23 or Dia==30):	DiaSem = (DoomAnio + 4) % 7
		elif(Dia==3 or Dia==10  or Dia==17 or Dia==24 or Dia==31):	DiaSem = (DoomAnio + 5) % 7
		elif(Dia==4 or Dia==11  or Dia==18 or Dia==25):				DiaSem = (DoomAnio + 6) % 7
		elif(Dia==5 or Dia==Dic or Dia==19 or Dia==26):				DiaSem =  DoomAnio % 7
		elif(Dia==6 or Dia==13  or Dia==20 or Dia==27):				DiaSem = (DoomAnio + 1) % 7
		elif(Dia==7 or Dia==14  or Dia==21 or Dia==28):				DiaSem = (DoomAnio + 2) % 7



def Chk_Mes(Mesy):
	
	Mes = Mesy.lower()
	
	try:
		Mes = int(Mes)
		
		if Mes == 1 or Mes == 2 or Mes == 3 or Mes == 4 or Mes == 5 or Mes == 6 \
		or Mes == 7 or Mes == 8 or Mes == 9 or Mes == 10 or Mes == 11 or Mes == 12:
			return Mes
		else:
			print("\n\n\t [!] No Existe El Mes", Mesy)
	except:
		
		if Mes == "enero" or Mes == "ene": Mes = 1
		elif Mes == "febrero" or Mes == "feb": Mes = 2
		elif Mes == "marzo" or Mes == "mar": Mes = 3
		elif Mes == "abril" or Mes == "abr": Mes = 4
		elif Mes == "mayo" or Mes == "may": Mes = 5
		elif Mes == "junio" or Mes == "jun": Mes = 6
		elif Mes == "julio" or Mes == "jul": Mes = 7
		elif Mes == "agosto" or Mes == "ago": Mes = 8
		elif Mes == "septiembre" or Mes == "sep": Mes = 9
		elif Mes == "octubre" or Mes == "oct": Mes = 10
		elif Mes == "noviembre" or Mes == "nov": Mes = 11
		elif Mes == "diciembre" or Mes == "dic": Mes = 12
		else:
			print("\n\n\t [!] No Existe El Mes", Mesy)
			
		return Mes
	
	
#=======================================================================

DiaSem = 0
DoomAnio = 0


def Main():
	
	Fecha = input("\n\n\t Fecha: ")
	
	Dia, Mes, Anio = getFecha(Fecha)
	Dia, Anio = int(Dia), int(Anio)
	
	Mes = Chk_Mes(Mes)
	
	EsBisiesto = Bisiesto(Anio)
	
	FValida = ValidarFecha(Dia, Mes, EsBisiesto)
	
	if(FValida == False):
		
		print("\n\t\t [!] Fecha Invalida.")
		print("\n\n\t Modo de Uso:\n\n\t\t Día/Mes/Año   o   Día-Mes-Año")
		os.system("Pause > Nul && cls")
		return
	
	if(EsBisiesto == True): print("\n\t [*] Bisiesto: Si.", end="")
	else: print("\n\t [*] Bisiesto: No.", end="")
	
	DBS = getDiaBaseSiglo(Anio)
	
	if(DBS==0):   print("\n\t [*] Doomsday Base Del Siglo: Domingo", end="")
	elif(DBS==2): print("\n\t [*] Doomsday Base Del Siglo: Martes", end="")
	elif(DBS==3): print("\n\t [*] Doomsday Base Del Siglo: Miércoles", end="")
	elif(DBS==5): print("\n\t [*] Doomsday Base Del Siglo: Viernes", end="")
	
	DBD = getDiaBaseDecada(Anio)
	getDoomsday(DBD, DBS)
	CalcularDD(Dia, Mes, EsBisiesto)
	
	Anio = str(Anio)
	if(DoomAnio==0):   print("\n\t [*] Doomsdays del Año " + Anio + ": Domingo")
	elif(DoomAnio==1): print("\n\t [*] Doomsdays del Año " + Anio + ": Lunes")
	elif(DoomAnio==2): print("\n\t [*] Doomsdays del Año " + Anio + ": Martes")
	elif(DoomAnio==3): print("\n\t [*] Doomsdays del Año " + Anio + ": Miércoles")
	elif(DoomAnio==4): print("\n\t [*] Doomsdays del Año " + Anio + ": Jueves")
	elif(DoomAnio==5): print("\n\t [*] Doomsdays del Año " + Anio + ": Viernes")
	elif(DoomAnio==6): print("\n\t [*] Doomsdays del Año " + Anio + ": Sábado")
	
	if(DiaSem==0):   print("\n\n ------> [+] Dia De La Semana: Domingo")
	elif(DiaSem==1): print("\n\n ------> [+] Dia De La Semana: Lunes")
	elif(DiaSem==2): print("\n\n ------> [+] Dia De La Semana: Martes")
	elif(DiaSem==3): print("\n\n ------> [+] Dia De La Semana: Miércoles")
	elif(DiaSem==4): print("\n\n ------> [+] Dia De La Semana: Jueves")
	elif(DiaSem==5): print("\n\n ------> [+] Dia De La Semana: Viernes")
	elif(DiaSem==6): print("\n\n ------> [+] Dia De La Semana: Sábado")



#=======================================================================


if __name__ == "__main__":

	while True:
		
		try:
			
			Main()
			
		except KeyboardInterrupt:
			
			#~ print("\n\n\t\t [+] Bye bye...\n\n\n")
			#~ os.system("Pause > Nul")
			#~ break
			
			os.system("cls")
			
		except: print("\n\n\t\t [!] Error")


