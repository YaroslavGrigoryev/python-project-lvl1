import prompt


# noinspection TaskProblemsInspection,SpellCheckingInspection
def welcome_user():
    """ddfdf."""
    name = prompt.string('May I have your name? ')
    template = 'Hello, {}!'
    # noinspection TaskProblemsInspection
    print(template.format(name))


if __name__ == '__main__':

    welcome_user()
