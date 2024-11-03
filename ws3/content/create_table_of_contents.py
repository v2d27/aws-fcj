##########################################
# Run commnand
#
# python create_table_of_contents.py
##########################################


import os
import re


def dir_list(path):
    # List all directories in the given path
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def file_read(file):
    # Open the file and read its contents
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()


# Specify the path you want to create
def create_contents_for_dir(path):
    directories = dir_list(path)
    if len(directories) == 0: return
    contents = "#### Contents"
    for d in directories:
        index_file = path + "/" + d + "/_index.md"
        if not os.path.exists(index_file): continue

        file_data = file_read(index_file)
        if len(file_data) == 0: continue

        match = re.search(r'title\s*:\s*"([^"]*)"', file_data)
        if not match: continue
        title = match.group(1)

        match = re.search(r'pre\s*:\s*.+<b>\s*(\d+\.\d*\.*)\s*</b>', file_data)
        if not match: continue
        pre = match.group(1)

        fix = "/" + d
        if path != "./": fix = path + "/" + d
        fix = fix.replace("./", "/")

        contents += "\n- [{} {}]({})".format(pre, title, fix)

    main_index_file = path + "/_index.md"
    if os.path.exists(main_index_file):
        with open(main_index_file, 'r', encoding='utf-8') as file: data = file.readlines()
        data += "\n\n" + contents
        with open(main_index_file, 'w', encoding='utf-8') as file: file.writelines(data)

    return contents


list_dirs = []
def list_subdir(path):
    if os.path.isdir(path):
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            # If the entry is a directory
            if os.path.isdir(full_path):
                has_subdir = True
                if len(dir_list(full_path)) > 0:
                    list_dirs.append(full_path.replace("\\", "/"))  # Print the directory path
                list_subdir(full_path)


if __name__ == "__main__":
    target_dir = "."
    contents = create_contents_for_dir(target_dir)
    print(contents)

    # sub folder
    list_subdir(target_dir)
    if len(list_dirs) == 0: exit()

    for d in list_dirs:
        print(d)
        contents = create_contents_for_dir(d)
        print(contents)


