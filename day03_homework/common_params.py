#  加油卡的请求参数


def get_params():
    data = {"dataSourceId": "endq", "methodId": "00A", "CardInfo": {
        "cardNumber": "081211"
    }}
    url = "http://115.28.108.130:8080/gasStation/process"
    return data, url


def get_binding_params():
    data = {"dataSourceId": "endq","methodId": "01A", "CardUser": {
        "userName": "SMF",
        "idType": "1",
        "idNumber": "0306"
    },
            "CardInfo": {
                "CardNumber": "0922"
            }
        }
    url = "http://115.28.108.130:8080/gasStation/process"
    return data, url

