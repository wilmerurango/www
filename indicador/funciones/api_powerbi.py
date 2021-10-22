import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random

##class for data_generation
class datos():
    def data_generation():
        FACTURACION = random.randint(230000000, 890000000)
        RECAUDO = random.randint(100000000, 600000000)
        COSTOS =random.randint(25000000, 75600000)
        GASTOS = random.randint(20000000, 90000000)
        INGRESOS = random.randint(1000000000, 7000000000)
        NOMINA = random.randint(1000000, 7000000)
        COSTO_MEDICAMENTOS = random.randint(10000000, 70000000)
        FECHA = datetime.today().strftime("%Y-%m-%d")
        Facturacion = random.randint(1, 3)
        Recaudo = random.randint(1, 3)
        Costos = random.randint(1, 3)
        # surr_id = random.randint(1, 3)
        # speed = random.randint(20,200)
        # date = datetime.today().strftime("%Y-%m-%d")
        # time = datetime.now().isoformat()

        return [FACTURACION,
                RECAUDO,
                COSTOS,
                GASTOS,
                INGRESOS,
                NOMINA,
                COSTO_MEDICAMENTOS,
                FECHA
                ]


    if __name__ == '__main__':

        REST_API_URL = 'https://api.powerbi.com/beta/a944c466-734b-4bd4-8cd8-c77d529a3150/datasets/a61197ae-f34a-454f-9c35-dc30e8c515d3/rows?redirectedFromSignup=1&key=bRPsa8kIiVBgdFCrhc8Bn1fZZf2o65H0oWv0AbvFOhYkvevcRWT67yvPcxJmaABDYHuuE9YJzgDGTLuFvZxOmQ%3D%3D'
        # 'https://api.powerbi.com/beta/e81af6ba-a66f-4cab-90f9-9225862c5cf8/datasets/51a56115-ac32-437a-8f2c-3ed1fa1dc37a/rows?key=24THP%2FqLUg2EWnDtFiTUr8GTjjPOU%2FxjT%2BnkTt9%2FHMlkMG%2B5BhWe0pYVfsJcE8gVNitZ3C2Fp1akv3LR7hLVNQ%3D%3D'

        while True:
            data_raw = []
            for i in range(1):
                row = data_generation()
                data_raw.append(row)
                print("Raw data - ", data_raw)

            # set the header record
            HEADER = ["FACTURACION", "RECAUDO", "COSTOS","GASTOS", "INGRESOS", "NOMINA", "COSTO_MEDICAMENTOS", "FECHA"]

            data_df = pd.DataFrame(data_raw, columns=HEADER)
            data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
            print("JSON dataset", data_json)

            # Post the data on the Power BI API
            req = requests.post(REST_API_URL, data_json)

            print("Data posted in Power BI API")
            time.sleep(2)

