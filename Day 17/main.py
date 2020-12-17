f = open('text.txt', 'r')
doc = f.read()

conditions = [i.split(':')[1].lstrip().split(' or ') for i in doc.split('\nyour ticket')[0].split('\n')[:-1]]
conditions = [item for sublist in conditions for item in sublist]
my_ticket = doc.split('\nyour ticket:\n')[1].split('\nnearby tickets')[0].split(',')
other_tickets = [i.split(',') for i in doc.split('\nnearby tickets:\n')[1].split('\n')]
invalid_count = 0
invalid_arr = []

def check_valid_value(value):
    for condition in conditions:
        lower_bound = int(condition.split('-')[0])
        upper_bound = int(condition.split('-')[1])
        if value >= lower_bound and value <= upper_bound:
            return True
    return False

for ticket in other_tickets:
    for value in ticket:
        value = int(value)
        if not check_valid_value(value):
            invalid_count += value
            if ticket not in invalid_arr:
                invalid_arr.append(ticket)

print(invalid_count)

# Part 2
for invalid_ticket in invalid_arr:
    other_tickets.remove(invalid_ticket)

conditions = {i.split(': ')[0] : i.split(': ')[1].split(' or ') for i in doc.split('\nyour ticket')[0].split('\n')[:-1]}

def check_condition_value(value, conditions_arr):
    for condition in conditions_arr:
        lower_bound = int(condition.split('-')[0])
        upper_bound = int(condition.split('-')[1])
        if lower_bound <= value <= upper_bound:
            return True
    return False

final_fields = {}

for i in range(len(other_tickets[0])):
    col = [x[i] for x in other_tickets]
    poss_conditions = list(conditions.keys())
    for value in col:
        value = int(value)
        for condition_name, conditions_arr in conditions.items():
            if not check_condition_value(value, conditions_arr):
                if condition_name in poss_conditions:
                    poss_conditions.remove(condition_name)

    final_fields[i] = poss_conditions

    if len(poss_conditions) == 1:
        del conditions[poss_conditions[0]]
    #else:
        #raise Exception('Possible conditions array is too long')

def runloop():
    for idx in range(len(final_fields.keys())):
        val = final_fields[idx]
        if len(val) == 1:
            for key in final_fields.keys():
                if val[0] in final_fields[key] and len(final_fields[key]) > 1:
                    final_fields[key].remove(val[0])
for x in range(20):
    runloop()
ans = 1
for idx, value in final_fields.items():
    value = value[0]
    if 'departure' in value:
        ans *= int(my_ticket[idx])
print(ans)