# Sunflower

## Introduction

Our idea is to align solar panels towards the sun throughout the day to maximize the power output.

The core idea stems from the natural behaviour of Sunflowers which always face the sun (hence the name). Our goal is to mimic that behaviour. We are using the pvlib package in Python for calculating the angles.

pvlib python is a community-developed toolbox that provides a set of functions and classes for simulating the performance of photovoltaic energy systems and accomplishing related tasks.

## Run Locally

Clone the project

```cmd
git clone https://github.com/navaneethkrishna30/Sunflower/
```

Go to the project directory

```cmd
cd Sunflower
```

Activate Virtual Environment

```cmd
python -m venv venv
venv/scripts/activate
```

Install Dependencies
```cmd
pip3 install requirements.txt
```

## API Endpoints

### Sunrise and Sunset

**POST** `/sunrise-and-sunset`

Request Body:
```json
{
  "latitude": 43,
  "longitude": 56,
  "timezone": "Asia/Kolkata",
  "date": "2025-01-11"
}
```

### Angles

**POST** `/angles`

Request Body:
```json
{
  "latitude": 43,
  "longitude": 56,
  "timezone": "Asia/Kolkata",
  "date": "2025-01-11",
  "sunrise": "2025-01-11 09:15:40",
  "sunset": "2025-01-11 18:32:30"
}
```

## Acknowledgements

- Anderson, K., Hansen, C., Holmgren, W., Jensen, A., Mikofski, M., and Driesse, A. “pvlib python: 2023 project update.” Journal of Open Source Software, 8(92), 5994, (2023). DOI: 10.21105/joss.05994.

- Holmgren, W., Hansen, C., and Mikofski, M. “pvlib python: a python package for modeling solar energy systems.” Journal of Open Source Software, 3(29), 884, (2018). DOI: 10.21105/joss.00884.

## Related

Here are some related links:

- [pvlib Docs](https://pvlib-python.readthedocs.io/en/stable/)

