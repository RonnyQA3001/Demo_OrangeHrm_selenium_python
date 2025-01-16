import json

# Import JSON
with open('data/user_details.json') as file:
    config = json.load(file)

nationalities_iter = iter(config['nationalities'])

def get_nationality():
    try:
        return next(nationalities_iter)
    except StopIteration:
        return None

# Función para leer y ejecutar un archivo JS
def read_js(file_path, driver):
    with open(file_path, "r") as file:
        js_script = file.read()
    return driver.execute_script(js_script)
