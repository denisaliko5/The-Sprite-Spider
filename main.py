import turtle

t = turtle.Turtle()
t.ht()
t.speed(0)
t.shape("circle")
t.stamp()

leg_nr = int(input("Enter the number of legs: "))
for i in range(leg_nr):
  t.shape("triangle")
  t.fd(50)
  t.stamp()
  t.bk(50)
  t.lt(360/leg_nr)