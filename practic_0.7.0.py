# Задача 1

import requests

latitude, longitude = 56.50, 60.35

url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation,weathercode"
response=requests.get(url)
data=response.json()

print(data)

# Задача 2

import requests

url = 'https://pokeapi.co/api/v2/pokemon?limit=20&offset=0'


pokemons = requests.get(url).json()['results']
for x in pokemons:
    print(f"{x['name']}")

choice = input('Введите имя покемона: ')


url = f'https://pokeapi.co/api/v2/pokemon/{choice}/'
pokemon_info = requests.get(url).json()


result = []

for x in pokemon_info['abilities']:
    result.append(x['ability']['name'])


print(f"Имя: {pokemon_info['name']}")
print(f"Тип: {pokemon_info['types'][0]['type']['name']}")
print(f"Вес: {pokemon_info['weight']}")
print(f"Рост: {pokemon_info['height']}")
print(f"Способности: {', '.join(result)}")

# Задача 3

import requests


def get_json_page():
    return requests.get('https://jsonplaceholder.typicode.com/posts').json()


def get_json_page_by_id(ids):
    return requests.get('https://jsonplaceholder.typicode.com/posts/{}'.format(ids)).json()


def get_info_from_page(ids):
    r = get_json_page_by_id(ids)

    print('Post ID: ', r['id'])
    print('User ID: ', r['userId'])
    print('Title: ', r['title'])
    print('Body: ', r['body'])


print(get_json_page())
print(get_json_page_by_id(2))
get_info_from_page(2)

# Задача 4

import requests


def get_json_page():
    return requests.get('https://jsonplaceholder.typicode.com/posts').json()


def get_json_page_by_id(ids):
    return requests.get('https://jsonplaceholder.typicode.com/posts/{}'.format(ids)).json()


def get_info_from_page(ids):
    r = get_json_page_by_id(ids)

    print('Post ID: ', r['id'])
    print('User ID: ', r['userId'])
    print('Title: ', r['title'])
    print('Body: ', r['body'])


def create_new_post():
    title = input("Укажите заголовок: ")
    bd = input("Укажите содержимое пост: ")
    user_id = input("Введите ид пользоваателя: ")

    new_post = {
        "title": title,
        "body": bd,
        "userId": int(user_id)
    }

    res = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
    return res.json()


def update_post():
    post_id = input("Введите ид поста: ")
    title = input("Укажите загловок: ")
    bd = input("Укажите содержимое: ")

    upd_post = {
        "title": title,
        "body": bd
        }

    rep = requests.put(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=upd_post)
    return rep.json()


def delete_post():
    ids = input("Укажите ид поста для удаления: ")
    red = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{ids}')
    return red.status_code


# print(get_json_page())

# print(get_info_from_page(2))

# new_post = create_new_post()
# print(new_post)

# updated_post = update_post()
# print(updated_post)

# status_code = delete_post()
# print(status_code)

# Задача 5

import requests


def get_all_dogs():
    result = []
    req = requests.get('https://dog.ceo/api/breeds/list/all').json()

    for dog in req['message']:
        if req['message'][dog] == []:
            result.append(dog)
        else:
            for z in req['message'][dog]:
                result.append(f'{dog}-{z}')
    
    i = 1
    for dog in result:
        print(f'{i}. {dog}')
        i += 1


def get_dog_image():
    result = []
    dogs = input('Введите одну или несколько собак через запятую: ').split(' ')

    
    for dog in dogs:
        dog = dog.strip(',').strip()
        
        if '-' in dog:
            dog_split = dog.split('-')
            # https://dog.ceo/api/breed/hound/afghan/images/random
            req = requests.get(f'https://dog.ceo/api/breed/{dog_split[0]}/{dog_split[1]}/images/random').json()
        
        else:
            req = requests.get(f'https://dog.ceo/api/breed/{dog}/images/random').json()
        
        result.append([dog, req['message']])
        
    i = 1
    for dog in result:
        print(f'{i}. {dog[0]}\n   {dog[1]}\n')
        i += 1


get_all_dogs()
get_dog_image()