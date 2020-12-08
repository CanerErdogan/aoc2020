import re

with open('day04.txt') as fp:
    batch = fp.readlines()
    regex = re.compile(r"(?P<field>\w+):(?P<value>\S+)")
    passlist = []
    newpass = dict()
    for line in batch:
        if line != '\n':
            for entry in line.strip('\n').split(' '):
                newpass[regex.match(entry).group('field')] \
                    = regex.match(entry).group('value')
        else:
            passlist.append(newpass)
            newpass = dict()


def cid_optional(passlist):
    valid = []
    for passport in passlist:
        fields = passport.keys()
        if len(fields) > 7 or (len(fields) == 7 and 'cid' not in fields):
            valid.append(passport)
    return valid


print("Part 1 solution:", len(cid_optional(passlist)))


def validation(passlist):
    re_hgt = re.compile(r"(?P<amount>\d+)(?P<unit>\w+)")
    re_hcl = re.compile(r"#[a-f0-9]{6}")
    re_pid = re.compile(r"[0-9]{9}")
    ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    hgt_limits = {
        'cm': [150, 193],
        'in': [59, 76]
    }

    valid = []
    for passport in passlist:
        byr = int(passport['byr'])
        if byr < 1920 or byr > 2002:
            continue

        iyr = int(passport['iyr'])
        if iyr < 2010 or iyr > 2020:
            continue

        eyr = int(passport['eyr'])
        if eyr < 2020 or eyr > 2030:
            continue

        hgt_match = re_hgt.match(passport['hgt'])
        amount, unit = int(hgt_match.group('amount')), hgt_match.group('unit')
        if unit == 'cm' or unit == 'in':
            if amount < hgt_limits[unit][0] or amount > hgt_limits[unit][1]:
                continue
        else:
            continue

        if not re_hcl.match(passport['hcl']):
            continue

        if passport['ecl'] not in ecl_list:
            continue

        if (not re_pid.match(passport['pid'])) or len(passport['pid']) != 9:
            continue

        valid.append(passport)

    return valid


print("Part 2 solution:", len(validation(cid_optional(passlist))))
