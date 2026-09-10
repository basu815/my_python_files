rolls=[2,3,4,5,6]
marks=[30,65,90,50,20]
nz=zip(rolls,marks)
nd={k:("Pass" if v > 35 else "Fail" )for k,v in nz}
print(nd)
