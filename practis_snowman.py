import simple_draw as sd


sd.resolution = (1000,600)
y = 500
x = 100
while True:
    sd.clear_screen()
    point_0 = sd.get_point(x, y)
    sd.snowflake(center=point_0, factor_a=0.6, length=50)
    y -= 50
    x = x * 1.1
    if y < 40:
        break
    sd.sleep(0.5)
    if sd.user_want_exit():
        break

sd.pause()