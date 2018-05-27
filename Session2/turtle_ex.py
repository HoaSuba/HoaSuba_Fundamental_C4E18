from turtle import *
shape("turtle")
color("green")
speed(-1)


lenght = 5
for i in range(50):
    forward(lenght)
    left(90)
    lenght += 5 # tăng giá trị chiều dài lên 5

mainloop()  
