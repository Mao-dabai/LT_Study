
def test_login(login, json_data):
    data = json_data('data/prod.json')
    username, password = data['users']['user01']
    login(username, password)


def test_view(driver, search, json_data):
    data = json_data('data/prod.json')
    search_key = data['search_key']['key01']
    print(search_key)
    search(search_key)
    driver.find_elements('class name', 'goods-item')[1].click()
