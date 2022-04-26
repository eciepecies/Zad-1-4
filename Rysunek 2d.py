import turtle # Importuję bibliotekę.

turtle.bgcolor("gray") # Ustawiam tło.
turtle.pensize(5) # Ustawiam wielkość źółwia.
turtle.speed(0.4) # Ustawiam prędkośc żółwia.

# Tworzę pętlę rysującą koła do momentu, aż wróci do tego samego miejsca i powstanie spirograf.
for i in range(6):
    for colours in ["red", "white"]: # Ustawiam kolory.
        turtle.color(colours) # Ustawiam zmianę kolorów.
        turtle.circle(260) # Ustawiam wielkość kół.
        turtle.left(30) # Odstęp pomiędzy rysowaniem kół w lewo.

turtle.done()  # Ustawiam żółwia, aby nie zamykał się po zakończeniu rysowania.


