import pandas as pd

class DfBuilder:

    t_colunas = ['UF', 
            'Referência', 
            'Famílias PBF (até Out/2021)',
            'Famílias PBF (a partir de Mar/2023)', 
            'Valor repassado às famílias PBF (até Out/2021)', 
            'Valor repassado às famílias PBF (a partir de Mar/2023)', 
            'Valor do Benefício médio (até Out/2021)', 
            'Valor do Benefício médio (a partir de Mar/2023)',
            'Municipio']
    
    def __init__(self, data: list):
        self.data = data

    def gen_csv(self) -> None:
        df = pd.DataFrame(self.data, columns=self.t_colunas)
        df.to_csv('output_visdata.csv', index=False)
        print("output_visdata.csv foi gerado com sucesso!")