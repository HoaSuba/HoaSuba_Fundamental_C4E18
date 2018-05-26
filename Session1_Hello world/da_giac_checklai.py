from turtle import *

shape("turtle")
speed(-1)
color("green")

# Hỏi cú pháp ở đây sai ở đâu mà vì sao k ra?
input("n")
m = int(n)
for i in range(m):
    forward(100)
    left(360/m)

mainloop()
