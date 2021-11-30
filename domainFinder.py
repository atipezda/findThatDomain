import requests
import whois


class DomainFinder:
    @staticmethod
    def domainExsit(name):

        try:
            get_info = whois.query(name)
            if not get_info:
                return False
            return bool(get_info.registrar)
        except:
            return False

    @staticmethod
    def ensureFreeDomain(name):

        url = "https://www.ovh.pl/engine/apiv6/order/cart/abc4bfe8-090c-4796-bca6-b73ec7612e96/domain"

        querystring = {"domain": name}
        response = requests.request("GET", url, data="", params=querystring)

        try:
            return response.json()[0]["action"] == "create"
        except:
            return False