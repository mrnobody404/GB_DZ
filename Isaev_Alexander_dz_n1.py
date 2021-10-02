#1 задание
def conversion(sec):
  seconds = sec % 60
  minutes = (sec // 60) % 60
  hours = (sec // 3600) % 24
  days = (sec // 86400)
  print(f'Дней: {days} Часов: {hours} Минут: {minutes} Секунд {seconds}')

sec = int(input('Введите число: '))
conversion(sec)