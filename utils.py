import logging
import logging.config
import yaml
import ast
import requests


def get_proxis(filename):
    # yaml.safe_load()
    result = []
    line = True
    with open(filename) as f:
        # for p in f:
        #     print(f.readline())
        while line:
            line = f.readline()
            if line:
                host, port = line.split(':')
                result.append([host, int(port)])
                # result[host] = int(port)
    # print(result)
    return result


class ProxyError(Exception):
    pass


# def log2log():
#     logger = logging.getLogger(__name__)
#
#     handler_comman = logging.StreamHandler()
#     handler_file = logging.FileHandler(filename="t1.log")
#
#     logger.setLevel(logging.DEBUG)
#     handler_comman.setLevel(logging.WARNING)
#     handler_file.setLevel(logging.DEBUG)
#
#     formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
#     handler_comman.setFormatter(formatter)
#     handler_file.setFormatter(formatter)
#
#     logger.addHandler(handler_comman)
#     logger.addHandler(handler_file)
#     logger.error(f'application.outbound_ip is')


def log_config():
    with open('config/config.yml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    logger = logging.getLogger("proxyLogger")
    # print(logger)
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')


# def log_test():
#     logging.basicConfig()
#     logging.debug('This is a debug message')
#     logging.info('This is an info message')
#     logging.warning('This is a warning message')
#     logging.error('This is an error message')
#     logging.critical('This is a critical message')

def get_proxies_online():
    res = requests.get('http://118.24.52.95:5010/get_all/')
    proxies_list = ast.literal_eval(res.text)
    res = []
    for proxy in proxies_list:
        host, port = proxy.split(':')
        res.append([host,int(port)])
    return res


if __name__ == '__main__':
    print(get_proxis('config/proxis.txt'))
    # log2log()
    # log_test()
    # pass
    # log_config()
    print(get_proxies_online())
