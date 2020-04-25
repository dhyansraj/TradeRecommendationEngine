import manager.indicator.daily_rates_manager as daily_rates_manager
import manager.indicator.sma_manager as sma_manager
import manager.indicator.ema_manager as ema_manager
import manager.indicator.macd_manager as macd_manager
import manager.indicator.stoch_manager as stoch_manager
import manager.indicator.rsi_manager as rsi_manager
import manager.indicator.adx_manager as adx_manager
import manager.indicator.cci_manager as cci_manager
import manager.indicator.aroon_manager as aroon_manager
import manager.indicator.bbands_manager as bbands_manager
import manager.indicator.obv_manager as obv_manager

import sys
import time


def store_all_symbols_on_disk():
    daily_rates_manager.store_all_symbols_on_disk()
    adx_manager.store_all_symbols_on_disk()
    aroon_manager.store_all_symbols_on_disk()
    bbands_manager.store_all_symbols_on_disk()
    cci_manager.store_all_symbols_on_disk()
    sma_manager.store_all_symbols_on_disk()
    ema_manager.store_all_symbols_on_disk()
    macd_manager.store_all_symbols_on_disk()
    stoch_manager.store_all_symbols_on_disk()
    obv_manager.store_all_symbols_on_disk()
    rsi_manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():

    print("daily_rates_manager.store_all_symbols_on_db()")
    daily_rates_manager.store_all_symbols_on_db()

    print("adx_manager.store_all_symbols_on_db()")
    adx_manager.store_all_symbols_on_db()
    print("aroon_manager.store_all_symbols_on_db()")
    aroon_manager.store_all_symbols_on_db()
    print("bbands_manager.store_all_symbols_on_db()")
    bbands_manager.store_all_symbols_on_db()
    print("cci_manager.store_all_symbols_on_db()")
    cci_manager.store_all_symbols_on_db()
    print("sma_manager.store_all_symbols_on_db()")
    sma_manager.store_all_symbols_on_db()
    print("stoch_manager.store_all_symbols_on_db()")
    stoch_manager.store_all_symbols_on_db()
    print("ema_manager.store_all_symbols_on_db()")
    ema_manager.store_all_symbols_on_db()
    print("macd_manager.store_all_symbols_on_db()")
    macd_manager.store_all_symbols_on_db()
    print("obv_manager.store_all_symbols_on_db()")
    obv_manager.store_all_symbols_on_db()
    print("rsi_manager.store_all_symbols_on_db()")
    rsi_manager.store_all_symbols_on_db()


def main():

    if len(sys.argv) < 2:
        indicator = 1
    else:
        indicator = int(sys.argv[1])

    if indicator == 1:
        daily_rates_manager.store_all_symbols_on_disk()

    if indicator == 2:
        adx_manager.store_all_symbols_on_disk()

    if indicator == 3:
        aroon_manager.store_all_symbols_on_disk()

    if indicator == 4:
        bbands_manager.store_all_symbols_on_disk()

    if indicator == 5:
        cci_manager.store_all_symbols_on_disk()

    if indicator == 6:
        sma_manager.store_all_symbols_on_disk()

    if indicator == 7:
        ema_manager.store_all_symbols_on_disk()

    if indicator == 8:
        macd_manager.store_all_symbols_on_disk()

    if indicator == 9:
        stoch_manager.store_all_symbols_on_disk()

    if indicator == 10:
        obv_manager.store_all_symbols_on_disk()

    if indicator == 11:
        rsi_manager.store_all_symbols_on_disk()


if __name__ == "__main__":

    from datetime import datetime

    start = datetime.now()

    # main()

    store_all_symbols_on_db()

    end = datetime.now()

    delta = end - start

    print(delta)
