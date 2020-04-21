import reports
# Printing functions


def printing_count_games(file_name):
    print("There are", reports.count_games(file_name), "games in the file.")


def printing_decide(file_name):
    year = str(input("What year would you like to check? "))
    if reports.decide(file_name, year):
        print("There is a game for year %s." % year)
    else:
        print("There is no game for year %s." % year)


def printing_get_latest(file_name):
    print("The latest game was %s." % reports.get_latest(file_name))


def printing_count_by_genre(file_name, genre):
    print("We have", reports.count_by_genre(file_name, genre), "games in",
          genre, "genre")


def printing_get_line_number_by_title(file_name, title):
    print("The line number of %s is %d" %
          (title, reports.get_line_number_by_title(file_name, title)))

printing_decide("game_stat.txt")