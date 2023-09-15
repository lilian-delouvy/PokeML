# poke-cards-ml
This project is a playground to implement a rotation ML model on pokemon cards.

## Project architecture

The project will be separated in several parts :
- A single page application that will be used to provide cards, rotate them, and provide them to the backend
- A backend that will call the ML model and return the result the web application
- A web scrapping tool to recover pokemon cards and train the ML model
- A python script to recover the pokemon cards recovered via web scrapping and rotate them randomly to create our dataset