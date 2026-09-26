# Pokémon REST API

This is my RESTful api built with flask,python,with SQLite. This API is all about Pokemon Niche with their Names, PokeDexNumber, and Types.

## Base URL
* **Local Server:** `http://127.0.0.1:5000/api/pokemon`
* **Live Deployment (Render):** `https://roa-rest-api.onrender.com/api/pokemon`

## Endpoints Overview

Method  Endpoint 

**GET**  `/api/pokemon`  
**GET**  `/api/pokemon/:id` 
**POST**  `/api/pokemon` 
**PUT**  `/api/pokemon/:id` 
**DELETE** `/api/pokemon/:id` 

---

## Screenshots
# GET Method
![GET1.png](/screenshots/GET1.png)

![GET2.png](/screenshots/GET2.png)

![GET3.png](/screenshots/GET3.png)

# GET Pokemon

![GETPOKEMON.png](/screenshots/GETPOKEMON.png)

# POST Method

![POST.png](/screenshots/POST.png)

![POST2.png](/screenshots/POST2.png)

# PUT Method

![PUTPOKEMON.png](/screenshots/PUTPOKEMON.png)

# DELETE Method

![DELETE.png](/screenshots/DELETE.png)

# Render Link URL

![GETRENDER.png](/screenshots/GETRENDER.png)


## Sample Requests & Responses

### 1. GET `/api/pokemon`
* **Request:** `curl -X GET http://127.0.0.1:5000/api/pokemon`
* **Response:**
```json
[
  {
    "id": 1,
    "name": "Bulbasaur",
    "pokedexNumber": 1,
    "types": ["Grass", "Poison"]
  }
]
{
    ...... (others) .....
}

