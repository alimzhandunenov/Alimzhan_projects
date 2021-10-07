duration = int(input('Введите количество секунд'))
if duration < 60:
    print(duration, 'сек')
elif 3600 > duration >= 60:
    min = duration // 60
    sec = duration % 60
    print(min, 'мин', sec, 'сек')
elif 86400 > duration >= 3600:
    min = (duration//60) % 60
    sec = duration % 60
    h = duration // 3600
    print(h, 'ч', min, 'мин', sec, 'сек')
elif 2629743 > duration >= 86400:
    min = (duration//60) % 60
    sec = duration % 60
    h = duration % 86400 // 3600
    d = duration // 86400
    print(d, 'д', h, 'ч', min, 'мин', sec, 'сек')
elif 31556926 > duration >= 604800:
    min = (duration//60) % 60
    sec = duration % 60
    h = duration % 86400 // 3600
    d = duration % 604800 //86400
    w = duration // 2629743
    print(w, 'мес',d, 'д', h, 'ч', min, 'мин', sec, 'сек')
