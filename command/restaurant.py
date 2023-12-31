from typing_extensions import Annotated
import typer
from service.restaurant import Restaurantservice

restaurant_service =Restaurantservice()


app = typer.Typer()

@app.command()
def add(
    name: Annotated[str, typer.Option(prompt=True)],
    rating: Annotated[float, typer.Option(prompt=True)],
):
    restaurant_service.add_restaurant(name, rating)

@app.command()
def remove(
    name: Annotated[str, typer.Option(prompt=True)]
):
    restaurant_service.remove_restaurant(name)

@app.command()
def display():
    restaurant_service.display_restaurants()

@app.command()
def list_foods(
    restaurant_name: Annotated[str, typer.Option(prompt=True)],
):
    restaurant_service.list_foods(restaurant_name)