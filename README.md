# cripto_lab3

Este algoritmo de hash es para verificar archivos descargados de un servidor. Para ello se realizan las siguiente dos funciones:

a) Subir archivo:

1) Al subir el archivo al servidor, se le aplica el hash de zehui.
2) Se sube el resultado del hash a un repositorio indicando al archivo que corresponde.

b) Descargar archivo:

1) Se descarga el archivo y se le aplica el hash de zehui.
2) Se compara el resultado del hash con el del repositorio.
3) Retorna la integridad del archivo con un mensaje de error o exito.


![Untitled Diagram drawio (3)](https://user-images.githubusercontent.com/80857812/173143275-b80d7a41-4967-4b8c-9c26-0ad786766257.png)



![Untitled Diagram drawio (2)](https://user-images.githubusercontent.com/80857812/173143318-7a7d7be4-7d96-4f52-8662-1152d7b6b077.png)
