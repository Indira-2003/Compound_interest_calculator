principle=0
rate=0
time=0

while principle<=0:
    principle= int(input("Enter the principle amount in $:"))
    if principle<0:
        print("The amount should not be zero")
    else:
        break
        
while rate<=0:
    rate= float(input("Enter the rate of interest in  :"))
    if rate <0:
        print("The rate of intrest should not be equl to zero")
    else:
        break
while time<=0:
    time=int(input("Enter the time in years:"))
    if time<0:
        print("The time should not be equal to zero")
    else:
        break

total=principle*pow((1+rate/100),time)
print(f"Balance after {time} years is :${total:.2f}")

