import os
from string import Template
from dotenv import load_dotenv

load_dotenv()

VIEW_NODES_PATH = os.environ['VIEW_NODES_PATH']
VIEW_PRESENTATIONS_PATH = os.environ['VIEW_PRESENTATIONS_PATH']

def header():
    print('-------------------------')
    print('-----------gen-----------')
    print('-------------------------')


def get_content(page_name, flow):
    content = {
        'page_name': page_name,
        'flow': flow,
    }
    return content


def handle_add_files(content):
    base_node_full_path = VIEW_NODES_PATH + 'Base/' + content['flow']
    base_presentation_full_path = VIEW_PRESENTATIONS_PATH + 'Base/' + content['flow']

    file_type = input('What file type? [N]ode, [P]resentation, or [B]oth: ')
    state = input('What state? [CA], [TX], or [B]oth: ')

    if file_type == 'B':
        process_update(content, base_node_full_path, 'base_node_template')
        handle_add_state_files(content, VIEW_NODES_PATH, state, 'state_node_template')

        process_update(content, base_presentation_full_path, 'base_presentation_template')
        handle_add_state_files(content, VIEW_PRESENTATIONS_PATH, state, 'state_presentation_template')
    elif file_type == 'N':
        process_update(content, base_node_full_path, 'base_node_template')
        handle_add_state_files(content, VIEW_NODES_PATH, state, 'state_node_template')

    elif file_type == 'P':
        process_update(content, base_presentation_full_path, 'base_presentation_template')
        handle_add_state_files(content, VIEW_PRESENTATIONS_PATH, state, 'state_presentation_template')


def handle_add_state_files(content, destination_base_path, state, template):
    ca_full_path = destination_base_path + 'CA/' + content['flow']
    tx_full_path = destination_base_path + 'TX/' + content['flow']

    if state == 'B':
        process_update(content, ca_full_path, template)
        process_update(content, tx_full_path, template)
    elif state == 'CA':
        process_update(content, ca_full_path, template)
    elif state == 'TX':
        process_update(content, tx_full_path, template)


def process_update(content, dest, template):
    save_file_by_template(content, dest, template)
    handle_update_index(content['page_name'], dest)


def save_file_by_template(content, destination_path, template):
    src = load_template(template)
    result = src.substitute(content)
    save(content, destination_path, result)


def load_template(name):
    template_path = 'templates'
    file_path = get_full_path(template_path, f'{name}.txt')
    filein = open(file_path)
    src = Template(filein.read())
    return src


def save(content, dest, data):
    name = content['page_name']
    file = get_full_path(dest, f'{name}.ts')
    print(f'saving to {file}')
    with open(file, 'w') as fout:
        for line in data:
            fout.write(f'{line}')


def handle_update_index(page_name, dest):
    index_data = load_index_data(dest)
    updated_data = append_data(index_data, page_name)
    update_index_file(updated_data, dest)


def load_index_data(dest):
    file_path = get_full_path(dest, 'index.ts')
    data = []
    with open(file_path) as fin:
        for line in fin.readlines():
            if line.rstrip():
                data.append(line.rstrip())
    return data


def append_data(data, page_name):
    export_string = f"export * from './{page_name}';"
    data.append(export_string)
    return data


def update_index_file(data, dest):
    file_path = get_full_path(dest, 'index.ts')
    print(f'updating index at {file_path}')
    with open(file_path, 'w') as fout:
        for line in data:
            fout.write(f'{line}\n')


def get_full_path(*args):
    return os.path.abspath(os.path.join('.', *args))


def main():
    header()

    page_name = input('page name: ')
    flow = input('which flow (ie. discountFlow): ')

    content = get_content(page_name, flow)
    handle_add_files(content)

    print('done')


if __name__ == '__main__':
    main()
