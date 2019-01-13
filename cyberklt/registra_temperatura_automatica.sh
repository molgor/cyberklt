# /bin/bash
# Este Script registra en intervalos de 5 minutos la temperatura (y altura) usando el django app

NTIME=$1
for i in $(seq $NTIME ); 
	do curl http://raspberrypi.local:8000/temp/; 
	echo "lectura $i"; 
	sleep 5m; 
	done
