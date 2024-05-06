This is a simple e-commerce project 

## Installation

this requires Python 3.10.0

Install the dependencies and devDependencies and start the server.

```sh
create virtual environment : python -m venv env
activate virtual environment : .\env\Scripts\activate
install dependencies from requirements.txt : pip install -r .\requirements.txt

change values in .env accordingly such as db name, bd host, db password etc.
run command to migrate : python .\manage.py migrate
run command to register user : python .\manage.py createsuperuser
run command to run server : python .\manage.py runserver
now import postman collection which is in project directory named eComm
```
## end-points
- api/items/ : add, get and update items.
- api/my-kart/ : check orders which are in kart
- api/order-detail/<order-id>/ : check paid order details
- api/orders/ : create and update order


## Use
1. to create item
    api: http://127.0.0.1:8000/api/items/
    payload: {
    "name": "item3",
    "price": 300
}

2. update item
    api: http://127.0.0.1:8000/api/items/
    payload: {
    "name": "new name",
    "price": 399
}

3. to get access token, 
    api: http://127.0.0.1:8000/login/
    payload: {
    "username": "username",
    "password": "password"
}
this access token will be required to create order, update order, get kart details, get paid order details etc

4. create order
    api: http://127.0.0.1:8000/api/orders/
    payload: {
    "items":[1,2]
}
    this will take only item id(s)
    put access token in Headers see in postman requests

4. update order
    api: http://127.0.0.1:8000/api/orders/<order-id>/
    payload: {
    "status":"Accepted",
    "is_paid": true
}
    put access token in Headers see in postman requests

5. To see kart
    api: http://127.0.0.1:8000/api/my-kart/
    put access token in Headers see in postman requests
    this will show unpaid orders

6. To see paid order details
    api http://127.0.0.1:8000/api/order-detail/<order-id>/
    put access token in Headers see in postman requests
