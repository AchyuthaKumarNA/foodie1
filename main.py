import typer
from peewee import *
from model import create_tables
from service.users import UserSession,AuthenticationService
from command import users, restaurant ,cart,food,orders


app = typer.Typer()

user_session = users.user_session
auth = users.auth

app.add_typer(users.app, name="user")
app.add_typer(restaurant.app, name ="restaurant")
app.add_typer(food.app, name="food")
app.add_typer(cart.app, name="cart")
app.add_typer(orders.app, name="order")



if __name__ == "__main__":
    create_tables()
    with user_session:
        auth.load_session()
        app()