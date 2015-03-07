from time import sleep
import unicornhat as u

try:
    while True:
        for i in range(8):
                for j in range(8):
                        u.brightness(1.0)
                        u.set_pixel(i,j,255,0,0)
                        u.show()
                        sleep(0.01)
        sleep(2)
        for i in range(8):
                for j in range(8):
                        u.brightness(1.0)
                        u.set_pixel(i,j,0,255,0)
                        u.show()
                        sleep(0.01)
        sleep(2)
        for i in range(8):
                for j in range(8):
                        u.brightness(1.0)
                        u.set_pixel(i,j,0,0,255)
                        u.show()
                        sleep(0.01)
        sleep(2)
except KeyboardInterrupt:
    u.clean_shutdown()
