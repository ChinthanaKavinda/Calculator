import math
P=int(input("Enter P:"))
Q=int(input("Enter Q:"))
Tita=int(input("Enter Tita:"))
Red=(math.radians(Tita))             #converts angle Tita from degrees to radians
print(int(P**2+Q**2+2*P*Q*math.cos(Red)),"without point")
R=float(P**2+Q**2+2*P*Q*math.cos(Red))
print(R,"with point")
print("Samprayukatha Balaya=",math.sqrt(R),"N")
A=float(P*math.sin(Red))
B=float(Q+P*math.cos(Red))
Alpha=float(A/B)
print("TanAlpha=",Alpha)
print("Alpha=",math.degrees(Alpha),"Degrees")
