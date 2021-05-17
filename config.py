"""Конфигурация программного обеспечения."""
from logging.handlers import RotatingFileHandler
import configparser
import logging

CONFIG_FILE = 'config.ini'
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

logging.basicConfig(
    handlers=[RotatingFileHandler(config.get("LOGGER", "LOGFILE"), maxBytes=10000000, backupCount=100)],
    # level=logging.CRITICAL,
    level=logging.INFO,
    format='[%(asctime)s]  [%(name)s]  [%(levelname)s]  [%(funcName)s]  [%(pathname)s]  [%(message)s]',
    datefmt='%d/%m/%Y %H:%M:%S %z')


class AccountSMTP:
    SERVER = config.get('SMTP', 'SERVER')
    USER = config.get('SMTP', 'USER')
    PASSWORD = config.get('SMTP', 'PASSWORD')
    SENDER = config.get('SMTP', 'SENDER')