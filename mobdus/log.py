#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
# вся информация о работе сервиса находится в README.txt
# и размещена в репозитории

from twisted.logger import Logger

logging = Logger()


def init_log(name, config="/etc/kiosk/log.yaml", extra_handlers=[]):
    """
    Ф-я инициализации логирования для службы
    """
    import os
    import yaml
    import logging.config
    from twisted.logger import globalLogBeginner
    from twisted.logger import STDLibLogObserver

    # создаем переменную которая покажет имя запускаемого сервиса
    name = os.path.dirname(os.path.abspath(name)).split('/')[-1]

    logging.info("Запускается - %s " % name)
    try:
        f = open(config, "r")
        d = yaml.load(f)
        dct = dict(version=d['version'], formatters=d['formatters'], handlers={}, loggers={})
        hds = [name] + extra_handlers
        for h in hds:
            ds = d['loggers'][h]
            dct['loggers'][h] = ds
            for x in ds['handlers']:
                dct['handlers'][x] = d['handlers'][x]
                logging.info('Логирование выводится в - %s' % x)
        logging.config.dictConfig(dct)
        f.close()
    except:
        logging.error("Не смогли открыть - %s" % config)
    observers = [STDLibLogObserver(name)]
    globalLogBeginner.beginLoggingTo(observers)
