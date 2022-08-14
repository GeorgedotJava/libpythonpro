import requests


def buscar_avatar(usuario):
    """
    Busca um usuário do github
    :param usuario: str com o nome do usuário
    :return: str com o link do usuário
    """

    url = f'https://api.github.com/users/{usuario}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('GeorgedotJava'))
