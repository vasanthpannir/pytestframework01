from src import BASE_URL,APIconstants

print(BASE_URL)

def get_url():
    base_url = APIconstants.base_url()
    print(base_url)

    create_token = APIconstants.create_token()
    print(create_token)