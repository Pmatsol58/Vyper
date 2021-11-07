Import("env")

from datetime import datetime

env['PROGNAME'] = datetime.now().strftime("main_board_%Y%m%d-%H%M%S")
