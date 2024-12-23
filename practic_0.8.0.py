# Задача 1

import requests

api_key = ''


def get_apod():
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

    data = requests.get(url).json()

    result = ''
    result += f'Название: {data["title"]}\n'
    result += f'Описание: {data["explanation"]}\n'
    result += f'Дата: {data["date"]}\n'

    return result


def get_photo():
    rover = input("Выберите один из вариантов (Curiosity, Opportunity, Spirit): ")
    camera = input("Выберите один из типов камер (FHAZ, RHAZ, NAVCAM, etc.): ")
    photo_count = int(input("Введите кол-во снимков которые хотите получить (0-10): "))
    date = input("Введите дату (YYYY-MM-DD): ")
    
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos"
    params = {"earth_date": date, "camera": camera, "api_key": api_key}

    data = requests.get(url, params=params).json()

    photos = data.get("photos", [])
    
    result = ''
    if photos:
        for photo in photos[:photo_count]:
            result += f'ID: {photo["id"]}\n'
            result += f'Ссылка: {photo["img_src"]}\n'

        print(result)
        
    else:
        print('Не найдено фотографий по Вашим параметрам')


def get_neos():
    date = input("Введите дату (YYYY-MM-DD): ")

    url = 'https://api.nasa.gov/neo/rest/v1/feed'
    params = {"start_date": date, "end_date": date, "api_key": api_key}

    data = requests.get(url, params=params).json()
    neos = data.get("near_earth_objects", {}).get(date, [])

    result = ''

    for neo in neos:
        result += f'Имя: {neo["name"]}\n'
        result += f'Диаметр: {neo["estimated_diameter"]["meters"]["estimated_diameter_max"]} м\n'
        result += f'Опасен ли: {neo["is_potentially_hazardous_asteroid"]}\n'

    print(result)


def get_weather():
    url = f"https://api.nasa.gov/DONKI/FLR?api_key={api_key}"
    data = requests.get(url).json()

    result = ''

    for flare in data[:5]:
        result += f'Начало в {flare["beginTime"]}\n'
        result += f'Класс: {flare["classType"]}\n'
        result += f'Источник: {flare["sourceLocation"]}\n'
    
    print(result)


def main():
    while True:
        print("\nМеню:")
        print("1. Астрономическая картинка дня (APOD)")
        print("2. Фото с марсохода")
        print("3. Объекты, сближающиеся с Землей (NEOs)")
        print("4. Космическая погода")
        print("5. Выход")

        choice = input("Выберите опцию (1-5): ")

        if choice == "1":
            print(get_apod())
        elif choice == "2":
            get_photo()
        elif choice == "3":
            get_neos()
        elif choice == "4":
            get_weather()


main()

# Задача 2

import requests


url = "https://api.artic.edu/api/v1/artworks"


def get_art(page=1):
    params = {"page": page, "limit": 10}
    data = requests.get(url, params=params)
    
    if data.status_code != 200:
        print("Ошибка.")
        return [], 0

    data = data.json()
    arts = data.get("data", [])
    tp = data.get("pagination", {}).get("total_pages", 0)
    
    return arts, tp


def filter_art(arts, name):
    result = []

    for art in arts:
        artist = art['artist_title']
        
        if name.lower() in artist.lower():
            result.append(art)

    return result


def show_detail(art):
    title = art.get('title', 'Неизвестное название')
    artist = art.get('artist_title', 'Неизвестный художник')
    date = art.get('date_display', 'Неизвестная дата')
    medium = art.get('medium_display', 'Неизвестный носитель')

    print(f"\nНазвание: {title}")
    print(f"Исполнитель: {artist}")
    print(f"Дата: {date}")
    print(f"Носитель: {medium}\n")


