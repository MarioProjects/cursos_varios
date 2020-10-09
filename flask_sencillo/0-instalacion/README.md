# Preparación del entorno Flask

A través de esta guía crearemos aplicaciones de Python utilizando el microframework de Flask. Antes de ello necesitaremos instalar los componentes necesarios.

## Instalar los componentes necesarios

Nuestro primer paso será instalar todo lo que necesitamos desde los repositorios de Ubuntu. Esto incluye `pip`, el administrador de paquetes de Python, que gestionará nuestros componentes de Python. También obtendremos los archivos de desarrollo de Python necesarios para crear algunos de los componentes de Gunicorn.

Primero, actualizaremos el índice de paquetes locales e instalaremos los paquetes que nos permitirán crear nuestro entorno de Python. Entre ellos está `phyton3-pip`, junto con paquetes y herramientas de desarrollo adicionales que se necesitan para un entorno de programación sólido:

```sh
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
```

Una vez implementados estos paquetes, crearemos un entorno virtual para nuestro proyecto

## Crear un entorno virtual en Python

A continuación, configuraremos un entorno virtual para aislar nuestra aplicación de Flask de los otros archivos de Python del sistema.

Comience instalando el paquete phyton3-venv, que instalará el módulo venv:

```sudo apt install python3-venv```

Luego, crearemos un directorio principal para nuestro proyecto de Flask. Después de crearlo, posiciónese en él:
```
mkdir ~/curso_flask
cd ~/curso_flask
```
Cree un entorno virtual para almacenar los requisitos de Python de su proyecto de Flask escribiendo lo siguiente:

```virtualenv -p python3 venv```

Con esto se instalará una copia local de Python y pip en un directorio llamado myprojectenv dentro del directorio de su proyecto.

Antes de instalar aplicaciones dentro del entorno virtual, deberá activarlo. Hágalo escribiendo lo siguiente:

```source venv/bin/activate```

Su mensaje cambiará para indicar que ahora realiza operaciones dentro del entorno virtual. Se parecerá a esto: `(venv)user@host:~/curso_flask$`.

## Configurar el entorno de Flask

Ahora que se encuentra en su entorno virtual, podrá instalar Flask y Gunicorn y comenzar a diseñar su aplicación.

Primero, instalaremos wheel con la instancia local de pip para asegurarnos de que nuestros paquetes se instalen aunque falten archivos de wheel:

`pip install wheel`

Nota: Independientemente de la versión de Phyton que use, cuando se active el entorno virtual deberá utilizar el comando pip (no pip3).

A continuación, instalaremos Flask y Gunicorn:

`pip install gunicorn flask`
