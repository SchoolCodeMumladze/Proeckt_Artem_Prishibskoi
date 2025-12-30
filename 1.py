budshet = int(input('Введите ваш бюджет в руб.: '))
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
    print("| Категория        | Сумма           |")
    print("|------------------|-----------------|")

    for kategoria___, Sum___ in kategoria_glav:
        print(f"| {kategoria___:<16} | {Sum___:>10} руб. |")
    print("|------------------|-----------------|")
    print(f"| {'Потрачено':<16} | {f'{schochic} руб.':^15} |")
    print("|------------------|-----------------|")
    print(f"| {'Осталось':<16} | {f'{budshet} руб.':^15} |")