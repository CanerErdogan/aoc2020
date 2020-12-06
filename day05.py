with open('day05.txt') as fp:
    boarding_passes = list(map(str.strip, fp.readlines()))


def seat_ids(boarding_passes):
    ids = []
    for boarding_pass in boarding_passes:
        rows = list(range(128))
        for zone in boarding_pass[:-3]:
            rows = rows[:len(rows)//2] if zone == 'F' else rows[len(rows)//2:]

        cols = list(range(8))
        for zone in boarding_pass[-3:]:
            cols = cols[:len(cols)//2] if zone == 'L' else cols[len(cols)//2:]

        seat_id = rows[0] * 8 + cols[0]
        ids.append(seat_id)

    return ids


def find_seat(ids):
    possible_seats = set(range(min(ids) + 1, max(ids)))
    full_seats = set(sorted(ids)[1:-1])
    return next(iter(possible_seats.difference(full_seats)))


ids = seat_ids(boarding_passes)
print("Max seat ID:", max(ids))
print("Your seat ID:", find_seat(ids))
