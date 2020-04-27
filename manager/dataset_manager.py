import trade_dao as dao
import numpy as np

PIXEL_WIDTH = 30
PIXEL_HEIGHT = 30


def process_pixel(pixel):

    for i, row in enumerate(pixel):
        if i == len(pixel) - 1:
            pixel[i] = [0] * PIXEL_WIDTH
            break

        for j, col in enumerate(row):

            c = pixel[i][j]  # Current Day's value
            p = pixel[i + 1][j]  # Previous Day's value

            if p == 0:
                pixel[i][j] = 0
            else:
                pixel[i][j] = (c - p) / p

    return [ele for ele in reversed(pixel)]


def get_as_pixel(tres):
    matrix = []
    for i, tre in enumerate(tres):
        matrix.append([tre.get("data" + str(j), 0.0) for j in range(0, PIXEL_WIDTH)])

    return np.array(matrix)


def get_symbol_as_pixels(tres):
    all_pixels = np.zeros(shape=(1, PIXEL_HEIGHT, PIXEL_WIDTH))
    all_labels = []
    all_dates = []

    for i, _ in enumerate(tres):
        if i == 0:
            continue

        if i + PIXEL_HEIGHT <= len(tres):
            c = tres[i].get("data3", 0.0)  # Current Day's closing rate
            n = tres[i - 1].get("data3", 0.0)  # Next Day's closing rate

            all_labels.append(1 if n > c else 0)

            pixel = get_as_pixel(tres[i : i + PIXEL_HEIGHT])

            all_pixels = np.append(all_pixels, [process_pixel(pixel)], axis=0)

            all_dates.append(tres[i]["date"])

    return np.delete(all_pixels, 0, axis=0), all_labels, all_dates


def get_dataset():
    all_symbols = np.zeros(shape=(1, PIXEL_HEIGHT, PIXEL_WIDTH))
    all_labels = []
    all_dates = []

    for symbol in dao.get_symbols_list():
        pixel, labels, dates = get_symbol_as_pixels(dao.get_records(symbol))

        all_symbols = np.append(all_symbols, pixel, axis=0)
        all_labels.extend(labels)
        all_dates.extend(dates)

    return (
        np.flip(np.delete(all_symbols, 0, axis=0), axis=0),
        np.flip(np.asarray(all_labels)),
        all_dates[::-1],
    )


def get_symbol_data_for_today(symbol):
    db_data = dao.get_records(symbol, PIXEL_HEIGHT)
    symbol_data = np.zeros(shape=(1, PIXEL_HEIGHT, PIXEL_WIDTH))

    symbol_data = np.append(
        symbol_data, [process_pixel(get_as_pixel(db_data))], axis=0,
    )

    return np.delete(symbol_data, 0, axis=0), db_data[0].get("date")


# np.set_printoptions(precision=5, suppress=True)

# [i.data1 for i in trade_dao.get_records("IBM")]
# _, ibm, _ = get_symbol_as_pixels(dao.get_records("IBM"))
# _, msft, _ = get_symbol_as_pixels(dao.get_records("MSFT"))

# all_labels = []

# all_labels.extend(ibm)
# all_labels.extend(msft)

# len(all_labels)


# for d, l, p in zip(dates, labels, pixels):
# print(d, l, p)

# symbols, labels, dates = get_dataset()

# symbols[0]
# dates

# get_as_pixel(dao.get_records("A", 30))

# get_symbol_data_for_today("A")

# dao.get_records("A", 30)
