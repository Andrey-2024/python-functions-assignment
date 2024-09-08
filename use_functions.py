def add_funds(balance):
    """
    Функция для пополнения счета.
    :param balance: текущий баланс
    :return: обновленный баланс
    """
    amount = float(input('Введите сумму пополнения: '))
    balance += amount
    print(f'Счет пополнен. Текущий баланс: {balance}')
    return balance


def make_purchase(balance, purchases):
    """
    Функция для совершения покупки.
    :param balance: текущий баланс
    :param purchases: список с историей покупок
    :return: обновленный баланс и история покупок
    """
    amount = float(input('Введите сумму покупки: '))
    if amount > balance:
        print('Недостаточно средств на счете.')
    else:
        item = input('Введите название покупки: ')
        balance -= amount
        purchases.append((item, amount))
        print(f'Покупка "{item}" на сумму {amount} совершена. Остаток на счете: {balance}')
    return balance, purchases


def show_purchase_history(purchases):
    """
    Функция для отображения истории покупок.
    :param purchases: список с историей покупок
    :return: None
    """
    if purchases:
        print('История покупок:')
        for i, (item, amount) in enumerate(purchases, 1):
            print(f'{i}. {item} - {amount}')
    else:
        print('История покупок пуста.')


def main():
    balance = 0.0
    purchases = []

    while True:
        print('\n1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            balance = add_funds(balance)
        elif choice == '2':
            balance, purchases = make_purchase(balance, purchases)
        elif choice == '3':
            show_purchase_history(purchases)
        elif choice == '4':
            print('Выход из программы.')
            break
        else:
            print('Неверный пункт меню.')

if __name__ == '__main__':
    main()
