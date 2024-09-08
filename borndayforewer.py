def check_answer(question, correct_answer):
    """
    Функция задает вопрос пользователю и проверяет его ответ.
    :param question: вопрос, который задается пользователю
    :param correct_answer: правильный ответ на вопрос
    :return: None
    """
    answer = input(question)
    while answer != correct_answer:
        print("Не верно")
        answer = input(question)
    print("Верно")


def main():
    check_answer('Введите год рождения А.С.Пушкина:', '1799')
    check_answer('Введите день рождения Пушкина:', '6')


if __name__ == '__main__':
    main()
