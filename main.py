"""

projekt_1.py: první projekt do Engeto Online Python Akademie


autor: Martin Nováček

email: mnovacek@me.com

discord: Novicce #7276

"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
    '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''',
]

REGISTERED_USERS = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}


def log_in():
    username = input('username:')
    password = input('password:')
    if username not in REGISTERED_USERS.keys() or password != REGISTERED_USERS[username]:
        print('Unregistered user or bad password, terminating the program...')
        exit(1)
    print('----------------------------------------')
    print(f'Welcome to the app, {username}.')
    print(f'We have {len(TEXTS)} texts to be analyzed.')


def choose_text():
    print('----------------------------------------')
    choice = int(input(f'Enter a number between 1 and {len(TEXTS)} to select:'))
    if choice < 1 or choice > len(TEXTS):
        print('No text available, terminating the program...')
        exit(2)
    return choice - 1


def make_stats(text):
    text = text.strip()
    text = text.replace('\n', ' ')
    words = text.split(' ')
    res = {
        'words_cnt': len(words),
        'titlecase_cnt': 0,
        'uppercase_cnt': 0,
        'lowercase_cnt': 0,
        'numeric_cnt': 0,
        'sum': 0,
        'histogram': {},
    }
    histogram = {}

    for word in words:
        word = ''.join(c for c in word if c.isalnum())
        if word.isnumeric():
            res['numeric_cnt'] += 1
            res['sum'] += int(word)
        else:
            if word.istitle():
                res['titlecase_cnt'] += 1
            elif word.isupper():
                res['uppercase_cnt'] += 1
            elif word.islower():
                res['lowercase_cnt'] += 1

        if len(word) in histogram:
            histogram[len(word)] += 1
        else:
            histogram[len(word)] = 1

    return res, histogram


def print_stats(stats):
    print('----------------------------------------')
    print(f'There are {stats["words_cnt"]} words in the selected text.')
    print(f'There are {stats["titlecase_cnt"]} titlecase words.')
    print(f'There are {stats["uppercase_cnt"]} uppercase words.')
    print(f'There are {stats["lowercase_cnt"]} lowercase words.')
    print(f'There are {stats["numeric_cnt"]} numeric strings.')
    print(f'The sum of all the numbers {stats["sum"]}')


def print_histogram(histogram):
    print('----------------------------------------')
    print('LEN|    OCCURENCES    |NR.')
    print('----------------------------------------')
    for i in range(1, max(histogram.keys()) + 1):
        cnt = histogram[i] if i in histogram else 0
        print(f'{i : >3}|{"*" * cnt : <18}|{cnt}')


def main():
    log_in()
    choice_idx = choose_text()
    stats, histogram = make_stats(TEXTS[choice_idx])
    print_stats(stats)
    print_histogram(histogram)


if __name__ == '__main__':
    main()
