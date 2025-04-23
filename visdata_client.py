import requests
from datetime import datetime
import re

class VisdataClient:

    def __init__(self, cod_municipio: int, municipio: str):
        self.cod_municipio = cod_municipio
        self.municipio = municipio

    def __gen_url(self, cod_municipio: int) -> tuple:
        url = f'https://aplicacoes.cidadania.gov.br/vis/data3/v.php?q[]=r6JtZJCug7BtxKW25rV%2FfmdhhJFkl21kmK19ZnF1ZW2maX7KmZO20qfOnJm%2B6IianbSon7SfrrqqkpKcmcuppsK2iKextVi1mpyuwZxNzsmY2F1zyuDAk522pHa2YH9%2BaV6EkmOXbWSEm8GcobZVetufrL%2BrkbbHlNddmMnuslSqvaGmmZ67sliqkseU1rCYmOGuoK%2BtcHXfmrnBnGiS1KjXYK5%2B3q6noWisot6nbY6kksrAlNiscZqif2Rue2JqrGZ9f15Ny8mY2F1zv%2BGspbCslKDapm2zo6C8gaHfqZ994LuYXcVwoNqlwLNyk7jNps94bsPcuaehg3Ct7qZwyViQuNSYirSbwultdKmtqJnap7yKdFSJkWWbamSNqH1lY2ipot6nbY6Zk7bXn4qin9DgbaKxtKFa3qexb7RovcKf3aJuw9y5p6GDcKDapcCzcmjK1qCNuFTA3MCZXL%2Bdn%2BdZjbucoLbCodl7cIStfWZvdWVtpml%2BdVehv8ahin2Vw9rDoFytoa3eWbvDo5l3xqHOXrCY4a6gr61woNqlwLNyaL3Cn92ibpjuwqFfw1ad2qyybq6VvM9TqqqY0NquoquEcmGraX9%2FZF6HjmObZFPR47KiXHCYm%2ByebcWfksWBc8yjks7vsZOiqaJ4qVnBtpybd9Oi36uXhbuvmpu%2BoXSzp8K7nJ%2FAxGKqn5m87MGYm66Wp6Vrdm6cmcrGU9iyn8mbsqKgcVWf5ayybqWiw81Tz6uXfviImp20qJ%2B0n666qpKSnJnLqabCtoinsbVYtZqcrsGcTc7JmNhdc8rgwJOdtqR4tmB%2FfmlghJFml21khJvBnKG2VWLcmsCzV6S%2FxqGKfamPsYFnenhVruGeu26pnMzPl5J9lcPaw6B2gqOv5p6%2Ft5pcl9dloHFmia12VKG0qJ%2BZp8K6o028z5eTXZjJ7rJUqr2hppmeu7JYqpLHlNawmJjhrqCvrXB135q5wZxoktSo17l5vugQ4aixlq2Ze7K8nJPAxJwt3qXG3MBXgqmi%2FSaltq%2BqTaejeYpllNE%2B9lSLvalpq2l%2Ff2BQncKgLeqfxtzAVIyKe1qhmm2%2BmJ%2FLyqWKoZh9yK6ma3plbKxicKSYmcbTU9yio77uwJWgt1X9GaxttJiaGg6f056mfcuPelxwlq484m2drKGGk2OcblyA0a6gq7pVrN6prsGqjrvQUy3dpn3hrqH%2F9aGj2qxtnnlzd4mUiq2Uz%2B%2B2plysmlrGmr99aV2JlFyNk5TJ6r9UoLdVfN6nsrT62rrKooqq9gbftqNccJauPOJtnayhhpNjnG5cgNGuoKu6VZ7oWY%2BzpZK9JODNpqJ96BDdoLGkWqGabb6Yn8vKpYqhmH3IrqZremVsrGLJvnKp091lmm1miqt%2BYWx5iWqpc31%2BcV2Hu24%3D&ag=m&codigo={cod_municipio}&dt1=2005-01-01&dt2=2025-03-01&wt=json&tp_funcao_consulta=0&rqprocess=c23890d77ced516dc54292bc061c9aa8'

        data_post = "draw=2&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=sigla&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=mes_ano_formatado&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=(case+when+t.mes_ano%3C%3D'2021-10-01'+then+t.bf_qtd_fam+else+null+&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=(case+when+t.mes_ano%3E%3D'2023-03-01'+then+t.bf_qtd_fam+else+null+&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=(case+when+t.mes_ano%3C%3D'2021-10-01'+then+t.bf_vl+else+null+end)&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=(case+when+t.mes_ano%3E%3D'2023-03-01'+then+t.bf_vl+else+null+end)&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=(case+when+t.mes_ano%3C%3D'2021-10-01'+then+(case+when+t.bf_qtd_fam&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=7&columns%5B7%5D%5Bname%5D=(case+when+t.mes_ano%3E%3D'2023-03-01'+then+(case+when+t.v2643%3E0+th&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=0&length=50&search%5Bvalue%5D=&search%5Bregex%5D=false"
        return url, data_post

    def __get_data(self) -> list:
        url, data_post = self.__gen_url(self.cod_municipio)
        visdata_csv = requests.post(url, data=data_post)
        return visdata_csv.json()['data']
    
    def __format_data(self, tabela: list) -> list:
        for i, linha in enumerate(tabela):
            linha_tmp = list(map(self.__remove_chars, linha))
            linha_tmp.append(self.municipio)
            tabela[i] = linha_tmp
        return tabela
    
    def __remove_chars(self, value):
        if (value == '-') or (value == 'R$ -'):
            return None
        elif ('R$' in value):
            value = value.replace('R$', '')
            value = value.replace('.', '')
            value = value.replace(',', '.')
            return float(value)
        elif ('.' in value):
            value = value.replace('.', '')
            return int(value)
        elif re.match(r'\d{2}/\d{4}', value):  # detecta padrão tipo "01/2005"
            return self.__format_date(value)
        return value.strip()
    
    def __format_date(self, value: str) -> str:
        try:
            dt = datetime.strptime(value, "%m/%Y")
            return dt.strftime("%Y-%m-%d")
        except:
            return value

    def return_data(self) -> list:
        tabela = self.__get_data()
        return self.__format_data(tabela)
    
