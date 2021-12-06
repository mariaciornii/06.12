with open ('desktop/Lista Clasei 11A.txt', 'r') as f:
       list1=f.readlines()
media,y,u=0,0,0
media_eng=0
media_germ=0
for i in list1:
   list2=i.split()
   media+=int(list2[2])
   if list2[3]=='engleza' or list2[3]=='Engleza':
      media_eng+=int(list2[2])
      y+=1
      with open('desktop/output_eng.txt','a') as f:
         x=list2[0]+' '+list2[1]+'\n'
         f.write(x)
   else:
    media_germ+=int(list2[2])
    u+=1
    with open('desktop/output_germ.txt','a') as f:
        x=list2[0]+' '+list2[1]+'\n'
        f.write(x)
with open('desktop/output_eng.txt','a') as f:
    f.write('Media grupului I : '+str(media_eng/y))
with open('desktop/output_germ.txt','a') as f:
    f.write('Media grupului II : '+str(media_germ/u))
print('Media clasei : ',media/len(list1))