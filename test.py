import trade_dao
import numpy as np

PIXEL_WIDTH = 28
PIXEL_HEIGHT = 28


def process_pixel(pixel):
    rpixel = [ele for ele in reversed(pixel)]

    for i, row in enumerate(rpixel):
        if i == len(pixel) - 1:
            break

        for j, col in enumerate(row):

            p = rpixel[i][j]
            t = rpixel[i + 1][j]

            if t == 0:
                rpixel[i][j] = 0
            else:
                rpixel[i][j] = (t - p) / p

    pixel[0] = [0] * PIXEL_WIDTH

    return pixel


def get_as_pixel(tres):
    matrix = []
    for i, tre in enumerate(tres):
        matrix.append([getattr(tre, "data" + str(j)) for j in range(0, PIXEL_WIDTH)])

    return np.array(matrix)


def get_symbol_as_pixels(tres):
    all_pixels = np.zeros(shape=(1, PIXEL_HEIGHT, PIXEL_WIDTH))
    all_labels = []
    all_dates = []

    rtres = [ele for ele in reversed(tres)]

    for i, _ in enumerate(rtres):
        if i == 0:
            continue

        if i + PIXEL_HEIGHT + 1 < len(rtres):
            c = rtres[i].data3  # Current Day's closing rate
            n = rtres[i - 1].data3  # Next Day's closing rate

            all_labels.append("B" if n > c else "S")

            pixel = get_as_pixel(rtres[i : i + PIXEL_HEIGHT])

            all_pixels = np.append(all_pixels, [process_pixel(pixel)], axis=0)

            all_dates.append(rtres[i].date)

    return np.delete(all_pixels, 0, axis=0), all_labels, all_dates


# [i.date for i in trade_dao.get_records("IBM")]

pixels, labels, dates = get_symbol_as_pixels(trade_dao.get_records("IBM"))

print(dates, labels)
