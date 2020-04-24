import trade_dao as dao
import numpy as np

PIXEL_WIDTH = 28
PIXEL_HEIGHT = 28


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
        matrix.append([getattr(tre, "data" + str(j)) for j in range(0, PIXEL_WIDTH)])

    return np.array(matrix)


def get_symbol_as_pixels(tres):
    all_pixels = np.zeros(shape=(1, PIXEL_HEIGHT, PIXEL_WIDTH))
    all_labels = []
    all_dates = []

    for i, _ in enumerate(tres):
        if i == 0:
            continue

        if i + PIXEL_HEIGHT + 1 < len(tres):
            c = tres[i].data3  # Current Day's closing rate
            n = tres[i - 1].data3  # Next Day's closing rate

            all_labels.append(1 if n > c else 0)

            pixel = get_as_pixel(tres[i : i + PIXEL_HEIGHT])

            all_pixels = np.append(all_pixels, [process_pixel(pixel)], axis=0)

            all_dates.append(tres[i].date)

    return np.delete(all_pixels, 0, axis=0), all_labels, all_dates


def get_dataset():
    all_symbols = np.zeros(shape=(1, PIXEL_HEIGHT, PIXEL_WIDTH))
    all_labels = []
    all_dates = []

    for symbol in dao.get_symbols_list():
        pixel, labels, dates = get_symbol_as_pixels(dao.get_records(symbol[0]))

        all_symbols = np.append(all_symbols, pixel, axis=0)
        all_labels.extend(labels)
        all_dates.extend(dates)

    return np.delete(all_symbols, 0, axis=0), np.asarray(all_labels), all_dates


# def get_dataset():
#     for symbol in dao.get_symbols_list():
#         return get_symbol_as_pixels(dao.get_records(symbol[0]))


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

# get_dataset()
