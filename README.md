
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Inceptia API</h3>

  <p align="center">
    API made with FastAPI. It uses requests, pandas.
    <a href="https://github.com/jbozas/inceptia"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jbozas/inceptia">Report Bug</a>
    <a href="https://github.com/jbozas/inceptia">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



### Built With

[![FastAPI][FastAPI-url]][FastAPI-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Resolución del enunciado ERS:

* Enunciado -> https://inceptia.notion.site/d208601409f649408f9d8f8e7ddb2849
* Crear una API con Python, usando el framework FastAPI _> que tenga dos endpoints:
    - GET /check_temperature/
    Este endpoint deberia llamar a WeatherService y chequear si la temperatura es mayor a una temperatura recibida por parametro de una ubicacion recibida por parametro
    Por defecto esta tempertura y ubicacion deberia ser 28 y peguajo respectivamente.
    - GET /is_product_available/
    Crear un nuevo Pedido, este endpoint deberia recibir producto, cantidades y retornar OK si todo esta bien
    Ademas, deberia almacenar el resultado de la busqueda, en caso de que este mal, almacenar 1 intento mas en la cache. Invalidar la request si se solicita mas de tres veces el mismo producto en menos de un minuto.



Consideraciones
* Crear Colección en POSTMAN - DONE 
* Agregar Dockerfile - DONE
* Agregar Documentación - DONE
* Agregar Logs - DONE
* Agregar pre-commit - DONE
* Agregar mypy - DONE
* Agregar requirements con versions - DONE

### Installation

1. Build the image.
   ```
   docker build -t inceptia .
   ```
2. Run it.
   ```
   docker run -p 8000:8000 inceptia
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jbozas/inceptia.svg?style=for-the-badge
[contributors-url]: https://github.com/jbozas/inceptia/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jbozas/inceptia.svg?style=for-the-badge
[forks-url]: https://github.com/jbozas/inceptia/network/members
[stars-shield]: https://img.shields.io/github/stars/jbozas/inceptia.svg?style=for-the-badge
[stars-url]: https://github.com/jbozas/inceptia/stargazers
[issues-shield]: https://img.shields.io/github/issues/jbozas/inceptia.svg?style=for-the-badge
[issues-url]: https://github.com/jbozas/inceptia/issues
[license-shield]: https://img.shields.io/github/license/jbozas/inceptia.svg?style=for-the-badge
[license-url]: https://github.com/jbozas/inceptia/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jbozas
[product-screenshot]: images/screenshot.png
[Fastapi-url]: https://img.shields.io/badge/fastapi-%252300ADD8.svg?style=for-the-badge&logo=fastapi&logoColor=white
[Sqlalchemy-url]: https://img.shields.io/badge/sqlalchemy-%252300ADD8.svg?style=for-the-badge&logo=sqlalchemy&logoColor=white
[Sqlite-url]: https://img.shields.io/badge/sqlite-%252300ADD8.svg?style=for-the-badge&logo=sqlite&logoColor=white