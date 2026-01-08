budshet = int(input('Введите ваш бюджет в руб.: '))
nach_budshet = budshet
kategoria_glav = []
print('Для остановки подсчёта напишите Стоп')
print("Если в категории должно быть словосочетание, пожалуйста, "
      "вместо пробела используйте символ _")
schochic = 0

while True:
    user_input = input('Введите категорию и стоимость через пробел: ')

    if user_input.lower() == 'стоп':
        break

    kategoria, stoimost = user_input.split()
    stoimost = int(stoimost)
    budshet -= stoimost
    schochic += stoimost
    kategoria_glav.append((kategoria, stoimost))
if budshet < 0:
    print(f'Привышен лимит бюджета. Не хватает {abs(budshet)} рублей')
else:
    print("| Категория        | Сумма           |    %   |")
    print("|------------------|-----------------|--------|")

    for kategoria, summa in kategoria_glav:
        percent = (summa / nach_budshet) * 100
        print(f"| {kategoria:<16} | {summa:>10} руб. | {percent:>5.1f}% |")

    print("|------------------|-----------------|--------|")

    potracheno_percent = (schochic / nach_budshet) * 100
    print(f"| {'Потрачено':<16} | {f'{schochic} руб.':^15} | {potracheno_percent:>5.1f}% |")

    print("|------------------|-----------------|--------|")

    ostatok_percent = (budshet / nach_budshet) * 100
    print(f"| {'Осталось':<16} | {f'{budshet} руб.':^15} | {ostatok_percent:>5.1f}% |")