# Report functions
def format_data(file_name):
    game_stat_dicts = []
    with open(file_name, "r+") as reader:
        for line in reader:
            line_elements_list = line.replace("\n", "").split("\t")
            line_elements_dict = {
                "name": line_elements_list[0],
                "sells": line_elements_list[1],
                "year": line_elements_list[2],
                "genre": line_elements_list[3],
                "publisher": line_elements_list[4]
            }
            game_stat_dicts.append(line_elements_dict)
    return game_stat_dicts


def count_games(file_name):
    """
    returns number
    'How many games are in the file'
    """
    return len(format_data(file_name))


def decide(file_name, year):
    """
    returns boolean
    'Is there a game for given year'
    """
    formatted_file = format_data(file_name)
    found = False
    for game_dict in formatted_file:
        if year == game_dict['year']:
            found = True
    return found


def get_latest(file_name):
    """
    returns string title;
    if there is more that one returns first from file.
    'Which was the latest game?'
    """
    formatted_file = format_data(file_name)
    years_list = [x['year'] for x in formatted_file]
    highest_year_index = years_list.index(max(years_list))
    names_list = [n['name'] for n in formatted_file]
    return names_list[highest_year_index]


def count_by_genre(file_name, genre):
    """
    returns a number
    'How many games do we have by genre'
    """
    number = 0
    formatted_file = format_data(file_name)
    for games_dict in formatted_file:
        for key, value in games_dict.items():
            if value == genre:
                number += 1
    return number


def get_line_number_by_title(file_name, title):
    """
    returns  number;
    if there is no game found, then raises ValueError exception
    'What is the line number of the given game (by title)'
    """
    formatted_file = format_data(file_name)
    exists = False
    for index, games_dict in enumerate(formatted_file):
        for key, value in games_dict.items():
            if value == title:
                exists = True
                return index + 1
    if not exists:
        raise ValueError("Non-existing game")
