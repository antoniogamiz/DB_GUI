# DATA BASE MANAGEMENT
Este programa consiste en una pequeña interfaz gráfica para la gestión de bases de datos con MySQL.

##### Requisitos
* Tener instalados los módulos `python-gobject` y `gobject-introspection` (`sudo apt-get install python-gobject gobject-introspection` para instalarlos.
* Tener MySQL instalado y contar con un usuario con suficientes permisos en una base de datos.
* (Recomendable): No tener ninguna tabla llamada `FIELD` en la base de datos, ya que esa es la que usa el programa (si se tiene creada, y se quiere editar con el programa, también se podrá, pero lanzará un Warning avisando).
