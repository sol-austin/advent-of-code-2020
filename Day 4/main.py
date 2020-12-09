f = open('text.txt', 'r')

arr = [i.replace('\n',' ').split(' ') for i in f.read().split('\n\n')]

arr_dict = [{x.split(':')[0] : x.split(':')[1] for x in i} for i in arr]

must_contain = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
count = 0

def check_item(passport, must_contain):
    for item in must_contain:
        if item not in passport.keys():
            return 0

    # Validation (part 2)
    if (len(passport['byr']) != 4) or (int(passport['byr']) < 1920) or (int(passport['byr']) > 2002):
        return 0

    if (len(passport['iyr']) != 4) or (int(passport['iyr']) < 2010) or (int(passport['iyr']) > 2020):
        return 0

    if (len(passport['eyr']) != 4) or (int(passport['eyr']) < 2020) or (int(passport['eyr']) > 2030):
        return 0

    if (passport['hgt'][-2:] != 'in') and (passport['hgt'][-2:] != 'cm'):
        # Height ends in cm or in
        return 0
    else:
        height_int = int(passport['hgt'][:-2])
        if passport['hgt'][-2:] == 'in':
            if (height_int < 59) or (height_int > 76):
                return 0
        else:
            if (height_int < 150) or (height_int > 193):
                return 0

    if (passport['hcl'][0] != '#'):
        return 0
    else:
        if (len(passport['hcl'][1:]) == 6):
            allowed_chars = '0123456789abcdef'
            for char in passport['hcl'][1:]:
                if char not in allowed_chars:
                    return 0
        else:
            return 0

    allowed_eyes = ['amb','blu','brn','gry','grn','hzl','oth']
    if passport['ecl'] not in allowed_eyes:
        return 0

    if len(passport['pid']) != 9:
        return 0
    return 1

for passport in arr_dict:
    count_inc = check_item(passport, must_contain)
    count += count_inc
print(count)
