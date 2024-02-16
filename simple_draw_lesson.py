import simple_draw as sd

sd.resolution = (1000,500)

def triangle(point, angle = 0):
    pass

    point = sd.get_point(200, 100)

    vector1 = sd.get_vector(start_point = point, angle = angle, length = 200, width = 3)
    vector1.draw()
    vector2 = sd.get_vector(start_point = vector1.start_point, angle = angle + 120, length = 200, width = 3)
    vector2.draw()
    vector3 = sd.get_vector(start_point = vector2.start_point, angle = angle + 240, length = 200, width = 3)
    vector3.draw()

    sd.sleep(50)

triangle(1,2)