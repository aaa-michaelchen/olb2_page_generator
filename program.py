import os
from string import Template


def header():
    print('-------------------------')
    print('-----------gen-----------')
    print('-------------------------')


def load(name):
    file_path = get_full_path(name, 'txt')
    filein = open(file_path)
    src = Template(filein.read())
    return src


def get_full_path(name, ext):
    return os.path.abspath(os.path.join('.', f'{name}.{ext}'))


def get_inputs(title, titleTwo, x):
    inputs = {
        'title': title,
        'titleTwo': titleTwo,
        'x': x,
    }
    return inputs


def save(data):
    file = get_full_path('new', 'txt')
    print(f'saving to {file}')
    with open(file, 'w') as fout:
        for line in data:
            fout.write(f'{line}')


def main():
    header()
    src = load('template')
    inputs = get_inputs('first', 'second', 'yourMom')
    result = src.substitute(inputs)
    save(result)
    print('done')


if __name__ == '__main__':
    main()
