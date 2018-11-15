import json
import requests

api_url_base = 'https://swapi.co/api/'
resource = '{0}people/'
final_results_set = []


def get_people_info(api_url):

    if api_url == None:
        api_url = resource.format(api_url_base)

    response = requests.get(api_url)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


def print_people_info(people_info, items):
    if people_info is not None:
        size = people_info['count']

        for results_set in people_info['results']:
            # print(' \n', results_set)
            final_results_set.append(results_set)
            items += 1

        if people_info['next'] is not None and size != items:
            next_page = get_people_info(people_info['next'])
            print_people_info(next_page, items)
    else:
        print('[!] Solicitação inválida')


print("Aqui estão suas informações: ")
people_info = get_people_info(None)
items = 0
print_people_info(people_info, items)

print(final_results_set[0])
