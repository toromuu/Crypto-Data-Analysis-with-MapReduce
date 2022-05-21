#!/usr/bin/bash


#1º Descargar dataset
python ../make_custom_dataset.py ../datasets_urls.txt
#cat custom_dataset.txt | python mapper.py | sort -k 1,1 | python reducer.py

#2º Configurar hadoop

#3º Realizar consultas

hs ./querys/1/mapper.py ./querys/1/reducer.py trabajo/dataset/ trabajo/output/Consulta1
hs ./querys/2/mapper.py ./querys/2/reducer.py trabajo/dataset/ trabajo/output/Consulta2
hs ./querys/3/mapper.py ./querys/3/reducer.py trabajo/dataset/ trabajo/output/Consulta3
hs ./querys/4/mapper.py ./querys/4/reducer.py trabajo/dataset/ trabajo/output/Consulta4
hs ./querys/5/mapper.py ./querys/5/reducer.py trabajo/dataset/ trabajo/output/Consulta5


#4º Recuperar resultados de las consultas y pasarselos a los scripts para pintar las graficas

hadoop fs -text trabajo/output/Consulta1/part-00000 | ./plots
hadoop fs -text trabajo/output/Consulta2/part-00000 |
hadoop fs -text trabajo/output/Consulta3/part-00000 |
hadoop fs -text trabajo/output/Consulta4/part-00000 |
hadoop fs -text trabajo/output/Consulta5/part-00000 |