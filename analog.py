from DrawingPanel import *
import datetime


def main():
    create_panel()

    while True:
        wn.set_title("ANALOG CLOCK")
        wn.draw_oval(100, 100, 300, 300, color="red")
        wn.draw_string("Hours Hand : Green", 20, 60, color="Green", font=str)
        wn.draw_string("Minute Hand : Red", 20, 80, color="Red", font=str)
        wn.draw_string("Second Hand : Yellow", 20, 100, color="Yellow", font=str)
        wn.draw_string("12", 290, 80, "black", font="")
        wn.fill_rect(248, 95, 5, 10, color="red")
        wn.fill_rect(248, 395, 5, 10, color="red")
        wn.fill_rect(95, 250, 10, 5, color="red")
        wn.fill_rect(395, 250, 10, 5, color="red")
        saniye = datetime.datetime.now().second
        dakika = datetime.datetime.now().minute
        saat = datetime.datetime.now().hour
        birim=str(saat)+" : "+str(dakika)+" : "+str(saniye)
        wn.draw_string(birim, 300, 50, "white")
        if saat <= 15:
            wn.draw_line(250, 250, 250 + 10 * saat, 100 + 10 * saat, color="Green")
        elif saat <= 30:
            x = saat - 15
            wn.draw_line(250, 250, 400 - x * 10, 100 + saniye * 10, color="green")
        elif saat <= 45:
            x = saat - 15
            y = saat - 30
            wn.draw_line(250, 250, 400 - x * 10, 400 - y * 10, color="green")
        else:
            x = saat - 45
            y = saat - 45
            wn.draw_line(250, 250, 100 + x * 10 - 10, 250 - y * 10, color="green")
        if dakika <= 15:
            wn.draw_line(250, 250, 250 + 10 * dakika, 100 + 10 * dakika, color="Red")
        elif dakika <= 30:
            x = dakika - 15
            wn.draw_line(250, 250, 400 - x * 10, 100 + saniye * 10, color="red")
        elif dakika <= 45:
            x = dakika - 15
            y = dakika - 30
            wn.draw_line(250, 250, 400 - x * 10, 400 - y * 10, color="red")
        else:
            x = dakika - 45
            y = dakika - 45
            wn.draw_line(250, 250, 100 + x * 10 - 10, 250 - y * 10, color="red")
        if saniye <= 15:
            wn.draw_line(250, 250, 250 + 10 * saniye, 100 + 10 * saniye, color="yellow")
        elif saniye <= 30:
            x = saniye - 15
            wn.draw_line(250, 250, 400 - x * 10, 100 + saniye * 10, color="yellow")
        elif saniye <= 45:
            x = saniye - 15
            y = saniye - 30
            wn.draw_line(250, 250, 400 - x * 10, 400 - y * 10, color="yellow")
        else:
            x = saniye - 45
            y = saniye - 45
            wn.draw_line(250, 250, 100 + x * 10 - 10, 250 - y * 10, color="yellow")
        wn.sleep(900)
        wn.clear()


def create_panel():
    global wn
    wn = DrawingPanel(600, 600, background="black")


main()
