# Shopping_helper

![license](https://img.shields.io/badge/license-MIT-blue)
![linux](https://img.shields.io/badge/os-Linux-green)
![language](https://img.shields.io/badge/language-Python3.8-blue)
![language](https://img.shields.io/badge/language-Django4.0-brightgreen)
![version](https://img.shields.io/badge/version-1.0.0-success)
![status](https://img.shields.io/badge/status-production-green)

A web browser based program based on Vue and Django. It allows you to analyze your expenses.

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)

## General info
The program is based on the django and vue frameworks. It allows the user to easily manage and analyze expenses data. 

Dictionaries allow you to analyze data not only by date but also by products and categories.
The website contains a login system based on an expiring token. Thanks to this system, it is possible to divide data into users. 

The backend works as a REST API, so the frontend written in VUE is not slowed down by the server. 

<p align="center" width="100%">
    <img width="50%" src="https://github.com/Miklakapi/shopping_helper/blob/master/README_IMAGES/Dashboard..png"> 
    <br>
    <img width="32%" src="https://github.com/Miklakapi/shopping_helper/blob/master/README_IMAGES/Dictionary.png"> 
    <img width="32%" src="https://github.com/Miklakapi/shopping_helper/blob/master/README_IMAGES/List.png"> 
    <img width="32%" src="https://github.com/Miklakapi/shopping_helper/blob/master/README_IMAGES/History.png"> 
    <br>
    <img width="50%" src="https://github.com/Miklakapi/shopping_helper/blob/master/README_IMAGES/Login.png"> 
</p>

## Technologies
Project is created with:

* Python 3.8.10
* Django 4.0.4

## Setup
### Django API
1. Enter the python virtual environment.
2. Create a database using migration ```python manage.py migrate```.
3. Create a user ```python manage.py createsuperuser```.
4. Start API ```python manege.py runserver <adress:port>```
5. Remember change API IP in Vue

### Vue
1. Run build ```npm run build```
2. An application has been generated in catalog ```dist```

## Features
* Product and category dictionaries for better data management
* Possible editing and adding of data.
* Data pagination.
* Login system using an expiring token.
* List of things to buy independent of dictionaries.
* Expense charts and tables.
* Graph results related to the logged in user only.
* Error handling.

## Status
The project's development has been completed.
