usd = 56
euro = 70
bgn = 35
chf = 60

money = int(input("Введите сумму, которую вы хотите обменять: "))
currency = int(input("Укажите код валюты (доллары - 400, евро - 401, львы - 402, франки - 403): "))

if currency == 400:
    cache = round(money / usd, 2)
    print("Валюта: доллары США")
elif currency == 401:
    cache = round(money / euro, 2)
    print("Валюта: евро")
elif currency == 402:
        cache = round(money / bgn, 2)
        print("Валюта: Болгарский лев ")
elif currency == 403:
        cache = round(money / chf, 2)
        print("Валюта: Швейцарский франк ")
else:
    cache = 0
    print("Неизвестная валюта")

print("К получению:", cache)