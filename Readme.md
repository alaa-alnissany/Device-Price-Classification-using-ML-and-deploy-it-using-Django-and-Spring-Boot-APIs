# Device Price Classification using ML and deploy it using Django and Spring Boot APIs

Build and deploy a pretrained DEBERTA model for movie reviews semantic analysis with FastAPI and link it with a simple web page.

## Overview

Device price Classification involves using machine learning techniques to estimate the price range of mobile devices based on various features. These features can include specifications like battery power, RAM, camera quality, screen size, and more. By analyzing these features, we can predict whether a mobile device falls into a low-cost, medium-cost, high-cost, or very high-cost category.

## Installation

First, activate the virtual environment, after moving to the workspace directory:
```
.\Scripts\activate.bat
```
Second, install the libraraies in the environment from **requirements.txt** file:
```
pip install -r requirements.txt
```
## Usage

First, open CMD and activate the virtual environment if its deactivated, after moving to the workspace directory:
```
.\Scripts\activate.bat
cd DPC
```
Second, run the django Server:
```
python manage.py runserver
```
local host for django API is http://127.0.0.1:8000.
third, open move to Spring Boot folder "Api", then open CMD there and open VScode using typing this in the CMD:
```
Code .
```
then open this file as a tab in VScode:
```
.\src\main\java\com\DevicePriceClassifier\Api\DpcApplication.java
```
and run the server from there. 
local host for Spring Boot API is http://127.0.0.1:9090.
## Accessing the APIs

Django endpoints:

● POST /api/devices/: Retrieve a list of all devices
● GET /api/devices/{id}: Retrieve details of a specific device by ID.
● POST /api/adddevices: Add a new device.
● POST /api/predict/{deviceId}/: predict the class of specific device by ID.

Spring Boot endpoints:

● POST /api/devices/: Retrieve a list of all devices
● GET /api/devices/{id}: Retrieve details of a specific device by ID.
● POST /api/devices: Add a new device.
● POST /api/predict/{deviceId}: predict the class of specific device by ID.

