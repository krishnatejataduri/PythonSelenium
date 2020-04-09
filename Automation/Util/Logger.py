import logging
class Logger():

    def __init__(self):
        logging.basicConfig(filename='Logs.txt',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
        self.custom_logger = logging