"""Manage requests and controls response's data."""
import json
import requests


# Base url for requesting stuff.
BASE_URL = 'https://api-dados-abertos.tce.ce.gov.br'
# Default headers to requests.
HEADERS = {'accept': 'application/json',}
# Target timeline of data samples (start and end date).
TARGET_DATE = '2023-01-01_2023-12-31'


def __find_city_by_name(city_name: str) -> str:
    """Find a city id by it's name.

    Make a request to get every city and it's id from TCE,
    and iterate through each city to find the matching 
    'city_name'.

    Parameters
    ----------
    city_name : str
        The city name that'll be searched.

    Returns
    -------
    str
        The matching city id.
    """
    # Make a request to get every city from TCE.
    target_url: str = f'{BASE_URL}/municipios'
    response = requests.get(url=target_url, headers=HEADERS, timeout=10_000)
    response_data = response.json()

    # Iterate through each city and tries to find
    # the corresponding 'city_name'.
    for city in response_data['data']:
        if city['nome_municipio'].upper() == city_name.upper():
            print(f'Found {city_name}!')
            return city['codigo_municipio']
    print(f'{city_name} wasn\'t found.')
    return '-1' # City not found.


def __get_bidders_from_city_by_id(city_id: str) -> None:
    """Save every bidder from a city to a .json file.

    Make a request to get the target city using it's
    id from TCE, then get every bidder and save it to
    a .json file.

    Parameters
    ----------
    city_id : str
        The city id.
    """
    # Make a request to get bidders from a target city by it's id.
    target_url: str = f'{BASE_URL}/licitantes'
    parameters = {'codigo_municipio': city_id,
                  'data_realizacao_licitacao': TARGET_DATE,
                  'quantidade': 100,
                  'deslocamento': 0,}
    response = requests.get(url=target_url, headers=HEADERS, params=parameters, timeout=10_000)

    # Check if response was successful and save it to a .json file.
    if response.status_code == 200:
        response_data = response.json()
        if len(response_data['data']) > 0:
            with open(file='bidders_data.json', mode='w', encoding='utf-8') as file:
                json.dump(obj=response_data, fp=file, indent=2)
                file.close()
            print('File "bidders_data.json" saved.')
    else:
        print('Something went wrong while requesting data.')


def request_data(city_name: str) -> None:
    """Save every bidder data of any city from TCE to a .json file.

    Parameters
    ----------
    city_name : str
        The city's name that'll be requested from TCE.
    """
    city_id: str = __find_city_by_name(city_name=city_name)
    __get_bidders_from_city_by_id(city_id=city_id)
