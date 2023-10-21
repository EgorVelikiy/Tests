import requests
from get_token import get_tok


def create_folder(folder_name):
    token = get_tok()
    url = f"https://cloud-api.yandex.net/v1/disk/resources/"
    params = {'path': folder_name}
    headers = {
        'Authorization': f'OAuth {token}'
    }

    response = requests.request("PUT", url, headers=headers, params=params)

    return response.status_code


