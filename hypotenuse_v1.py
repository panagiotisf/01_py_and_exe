#calcullation of hypotenuse (distance) between two points in Easting, Northing.
print ('Calculate the distance between two points from Eastings, Northings')
print ('Please test and report any bugs to PF :)')
#insert points
X1 = float(input ("Please insert Easting X1:"))
Y1 = float(input ("Please insert Northing Y1:"))
X2 = float(input ("Please insert Easting X2:"))
Y2 = float(input ("Please insert Northing Y2:"))
# d is the distance between the epoints
# could be like that?: d=(((X1-X2)**2)+((Y1-Y2)**2))**0.5
# I will split the steps as per bellow
a2=(X1-X2)**2
b2=(Y1-Y2)**2
d=(a2+b2)**0.5
#the above line gives a dfloatin g number with lot of decimals. The round bellow gives t2 decimal points
output= round(d,2)
print ('The distance between points 1 and 2 is : ',output)


