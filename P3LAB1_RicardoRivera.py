Red = int(input())
Green = int(input())
Blue = int(input())

Grey = Red

if Green < Grey:
    Grey = Green
if Blue < Grey:
    Grey = Blue
    
Red = Red - Grey
Green = Green - Grey
Blue = Blue - Grey

print(Red, Green, Blue)
