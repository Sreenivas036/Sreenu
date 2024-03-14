print("\n\n WELCOME TO STUDENT MARKS PROJECT \n\n")
tel=float(input("enter telugu subject marks:"))
eng=float(input("enter english subject marks:"))
mat=float(input("enter maths subject marks:"))
sci=float(input("enter science subject marks:"))
soc=float(input("enter social subject marks:"))
hin=float(input("enter hindi subject marks:"))
print("\n\n\n**********************************************************************")
print("\n\n scored subjects")
print("\n the telugu subject marks are",tel)
print("\n the english subject marks are",eng)
print("\n the maths subjectmarks are",mat)
print("\n the science subject marks are",sci)
print("\n the social subject marks are",soc)
print("\n the hindi subject marks are",hin)
print("\n\n\n***************************************************************************")
print("\n total maarks on 6 subjects")
tot=tel+eng+mat+sci+soc+hin
print("\n\n the total six subject marks are:",tot)
print("\n average marks")
avg=tot/6
print("\n the six subjects average marks are:",avg)
print("\n\n\n\n*************************************************************************")
print("\n\n highest marks subjects")
if(tel>eng and tel>mat and tel>sci and tel>soc and tel>hin):
    print("\n the telugu subject marks are highest in given six subjects:",tel)
elif(eng>tel and eng>mat and eng>sci and eng>soc and eng>hin):
    print("\n the english subjecst marks are higest in given six subjects:",eng)
elif(mat>tel and mat>eng and mat>sci and mat>soc and mat>hin):
    print("\n the maths subjects marks are highest in given six subjects:",mat)
elif(sci>tel and sci>eng and sci>mat and sci>soc and sci>hin):
    print("\n the science subjects marks are highest in given six subjects:",sci)
elif(soc>tel and soc>eng and soc>mat and soc>sci and soc>hin):
    print("\n the social subject marks are highest in given six subjects:",soc)
elif(hin>tel and hin>eng and hin>mat and hin>sci and hin>soc):
    print("\n the hindi subject marks are highest in given six subjects:",hin)
    print("\n\n\n\n*********************************************************************************")
    print("\n\n Lowest marks subjects")
if(tel<eng and tel<mat and tel<sci and tel<soc and tel<hin):
    print("\n the telgu subject marks are lowest in given six subjects:",tel)
elif(eng<tel and eng<mat and eng<sci and eng<soc and eng<hin):
    print("\n the english subject marks are lowest in given six subjects:",eng)
elif(mat<tel and mat<eng and mat<sci and mat<soc and mat<hin):
    print("\n the maths subject marks are lowest in given six subjects:",mat)
elif(sci<tel and sci<eng and sci<mat and sci<soc and sci<hin):
    print("\n the science subject marks are lowest in given six subjects:",sci)
elif(soc<tel and soc<eng and soc<mat and soc<sci and soc<hin):
    print("\n the social subject marks are lowest in given six subjects:",soc)
elif(hin<tel and hin<eng and hin<mat and hin<sci and hin<soc):
    print("\n the hindhi subject marks are lowest in given six subjects:",hin)
    print("\n\n\n******************************************************************************************")
    print("\n\n failed subjects",)
if(tel<35):
    print("\n failed in telugu subjects",tel)
if(eng<35):
    print("\n failed in english subjects",eng)
if(mat<35):
    print("\n failed in maths subjects",mat)
if(sci<35):
    print("\n failed in science subjects",sci)
if(soc<35):
    print("\n failed in social subjects",soc)
if(hin<35):
    print("\n failed in hindi subjects",hin)





