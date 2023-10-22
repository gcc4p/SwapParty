#TODO
#when people subscribe, add them to the peopledict along with their quiz answers
#excel sheet

peopledict = {}


#key = person, value = list of answers
#[key] is stored as
#[box_size (0), clothes(1), [up to three keywords] (2), cm or inches (3), [chest, waist, hip, height] (4)]
#[box_size (0), accessories (1), color scheme (2), [up to three keywords] (3)]
#[box_size (0), shoes(1), type (2), sex (3), size (4)]

def clothes_match(person1, person2):
    match_counter = 0
    for i in range(len(peopledict.get(person1)[2]) - 1): # iterating through each keyword
        for j in range(len(peopledict.get(person2)[2]) - 1):
            if peopledict.get(person1)[2][i] == peopledict.get(person2)[2][j]:
                match_counter += 1
    # since it'll be counting everything twice because the options are symmetric, i.e. (a,b) E S => (b,a) E S


    #matching measurements
    sizematch_counter = 0 #number of measurements that match
    for i in range(3):
        error_cwh = 1.0
        if (abs((peopledict.get(person1)[3][i]) - (peopledict.get(person2))[3][i])) > error_cwh:
            match_counter = 0
            return match_counter
    error_height = 4.0
    if (abs(peopledict.get(person1)[3][3] - peopledict.get(person2)[3][3])) > error_height:
        match_counter = 0
        return match_counter
    match_counter += 1

    return match_counter


def accessories_match(person1, person2):
    match_counter = 0
    for i in range(len(peopledict.get(person1)[3]) - 1):
        for j in range(len(peopledict.get(person2)[3]) - 1):
            if peopledict.get(person1)[3][i] == peopledict.get(person2)[3][j]:
                match_counter += 1
    return match_counter

def shoes_match(person1, person2):
    for i in range(2, 5):
        if peopledict.get(person1)[i] != peopledict.get(person2)[i]:
            return False
    return True

def main():
    match_counter = 0
    match_list = []
    for person1 in peopledict:
        for person2 in peopledict:
            each_match = []
            if person1 == person2: #to avoid people matching with themselves
                continue

            elif peopledict.get(person1)[0] != peopledict.get(person2)[0]:
                continue

            elif ((peopledict.get(person1))[1] == (peopledict.get(person2))[1]) and ((peopledict.get(person1))[1] == "clothes"):
                match_counter = clothes_match(person1, person2)
                #match_counter /= 2
                each_match.append(person1)
                each_match.append(person2)
                each_match.append(match_counter)

            elif (peopledict.get(person1)[1] == peopledict.get(person2)[1]) and (peopledict.get(person1)[1] == "accessories"):
                if ((peopledict.get(person1)[1] == "Gold") and (peopledict.get(person2)[1] == "Silver")) or ((peopledict.get(person1)[1] == "Silver") and (peopledict.get(person2)[1] == "Gold")):
                    match_counter = 0
                elif ((peopledict.get(person1)[1] == "Other") and (peopledict.get(person2)[1] != "Other")) or ((peopledict.get(person1)[1] != "Other") and (peopledict.get(person2)[1] == "Other")):
                    match_counter = 0
                else:
                    match_counter = accessories_match(person1, person2)
                each_match.append(person1)
                each_match.append(person2)
                each_match.append(match_counter)

            elif (peopledict.get(person1)[1] == peopledict.get(person2)[1]) and (peopledict.get(person1)[1] == "shoes"):
                if shoes_match(person1, person2) == False:
                    match_counter = 0
                else:
                    return person1, person2
            if each_match  != []:
                match_list.append(each_match)

    only_match_counter = []
    for i in range(len(match_list) - 1):
        current = match_list[i][2]
        only_match_counter.append(current)

    match_index = only_match_counter.index(max(only_match_counter))

    person1 = match_list[match_index][0]
    person2 = match_list[match_index][1]

    return person1, person2



