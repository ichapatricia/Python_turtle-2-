import turtle

t = turtle.Turtle()
t.speed(20)
color = ['violet','indigo','blue','green','yellow','orange','red']

for i in range(50):
    k = i % 7
    t.color(color[k])
    t.circle(120)
    t.right(10)

turtle.done()