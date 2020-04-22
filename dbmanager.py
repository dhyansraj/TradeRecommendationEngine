import dailyrates
import tredao


def storeDailyRates():
    hrts = dailyrates.getHrtForAllSymbols()

    for hrt in hrts:
        tredao.createRecord(hrt)
