#!/usr/bin/bash

hadoop fs -rm -r trabajo
hadoop fs -mkdir -p trabajo

chmod 740 make_custom_dataset.py
chmod 740 plot_results.py

#1º Descargar dataset
python ./make_custom_dataset.py ./datasets_urls.txt
#cat custom_dataset.txt | python mapper.py | sort -k 1,1 | python reducer.py

mv custom_dataset.txt ./dataset

hadoop fs -put ./dataset trabajo

#2º Configurar hadoop


#3º Realizar consultas

hs ./querys/1/mapper.py ./querys/1/reducer.py trabajo/dataset/ trabajo/output/Consulta1
hs ./querys/2/mapper.py ./querys/2/reducer.py trabajo/dataset/ trabajo/output/Consulta2
hs ./querys/3/mapper.py ./querys/3/reducer.py trabajo/dataset/ trabajo/output/Consulta3
hs ./querys/4/mapper.py ./querys/4/reducer.py trabajo/dataset/ trabajo/output/Consulta4
hs ./querys/5/mapper.py ./querys/5/reducer.py trabajo/dataset/ trabajo/output/Consulta5



#4º Recuperar resultados de las consultas y pasarselos a los scripts para pintar las graficas

hadoop fs -text trabajo/output/Consulta1/part-00000 > ./results/query1.txt
hadoop fs -text trabajo/output/Consulta2/part-00000 > ./results/query2.txt
hadoop fs -text trabajo/output/Consulta3/part-00000 > ./results/query3.txt
hadoop fs -text trabajo/output/Consulta4/part-00000 > ./results/query4.txt
hadoop fs -text trabajo/output/Consulta5/part-00000 > ./results/query5.txt


python ./plot_results.py ./results/query1.txt ./plots/query1.png "bar-plot" "off" "Value" " Valor Promedio Historico"
python ./plot_results.py ./results/query2.txt ./plots/query2.txt "table" "on" "Value" "Fecha valor Historico mas alto"
python ./plot_results.py ./results/query3.txt ./plots/query3.png "bar-plot" "on" "Value" "Fecha del valor de cierre más alto en ultimo mes"
python ./plot_results.py ./results/query4.txt ./plots/query4.txt "table" "off" "Volume" "Moneda con el volumen de transacciones mas alto ultima semana"
python ./plot_results.py ./results/query5.txt ./plots/query5.txt "table" "on" "Diferencia" "Monedas con registros donde la diff(open-close) > 50%"

scp -o StrictHostKeyChecking=no -i ../../access_lab ./plots/query1.png alucloud192@lab2.cursocloudaws.net:/home/alucloud192/.
scp -o StrictHostKeyChecking=no -i ../../access_lab ./plots/query2.txt alucloud192@lab2.cursocloudaws.net:/home/alucloud192/.
scp -o StrictHostKeyChecking=no -i ../../access_lab ./plots/query3.png alucloud192@lab2.cursocloudaws.net:/home/alucloud192/.
scp -o StrictHostKeyChecking=no -i ../../access_lab ./plots/query4.txt alucloud192@lab2.cursocloudaws.net:/home/alucloud192/.
scp -o StrictHostKeyChecking=no -i ../../access_lab ./plots/query5.txt alucloud192@lab2.cursocloudaws.net:/home/alucloud192/.


ssh  -o StrictHostKeyChecking=no -i ../../access_lab alucloud192@lab2.cursocloudaws.net "bash -s" < ./s3_upload.sh