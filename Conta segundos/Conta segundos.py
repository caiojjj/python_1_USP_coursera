segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

print(segundos // 60 ** 2 , "Horas", (segundos % 60 **2) // 60,"Minutos", segundos % 60 , "Segundos")