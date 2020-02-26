def start(name):
    import logging
    from colorlog import ColoredFormatter

    formatter = ColoredFormatter(
        "%(bold_cyan)s%(asctime)-s%(reset)s%(log_color)s::%(module)s.%(name)-14s::%(levelname)-10s%(reset)s%("
        "blue)s%(message)-s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'bold_cyan',
            'INFO': 'bold_green',
            'WARNING': 'bold_yellow',
            'ERROR': 'bold_red',
            'CRITICAL': 'bold_red',
        }
    )

    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.info(f'Logger started for %s' % name)
    return logger
