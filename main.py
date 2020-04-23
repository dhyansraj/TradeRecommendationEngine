import trade_dao
import tre_db_manager

trade_dao.create_table()

tre_db_manager.save_daily_rates_of_all_symbols()
