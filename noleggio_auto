#1
import pprint
pp=pprint.PrettyPrinter(indent=4)
diz={"AA123BB":[("Giugno",9,1293),("Luglio",7,3231),("Agosto",7,4020),("Settembre",6,3928)],"AB345CD":[("Giugno",8,1391),("Luglio",6,1234),("Agosto",9,4932),("Settembre",8,2872)],"CD456FF":[("Giugno",7,2872),("Luglio",6,3273),("Agosto",4,3211),("Settembre",8,2827)]}
#2
diz["ZZ999CD"]=[("Giugno",10,2000),("Luglio",10,2000),("Agosto",10,2000),("Settembre",10,2000)]
#3
print(f"info Luglio: {(diz['AA123BB'][1][1])} {(diz['AA123BB'][1][2])}")
#4
print(f"info noleggi Luglio: {(diz['AA123BB'][1][1])}")
#5
somma=0
for i in range(len(diz["AB345CD"])):
  somma+=diz["AB345CD"][i][2]
print(f"la somma di tutti i km di tutti i mesi di AB345CD è: {somma}")
#6
somma=0
for chiave in diz.keys():
  for i in range (len(diz[chiave])):
   somma+=diz[chiave][i][2]
print(f"la somma di tutti i km di tutti i mesi di tutte le targhe è: {somma}")
#7
somma=0
max=0
for i in range (len(diz["CD456FF"])):
  if(diz["CD456FF"][i][2]>max):
    max=diz["CD456FF"][i][2]
    mesemax=diz["CD456FF"][i][0]
print(f"sono stati fatti più km nel mese {mesemax} con {max} km")
