todo = []
command = 'start'


def add(todo):
    global additions
    newitem = (input("Add an item:"))
    todo.append(newitem)


def lis(todo):
    for i, v in enumerate(todo):
        print(i + 1, v)


def mark(todo):
    item_marked = int(input("Which item would you like to mark? "))
    todo[item_marked - 1] = (f"[x] {todo[item_marked-1]}")
    return todo


def archive(todo):
    archive_index_list = []
    for i, v in enumerate(todo):
        if "[x]" in v:
            archive_index_list.append(i)
    for number in archive_index_list:
        todo.remove(todo[number])
    return todo


while command in {'start', 'list', 'add', 'mark', 'archive', 'exit'}:
    try:
        command = input(
            "what would you like to do? list, add, mark, archive or exit: ")
        if command == 'add':
            add(todo)
        if command == 'list':
            lis(todo)
        if command == 'mark':
            mark(todo)
        if command == 'archive':
            archive(todo)
        if command == 'exit':
            exit()
    finally:
        command = "start"
