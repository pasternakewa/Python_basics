import reports as r

file_name = "game_stat.txt"
year = str(input("What year would you like to check? "))
genre = "RPG"
title = "Counter-Strike"
is_game_in_year = r.decide(file_name, year)


def exporting_results(file_name):
    with open("game_statistics_export.txt", "w") as export_file:
        export_file.write(str(r.count_games(file_name)) + "\n")
        export_file.write(("True" if is_game_in_year else "False") + "\n")
        export_file.write(str(r.get_latest(file_name)) + "\n")
        export_file.write(str(r.count_by_genre(file_name, genre)) + "\n")
        export_file.write(
            str(r.get_line_number_by_title(file_name, title)) + "\n")


exporting_results(file_name)