def main():
    page = 1
    arts = []
    total_pages = 0

    while True:
        print("\nМеню:")
        print("1. Просмотр")
        print("2. Филтр по художнику")
        print("3. Подробная информация")
        
        choice = input("Выберите опцию (1-4): ")

        if choice == "1":
            arts, total_pages = get_art(page)

            if arts:
                print("\nПроизведения:")

                for i, art in enumerate(arts, start=1):
                    print(f"{i}. {art['title']}")

                print(f"\nСтраница {page}/{total_pages}")

                if page > 1:
                    print("5. Предыдущая страница")

                if page < total_pages:
                    print("6. Следующая страница")


        elif choice == "2":
            name = input("Укажите имя художника: ")
            filtered_arts = filter_art(arts, name)

            if filtered_arts:
                print("\nРезультаты фильтра:")
                for i, art in enumerate(filtered_arts, start=1):
                    print(f"{i}. {art['title']}")

            else:
                print("Произведения не найдены.")
        

        elif choice == "3":
            num = int(input("Введите номер произведения: ")) - 1

            if 0 <= num < len(arts):
                show_detail(arts[num])
            else:
                print("Неверный номер.")
        
        elif choice == "5" and page > 1:
            page -= 1
        

        elif choice == "6" and page < total_pages:
            page += 1


main()

# Задача 3

import requests
import time


url = "https://api.coingecko.com/api/v3"


cryptos = []


def get_current_price(crypto_id):
    link = f"{url}/simple/price?ids={crypto_id}&vs_currencies=usd&include_percentage_change_24h=true"
    data = requests.get(link).json()

    if crypto_id in data:
        price = data[crypto_id]['usd']
        change_24h = data[crypto_id]['usd_24h_change']
        return price, change_24h
    
    return None, None


def create():
    print("\nСоздание портфеля криптовалют")
    while True:
        crypto_id = input("Введите ид криптовалюты (bitcoin или ethereum), q для завершения: ").lower()
        if crypto_id == 'q':
            break

        amount = float(input(f"Введите кол-во {crypto_id}: "))
        cryptos.append({'id': crypto_id, 'amount': amount})

    print("Портфель создан")


def calculate():
    total_value = 0

    for crypto in cryptos:
        price, change_24h = get_current_price(crypto['id'])

        if price:
            value = price * crypto['amount']
            print(f"{crypto['id'].capitalize()}: {crypto['amount']} шт = {value:.2f} (Цена: {price:.2f}, Изменение 24ч: {change_24h:.2f}%)")
            total_value += value

    print(f"\nОбщая стоимость портфеля: {total_value:.2f}")


def show_changes():
    print("\nИзменения за последние сутки:")

    for crypto in cryptos:
        price, change_24h = get_current_price(crypto['id'])

        if price:
            if change_24h > 10:
                print(f"{crypto['id'].capitalize()} - увеличение: {change_24h:.2f}%")

            elif change_24h < -10:
                print(f"{crypto['id'].capitalize()} - понижение: {change_24h:.2f}%")


def get_historical():
    crypto_id = input("Введите ид криптовалюты (bitcoin, ethereum, ..): ").lower()

    link = f"{url}/coins/{crypto_id}/market_chart"
    params = {'vs_currency': 'usd', 'days': '7'}

    response = requests.get(link, params=params)
    data = response.json()
    prices = data.get('prices', [])
    
    print(f"\nДанные за последнюю неделю | {crypto_id.capitalize()}:")
    for price_data in prices:
        timestamp, price = price_data
        time_str = time.strftime('%Y-%m-%d', time.localtime(timestamp / 1000))
        print(f"Дата: {time_str}, Цена: {price:.2f}")


def main():
    while True:
        print("\nМеню:")
        print("1. Создать портфель")
        print("2. Посчитать стоимость портфель")
        print("3. Показать криптовалюты с наибольшими изменениями")
        print("4. Просмотреть данные о криптовалюте")

        choice = input("Выберите опцию (1-5): ")

        if choice == '1':
            create()
        elif choice == '2':
            calculate()
        elif choice == '3':
            show_changes()
        elif choice == '4':
            get_historical()
        else:
            print("Неверный выбор. Попробуйте снова.")


main()