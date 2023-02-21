t0 = float(input('Enter t\u2080: '))
y0 = float(input('Enter y(t\u2080): '))
h = float(input('Enter \u0394t: '))
max_t = float(input("Enter t\u2098\u2090\u2093: "))
f = input("Enter f(x,y): ")
ts = [t0]
ys = [y0]
t = t0
y = y0
for i in range(int(max_t/h)):
    fn = eval(f)
    y = y + h * fn
    t = t + h
    ts.append(round(t,4))
    ys.append(round(y,4))
print(ts)
print(ys)