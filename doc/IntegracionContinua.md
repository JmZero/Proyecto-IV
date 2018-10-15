# Integración Continua
Para añadir integración continua a nuestro proyecto vamos a utilizar la herramienta **Travis-CI**. Para conseguir que funcione tendremos que llevar a cabo los siguientes pasos:

1. Debemos haber subido las funcionalidades y los test a nuestro repositorio.
2. Iremos a la web de [Travis-CI](https://travis-ci.com/) y accederemos con nuestra cuenta de GitHub.
3. Seleccionaremos los repositorios de los cuales queremos que Travis lleve a cabo el testeo (en este caso Proyecto-IV).
4. Para que Travis funcione será necesario la creación de varios ficheros:
  - .travis.yml

  ```
  language: python

  python:
    - "3.6.6"

  install:
    - pip install -r requirements.txt

  script:
    - make test
  ```
  - Makefile: para ejecutar los test
  - requirements.txt

Una vez seguidos estos pasos Travis estará listo para testear nuestro repositorio.



## Test
Se han implementado varios test para comprobar la funcionalidad de la clase creada:
* testBattleTag: Comprobará si el BattleTag introducido esta dentro de la lista y si es correcto.
* testPerfilPublico: Comprobará si el perfil de jugador es público.
* testAddUser: Comprobará si se añade un perfil correctamente.
