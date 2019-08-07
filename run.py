from tproxy import proxy
from utils import get_proxis,get_proxies_online

if __name__ == '__main__':
    try:
        # proxy = proxy.ProxyServer(proxy.ProxyHandler, proxies=get_proxis('config/proxis.txt'))
        proxy = proxy.ProxyServer(proxy.ProxyHandler, proxies=get_proxies_online())
        proxy.start()
    except KeyboardInterrupt:
        proxy.stop()
