import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    template = 'Hello, {}!'
    print(template.format(name))


if __name__ == '__main__':
    welcome_user()
