import turtle



# USER INPUT
print("ex: '50 of 100 people are women. 50 of 100 people are men.'")
print("element = people")
print("value 1 = 50, value 1 description = women")
print("value 2 = 50, value 2 description = men")

element = input("in what field are the elements? ")

print("input descriptions and values; if using less than four elements, input '0' for the description")

a_des = input("element 1 description: ")
a = int(input("element 1 value: "))
b_des = input("element 2 description: ")
b = int(input("element 2 value: "))
c_des = input("element 3 description: ")
if c_des > 0:
    c = int(input("lement 3 value: "))
d_des = input("element 4 description: ")
if d > 0:
    d = int(input("element 4 value: "))
    
total = a + b + c + d


# CALCULATION
def indPercentage():
    a_1 = (a / total) *100
    b_1 = (b / total) *100
    c_1 = (c / total) *100
    d_1 = (d / total) *100

    a_2 = round(a_1,0)
    b_2 = round(b_1,0)
    c_2 = round(c_1,0)
    d_2 = round(d_1,0)

    if a > 0:
        print(a_2,"of 100",element,"are",a_des)
    if b > 0:
        print(b_2,"of 100",element,"are",b_des)
    if c > 0:
        print(c_2,"of 100",element,"are",c_des)
    if d > 0:
        print(d_2,"of 100",element,"are",d_des)
    
indPercentage()



# ARRAY
screen = turtle.getscreen()

turtle.setup(550,550)        
screen.bgcolor("#99ccff")

turtle.speed(10)
turtle.penup()
turtle.setpos(-225,225)
turtle.pendown()
turtle.fillcolor((99,59,59))

for i in range(0,10):
    for j in range(0,10):
        #if j = a_2:
            #turtle.fillcolor((255,179,71))
        #elif j = b_2:
            #turtle.fillcolor((240,248,255))
        #elif j = c_2:
            #turtle.fillcolor((245,245,245))
        #elif j = d_2:
            #turtle.fillcolor((255,179,71))
        turtle.begin_fill()
        turtle.circle(6)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
    turtle.penup()    
    turtle.setpos(-225,turtle.ycor()-50)
    turtle.pendown()


        


