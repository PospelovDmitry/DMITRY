euro = 60
usd = 57

print("Курсы валют на сегодняшний день: ","\n\tusd = ",usd,"\n\teuro =", euro)

money = int(input("Введите сумму в рублях которую вы хотите обменять: "))
currency = int(input("Введите код валюты который вы хотите обменять (Доллар - 1, Евро - 2)"))

if currency == 1:
    cache = round(money/usd,2)
    print("Валюта: Доллары США")
elif currency == 2:
    cache = round(money/euro,2)
    print("Валюта: Евро")
else:
    cache = 0
    print("Неизвестная валюта")
print("К получению:", cache)

