# poke-cards-ml
This project is a playground to implement a rotation ML model on Pokémon cards.

## Project architecture

The project will be separated in several parts :
- A single page application that will be used to provide cards, rotate them, and provide them to the backend
- A backend that will call the ML model and return the result the web application
- A web scrapping tool to recover Pokémon cards and train the ML model
- A python script to recover the Pokémon cards recovered via web scrapping and rotate them randomly to create our dataset

## API

The API uses Poetry for dependency management. Don't forget to install it and run ```poetry install``` before anything !

The following commands will be run inside poetry virtual environment, which can be activated with the ```poetry shell``` command.
To exit the virtual environment, you can just type ```exit```.

### Run the application

You can start the api by running ```flask --app controller run``` inside the "src" folder.

### Tests

You can run the api unit tests by placing yourself in the "poke-cards-api" directory and running ```python -m unittest discover tests```.
