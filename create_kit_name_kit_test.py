import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    # Se usa el mismo user_body para todas las pruebas
    user_body = data.user_body.copy()
    user_response = sender_stand_request.post_new_user(user_body)
    # El token se obtiene directamente, parece redundante hacer
    # una función nueva pues usaría el mismo argumento y función
    auth_token = user_response.json()["authToken"]
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

def negative_assert_code_400(name):
    user_body = data.user_body.copy()
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 400

# Función para prueba 8
def negative_assert_no_kit_body(name):
    user_body = data.user_body.copy()
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    kit_body = {}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 400

# Lista de comprobación
def test_create_kit_name_1_char_get_success_response():
    positive_assert("a")
def test_create_kit_name_max_char_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
def test_create_kit_name_men_char_get_failure_response():
    negative_assert_code_400("")
def test_create_kit_name_may_char_get_failure_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
def test_create_kit_name_special_char_get_success_response():
    positive_assert("\"\"№%@\",\"")
def test_create_kit_name_spaces_get_success_response():
    positive_assert(" A Aaa ")
def test_create_kit_name_numbers_get_success_response():
    positive_assert("123")
def test_create_no_kit_body_get_failure_response():
    negative_assert_no_kit_body("a")
def test_create_kit_name_int_char_get_failure_response():
    negative_assert_code_400(123)
