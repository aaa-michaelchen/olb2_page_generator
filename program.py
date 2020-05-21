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


def get_node_contents(node_name):
    inputs = {
        'node_name': node_name,
    }
    return inputs


def save(name, data):
    file = get_full_path(name, 'txt')
    print(f'saving to {file}')
    with open(file, 'w') as fout:
        for line in data:
            fout.write(f'{line}')


def handle_add_node_files(node_name, template):
    load_and_save(node_name, 'base_node_template')


def load_and_save(node_name, template):
    src = load(template)
    inputs = get_node_contents(node_name)
    result = src.substitute(inputs)
    save(node_name, result)


def main():
    header()

    node_name = input('node name: ')
    handle_add_node_files(node_name, 'base_node_template')

    print('done')


if __name__ == '__main__':
    main()
