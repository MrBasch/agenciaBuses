# agenciaBuses

Solucion a problema de agencia de buses desarrollada en django + nuxt.js

### Pre-requisitos 📋

Configurar PIP (python) y NPM (nodejs)
https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/
https://codingpotions.com/npm-tutorial

Paso 1: Clonar el proyecto de github
https://github.com/MrBasch/agenciaBuses.git

Crear ambiente de trabajo (virtual environment) a elección, personalmente use venv de python
https://towardsdatascience.com/virtual-environments-104c62d48c54#ee81

Instalar requerimientos del proyecto

> _python -m pip install -r requirements.txt_

## Comenzando 🚀

Desde DjangoAPI

    Crear usuario

> _python manage.py createsuperuser --email admin@example.com --username admin_

    Iniciar API

> _python manage.py runserver_

Desde FrontNuxt

Iniciar el servidor NUXT

> _npm run serve_

Iniciados los servidores, inicie sesion desde la pagina inicial desde el servidor nux ("base-url/")
Esta accion permitira a la adquisicion del token de seguridad, necesario para realizar las consultas de FrontNuxt a la API django
