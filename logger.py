import logging
# logging.disagle  # отключение протоколирования

logging.basicConfig(filename='S8_tel_logger.txt', encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')