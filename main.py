import json
from visdata_client import VisdataClient
from loader_db import LoaderDB

def main() -> None:
    with open("municipios.txt", "r", encoding="utf-8") as arquivo:
        municipios_input = arquivo.read().splitlines()

    with open("municipios_ibge.json", "r", encoding="utf-8") as municipios_ibge:
        municipios_ibge = json.load(municipios_ibge)

    municipios = [{municipio["id"]: municipio["nome"]} for m_input in municipios_input for municipio in municipios_ibge if m_input == municipio["nome"]]

    data = []

    for municipio in municipios:
        cod_municipio = list(municipio.keys())[0]
        municipio = list(municipio.values())[0]
        vdclient = VisdataClient(cod_municipio, municipio)
        data += vdclient.return_data()

    loader = LoaderDB(data)
    loader.load_data()

if __name__ == "__main__":
    main()