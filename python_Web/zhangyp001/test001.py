
# 引入suds库
from suds.client import Client


# 创建一个webservice对象，来调用webservice里面的各类接口
user_url = "http://172.25.2.106:52087/fpt-dsqz/services/DZFPService?wsdl"


def res_dsqz_webservice(url, data):
    client = Client(url)
    result = client.service.doService(data)
    return result
