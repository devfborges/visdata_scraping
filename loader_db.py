import pandas as pd
from sqlalchemy import create_engine

class LoaderDB:

    t_colunas = ['uf',
	'referencia',
	'familias_pbf_ate_out2021',
	'familias_pbf_a_partir_mar2023',
	'valor_repas_fam_ate_out2021',
	'valor_repas_fam_a_partir_mar2023',
	'valor_benef_medio_ate_out2021',
	'valor_benef_medio_a_partir_mar2023',
	'municipio']
    
    def __init__(self, data: list):
        self.data = data

    def load_data(self) -> None:
        df = pd.DataFrame(self.data, columns=self.t_colunas)
    
        engine  = create_engine('postgresql://postgres:postgres@localhost:5432/metabase')

        df.to_sql('pbf', engine, if_exists='append', index=False, schema='visdata')
        
        print("dados inseridos com sucesso")