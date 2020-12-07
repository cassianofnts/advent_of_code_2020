def transform_list(input):
    passport_list = []
    new_line = '' 

    for line in input:
        if line != '':
            new_line += f'{line} '                        
        else:
            passport_list.append(new_line.rstrip())
            new_line = ''

    passport_list.append(new_line.rstrip())
    
    return passport_list

def create_dict_entry(passport):
    fields = passport.split(' ')
    passport_dict = {}

    for field in fields:
        dict_entry = {field.split(':')[0] : field.split(':')[1] }
        passport_dict.update(dict_entry)
    
    return passport_dict

def check_if_valid(passport):
    required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

    for field in required_fields:
        if field not in passport:
            return False

    return True

def check_fields(passport):
    if (1920 <= int(passport['byr']) <= 2002) \
                    and (2010 <= int(passport['iyr']) <= 2020) \
                    and (2020 <= int(passport['eyr']) <= 2030) \
                    and ((passport['hgt'][-2:] == 'cm' and (150 <= int(passport['hgt'][:-2]) <= 193))\
                         or (passport['hgt'][-2:] == 'in' and (59 <= int(passport['hgt'][:-2]) <= 76))) \
                    and passport['hcl'][0] == '#' and len(passport['hcl']) == 7 and int(passport['hcl'][1:], 16)+1 \
                    and passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'} \
                    and (len(passport['pid']) == 9 and passport['pid'].isnumeric()):
    
        return 1
    else:
        return 0

def main():
    valid_passports = []
    password_with_valid_fields = 0

    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    passport_list = transform_list(data)

    for passport in passport_list:
        if check_if_valid(passport):
            valid_passports.append(passport)
    
    for passport in valid_passports:
        passport_dict = create_dict_entry(passport)
        password_with_valid_fields += check_fields(passport_dict)

    print(f'\n\nValid passports:')
    print(f'\tWithout Field Verification: {len(valid_passports)}')
    print(f'\tWith Field Verification: {password_with_valid_fields}\n\n')

if __name__ == "__main__":
    main()