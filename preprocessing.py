# My technique to get the columns number of a title i want.
def text_to_int(text):
    text_all_keepable = ["gameid", "url", "league", "split", "date", "week", "game", "patchno", "playerid", "side",
                         "position", "player", "team", "champion", "ban1", "ban2", "ban3", "ban4", "ban5", "gamelength",
                         "result", "k", "d", "a", "teamkills", "teamdeaths", "doubles", "triples", "quadras", "pentas",
                         "fb", "fbassist", "fbvictim", "fbtime", "kpm", "okpm", "ckpm", "fd", "fdtime", "teamdragkills",
                         "oppdragkills", "elementals", "oppelementals", "firedrakes", "waterdrakes", "earthdrakes",
                         "airdrakes", "elders", "oppelders", "herald", "heraldtime", "ft", "fttime", "firstmidouter",
                         "firsttothreetowers", "teamtowerkills", "opptowerkills", "fbaron", "fbarontime",
                         "teambaronkills", "oppbaronkills", "dmgtochamps", "dmgtochampsperminute", "dmgshare",
                         "earnedgoldshare", "wards", "wpm", "wardshare", "wardkills", "wcpm", "visionwards",
                         "visionwardbuys", "visiblewardclearrate", "invisiblewardclearrate", "totalgold", "earnedgpm",
                         "goldspent", "gspd", "minionkills", "monsterkills", "monsterkillsownjungle",
                         "monsterkillsenemyjungle", "cspm", "goldat10", "oppgoldat10", "gdat10", "goldat15",
                         "oppgoldat15", "gdat15", "xpat10", "oppxpat10", "xpdat10", "csat10", "oppcsat10", "csdat10",
                         "csat15", "oppcsat15", "csdat15"]
    return text_all_keepable.index(text)


# Used in keep function. Should not be called outside of it.
def text_to_int_to_keep(list_to_keep):
    int_list_to_keep = []
    for elem in list_to_keep:
        int_list_to_keep.append(text_to_int(elem))
    return int_list_to_keep


# give a dataset with all columns and keep only the columns we want listed in list_to_keep
# e.g. keep(dataset, ["gameid", "result"]
def keep(dataset, list_to_keep):
    list_to_keep = text_to_int_to_keep(list_to_keep)
    new_dataset = []
    for row in dataset:
        new_row = []
        for to_keep in list_to_keep:
            new_row.append(row[to_keep])
        new_dataset.append(new_row)
    return new_dataset


# Filter dataset with a key/column and a value.
# e.g. filter_containing(dataset, ["player"], ["Jankos"]) will return rows about Jankos
def filter_containing(dataset, key_list, value_list):
    new_dataset = []
    for row in dataset:
        done = False
        for key, value in zip(key_list, value_list):
            if row[text_to_int(key)] == value and done is False:
                new_dataset.append(row)
                done = True
    return new_dataset


# Filter dataset with a key/column and a value.
# e.g. filter_excluding(dataset, ["player"], ["Jankos"]) will return all the rows not about Jankos
def filter_excluding(dataset, key_list, value_list):
    new_dataset = []
    for row in dataset:
        done = False
        for key, value in zip(key_list, value_list):
            if row[text_to_int(key)] != value and done is False:
                new_dataset.append(row)
                done = True
    return new_dataset
