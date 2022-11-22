#1
diz={"Giuseppe Gullo" : [("corsa campestre",(40,21,0),"Allievi"),("corsa 100mt",(0,12,0),"Juniores mas"),("corsa 200mt",(0,29,19),"Juniores mas")],
     "Antonio Barbera" : [("corsa campestre",(0,39,11),"Juniores fem"),("corsa 100mt",(0,18,0),"Juniores fem"),("corsa 200mt",(0,0,0),"Juniores fem")],
     "Nicola Esposito" : [("corsa campestre",(0,43,22),"Allievi"),("corsa 100mt",(0,14,0),"Juniores mas"),("corsa 200mt",(0,36,19),"Juniores mas")]}
     
#2
diz["Davide Casaro"]=[("corsa campestre",(43,19,0),"Allievi"),("corsa 100mt",(0,10,0),"Juniores mas"),("corsa 200mt",(0,55,10),"Juniores mas")]

#9:41 controllo invernizzi
#3 
agg=diz["Giuseppe Gullo"]
agg.append(("corsa ad ostacoli",(0,40,34),"Allievi"))
diz["Giuseppe Gullo"]=agg

agg=diz["Antonio Barbera"]
agg.append(("corsa ad ostacoli",(0,39,10),"Allievi"))
diz["Antonio Barbera"]=agg

agg=diz["Nicola Esposito"]
agg.append(("corsa ad ostacoli",(0,40,10),"Allievi"))
diz["Nicola Esposito"]=agg

agg=diz["Davide Casaro"]
agg.append(("corsa ad ostacoli",(0,40,26),"Allievi"))
diz["Davide Casaro"]=agg

#9:31 controllo prof invernizzi
#4
print("informazioni sulla corsa campestre di Giuseppe Gullo:",diz["Giuseppe Gullo"][0][1])

#9:31 controllo prof invernizzi
#5
print("informazioni sulla corsa 200mt di Nicola Esposito:",diz["Nicola Esposito"][2][1][0])
print("informazioni sulla corsa 200mt di Nicola Esposito:",diz["Nicola Esposito"][2][1][1])
print("informazioni sulla corsa 200mt di Nicola Esposito:",diz["Nicola Esposito"][2][1][2])

#9:45 controllo prof invernizzi
#6
print("il tempo di Antonio Barbera nella corsa 100mt è: min =",diz["Antonio Barbera"][1][1][0],"sec =",diz["Antonio Barbera"][1][1][1],"mil =",diz["Antonio Barbera"][1][1][2])

#10:16 controllo prof invernizzi
#7
for chiave in diz.keys():
  if(diz[chiave][1][2]=="Juniores mas"):
    min0=diz[chiave][1][1][0]*60+diz[chiave][1][1][1]+diz[chiave][1][1][2]/1000

for chiave in diz.keys():
  min=0
  if(diz[chiave][1][2]=="Juniores mas"):
    min+=diz[chiave][1][1][0]*60
    min+=diz[chiave][1][1][1]
    min+=diz[chiave][1][1][2]/1000
    if(min<min0):
      min0=min
print("il tempo minimo nella corsa 100mt della categoria Juniores mas è:",min0," di:",chiave)

#10:23 controllo prot invernizzi
#8
for chiave in diz.keys():
  if(diz[chiave][2][2]=="Juniores mas"):
    max0=diz[chiave][2][1][0]*60+diz[chiave][2][1][1]+diz[chiave][2][1][2]/1000
    
for chiave in diz.keys():
  max=0
  if(diz[chiave][2][2]=="Juniores mas"):
    max+=diz[chiave][2][1][0]*60
    max+=diz[chiave][2][1][1]
    max+=diz[chiave][2][1][2]/1000
    if(max>max0):
      max0=max

print("il tempo massimo nella corsa 200mt della categoria Juniores mas è:",max0," di:",chiave)

#10:06 controllo prof invernizzi
#9
media=0
cont=0
for chiave in diz.keys():
  if(diz[chiave][0][2]=="Allievi"):
    media+=diz[chiave][0][1][0]*60+diz[chiave][0][1][1]+diz[chiave][0][1][2]/1000
    cont+=1
print("la media della corsa camopestre della categoria allievi in secondi è:",media/cont)

#10
nome=cognome=""

def leggiNumeroPersoneValido():
  n=int(input("inserire numero di persone "))
  while(n<=0):
    n=int(input("inserire numero di persone "))
  return n

def leggiNomeValido():
  nome=""
  while len(nome)==0:
    nome=input("inserire nome ")
    if(len(nome)==0):
      print("devi inserire nome ")
  return nome

def leggiCognomeValido():
  cognome=""
  while len(cognome)==0:
    cognome=input("inserire cognome ")
    if(len(cognome)==0):
      print("devi inserire cognome ")
  return cognome

def leggiChiave():
  nome=leggiNomeValido()
  cognome=leggiCognomeValido()
  return nome+" "+cognome

def leggiDValidi():
  disciplina=input("inserire disciplina ")
  min=int(input("inserire minuti "))  
  while(min<0 or min>=60):
    print("input incorretto")
    min=int(input("inserire minuti "))

  sec=int(input("inserire secondi "))
  while(sec<0 or sec>=60):
   print("input incorretto")
   sec=int(input("inserire secondi "))

  mil=int(input("inserire millisecondi "))
  while(mil<0 or mil>=60):
   print("input incorretto")
   mil=int(input("inserire millisecondi "))

  return disciplina,(min,sec,mil)

def leggiDatiValidi():
  disciplina1=leggiDValidi()
  disciplina2=leggiDValidi()
  disciplina3=leggiDValidi()
  disciplina4=leggiDValidi()
  return [disciplina1,disciplina2,disciplina3,disciplina4]

def popola():
  n=leggiNumeroPersoneValido()
  for i in range(n):
    chiave=leggiChiave()
    dati=leggiDatiValidi()
    if(chiave in diz.keys()):
      print("contatto già presente")
    else:
      diz[chiave]=dati
  print(diz)

popola()
