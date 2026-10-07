import pytest

import main

import requests

@pytest.mark.parametrize( 
"a , b , result",
[
    (1 , 2 , 3),
    (4 , 5 ,9),
    (-1 , -1 , -2)
])
def test_add( a, b, result):
    assert main.add(a , b) == result


def test_devide():
    with pytest.raises(ZeroDivisionError , match ="Division by 0 is not allowed"):
        main.devide(10 , 0)
        
@pytest.mark.parametrize(
    "amount , deduction , result",
    [
        (1000 , 200 , 800),
        (1500 , 100 , 1400),
    ]
)    
def test_widthdrwal(amount , deduction , result):
    assert main.widthdrwal(amount , deduction) == result


def test_deduction():
    with pytest.raises(ValueError , match = "Amount is less than withdrwal amount"):
        main.widthdrwal(600 , 3000)

@pytest.fixture
def customer():
    return{
        "id": 101,
        "name": "Aditya",
        "points": 500
    }
        
def test_customer_points(customer):
    assert customer["points"] == 500
    

@pytest.fixture
def database():
    print("\n Database connection made")
    
    db = {
        "status" : "connected"
    }
    yield db
    
    print("\n closing database")
    
def test_database(database):
    assert database['status'] == 'connected'
    
def test__mock_api(mocker):
    
    mock_get = mocker.patch("main.requests.get")
    
    mock_get.return_value.json.return_value = {
        'id': 101,
        'name' : 'user1'
    }
    
    result = main.get_customer(101)
    
    assert result == {
        'id': 101,
        'name' : 'user1'
    }
    
    mock_get.assert_called_once_with(
        "https://example.com/customers/101"
    )
    
def test_timeout_api(mocker):
    
    mock_get = mocker.patch("main.requests.get")
    mock_get.side_effect = requests.Timeout
    result = main.get_customer(101)
    assert result is None
