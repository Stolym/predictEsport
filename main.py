import preprocessing as preprocess


def extract_dataset(path):
    f = open(path, "r")
    fl = f.readlines()
    dataset = []
    for line in fl:
        line = line.split(';')
        dataset.append(line)
    f.close()
    return dataset


def dico_player(dataset):
    player_list = []
    dataset = preprocess.filter_excluding(dataset, ["player"], ["Team"])
    col_player = preprocess.text_to_int("player")
    while len(dataset) != 1:
        print(len(dataset))
        if dataset[1][col_player] not in player_list:
            player_list.append(dataset[1][col_player])
            dataset = preprocess.filter_excluding(dataset, ["player"], [dataset[1][col_player]])
    print(player_list)


def dico_team(dataset):
    team_list = []
    col_player = preprocess.text_to_int("team")
    while len(dataset) > 1:
        print(len(dataset))
        if dataset[1][col_player] not in team_list:
            team_list.append(dataset[1][col_player])
            dataset = preprocess.filter_excluding(dataset, ["team"], [dataset[1][col_player]])
    print(team_list)


def first_try(dataset):
    text_vector = []
    game = []
    win_vector = []
    gameid_list = []
    gameid_col = preprocess.text_to_int("gameid")
    for row in dataset:
        if row[gameid_col] not in gameid_list:
            if len(game) > 0:
                text_vector.append(game)
                game = []
            gameid_list.append(row[gameid_col])
            #print(row[gameid_col])
            game.append(row[preprocess.text_to_int("team")])
            game.append(row[preprocess.text_to_int("player")])
            win_vector.append(row[preprocess.text_to_int("result")])
        else:
            if row[preprocess.text_to_int("player")] != "team" and row[preprocess.text_to_int("player")] != "team":
                game.append(row[preprocess.text_to_int("team")])
                game.append(row[preprocess.text_to_int("player")])
    return text_vector, win_vector


#def tests(dataset):
    #id = first_try(dataset)
    #dico_team(dataset)
    #print(len(dataset))
    #dataset_0 = preprocess.filter_containing(dataset, ["gameid"], [str(id)])
    #dataset_0 = preprocess.filter_containing(dataset, ["team"], [""])
    #dataset_0 = preprocess.keep(dataset_0, ["team", "result", "date"])
    #print(dataset_0)
    #dataset_0 = preprocess.filter_containing(dataset_0, ["result"], ["0"])
    #dataset_0 = preprocess.keep(dataset_0, ["gameid"])
    #gameid_list = []
    #for elem in dataset_0:
    #gameid_list.append(' '.join(map(str, elem)))
    #dataset_1 = preprocess.filter_containing(dataset, ["gameid"] * len(dataset_0), gameid_list)
    #dataset_1 = preprocess.filter_excluding(dataset_1, ["team"], ["G2 Esports"])
    #dataset_1 = preprocess.filter_containing(dataset_1, ["player"], ["Team"])
    #dataset_1 = preprocess.keep(dataset_1, ["team"])
    #print(dataset_1)


def extract_all():
    #dataset = extract_dataset("src/2019-worlds.csv")
    #dataset = extract_dataset("src/2019-summer.csv")
    #dataset += extract_dataset("src/2019-spring.csv")
    dataset = extract_dataset("src/2018-worlds.csv")
    dataset += extract_dataset("src/2018-summer.csv")
    dataset += extract_dataset("src/2018-spring.csv")
    dataset += extract_dataset("src/2017-year.csv")
    #dataset += extract_dataset("src/2016-year.csv")
    #tests(dataset)
    return dataset

if __name__ == "__main__":
    extract_all()

