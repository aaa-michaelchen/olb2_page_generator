import os
from string import Template


def header():
    print('-------------------------')
    print('-----------gen-----------')
    print('-------------------------')


def load(dest, name):
    file_path = get_full_path(dest, f'{name}.txt')
    filein = open(file_path)
    src = Template(filein.read())
    return src


def get_full_path(*args):
    return os.path.abspath(os.path.join('.', *args))


def get_node_content(node_name, flow):
    content = {
        'node_name': node_name,
        'flow': flow,
    }
    return content


def save(content, dest, data):
    name = content['node_name']
    file = get_full_path(dest, f'{name}.txt')
    print(f'saving to {file}')
    with open(file, 'w') as fout:
        for line in data:
            fout.write(f'{line}')


def handle_add_node_files(content):
    print('HANDLING NODE FILES')
    base_node_destination_path = 'baseNode'
    state_node_destination_path = 'stateNode'

    load_and_save(content, base_node_destination_path, 'base_node_template')
    load_and_save(content, state_node_destination_path, 'state_node_template')


def handle_add_presentation_files(content):
    print('HANDLING PRESENTATION FILES')
    base_presentation_destination_path = 'basePresentation'
    state_presentation_destination_path = 'statePresentation'

    load_and_save(content, base_presentation_destination_path, 'base_presentation_template')
    load_and_save(content, state_presentation_destination_path, 'state_presentation_template')


def load_and_save(content, destination_path, template):
    src = load('templates', template)
    result = src.substitute(content)
    save(content, destination_path, result)


def main():
    header()

    node_name = input('node name: ')
    flow = input('which flow: ')

    node_content = get_node_content(node_name, flow)

    handle_add_node_files(node_content)
    handle_add_presentation_files(node_content)

    print('done')


if __name__ == '__main__':
    main()
