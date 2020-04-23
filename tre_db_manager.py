import daily_rates_manager
import trade_dao


def save_daily_rates_of_all_symbols():
    hrts = daily_rates_manager.get_all_symbols_as_hrt()

    for hrt in hrts:
        trade_dao.create_record(hrt)
