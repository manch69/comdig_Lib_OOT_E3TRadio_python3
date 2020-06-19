# comdig_Lib_OOT_E3TRadio_python3
This a gnuradio OOT
You have to have installed gnuradio library to be able to install this OOT. OOT as complements for gnuradio library

## PRERREQUISITOS
Fuera de las librerias que pueden ser tradicionales en Python3, debe instalarse previamente la libreria Eyediagram. Para hacerlo, se tiene un instalador con instrucciones en:  https://github.com/hortegab/comdig_Diagrama-de-ojo-Comunicaciones-II.git

Si algún dia surge la necesidad de prescindir de la instalación de EyeDiagram, lo que hay que tener en cuenta que solo tenemos dos bloques que dependen de ella y habría que eliminarlos del OOT, esto son:
- vec_diagrama_ojo_f
- b_eye_diagram_f

## INSTRUCCIONES

Busca la carpeta build en la raiz. Si tiene cosas bórralas. Si no existe, creela. 
Finalmente, realiza la instalación por terminal, ubicado dentro de la carpeta buid con los siguientes comandos:

```
cmake ..
make
sudo make install
sudo ldconfig
```
Hay un problema con las configuraciones del path hasta solucionar este bug es necesario ejecutar:
```
sudo cp -r /usr/local/lib/python3/dist-packages/E3TRadio /usr/local/lib/python3.8/dist-packages/
```
La libreria se esta guardando en python 3.0 pero se tiene instalado python 3.8
