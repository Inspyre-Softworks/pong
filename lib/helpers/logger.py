def start(name, debug=False):
    """

    Start a formatted root-logger

    :type name: str
    :param debug: Boolean - If True logger will start in at debug level. This is most useful if you're trying to see
                            the internal goings-on immediately on starting the logger.

    :param name: str - The name you want to give to the root logger

    """
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
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARN)
    logger.info(f'Logger started for %s' % name)
    return logger
