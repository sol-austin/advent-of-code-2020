f = open('text.txt', 'r')

dict = { i.split(' contain ')[0] : i.split(' contain ')[1].replace('.','').split(',') for i in f.read().split('\n') }

def searchForValueInKeyArrs(toSearch, dict):
    new_arr = []
    for key in dict:
        value_arr = dict[key]
        for value in value_arr:
            if toSearch in value:
                new_bag = key.replace(' bag','').replace(' bags', '').rstrip('s')
                new_arr.append(new_bag)
    return new_arr

def loopArrs(new_arr):
    orig_len = len(new_arr)
    for item in new_arr:
        returned_arr = searchForValueInKeyArrs(item, dict)
        for item in returned_arr:
            if item not in new_arr:
                new_arr.append(item)
    fin_len = len(new_arr)
    if fin_len > orig_len:
        finished = False
    else:
        finished = True
    return new_arr, finished

# DO NOT FORGET TO SUBTRACT 1
save_outer_arr, finished = loopArrs(['shiny gold'])
save_outer_arr, finished = loopArrs(save_outer_arr)
print(len(save_outer_arr)-1)