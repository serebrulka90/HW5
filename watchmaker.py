# Нужно написать функцию, которая позволит Вам конвертировать указанное Вами число секунд в формат записи дни:часы:минуты:секунды
def convertTime (mySeconds):
    day = (mySeconds // 86400)
    hour = ((mySeconds % 86400) // 3600)
    minutes = (((mySeconds % 86400) % 3600) // 60)
    seconds = (((mySeconds % 86400) % 3600) % 60)
    return str(day) + ':' + str(hour) + ':' + str(minutes) + ':' + str(seconds)

print(convertTime(300000))