usd = 56
euro = 69
kzt = 5
gpb = 78

money = int(input("Введите сумму, которую вы хотите обменять: "))
currency = int(input("Укажите код валюты (доллары - 400, евро - 401, kzt - 402, gpb - 403): "))

if currency == 400:
    cache = round(money / usd, 2)
    print("Валюта: доллары США")
elif currency == 401:
    cache = round(money / euro, 2)
    print("Валюта: евро")
elif currency == 402:
    cache = round(money / kzt, 2)
    print("Валюта: kzt")
elif currency == 403:
    cache = round(money / gpb, 2)
    print("Валюта: gpb")
else:
    cache = 0
    print("Неизвестная валюта")

print("К получению:", cache)