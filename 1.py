import math
room= int(input())
if(room<=32):
    podezd = math.ceil (room/8)
    print("Подъезд",podezd)
    if(room>8):
        print("Этаж",room-8*math.floor((room-1)/8) )
    else:
        print("Этаж", room)
else:
    print("Нет такой квартиры")