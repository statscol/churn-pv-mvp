# churn-pv-mvp


Churn Analysis model MVP

Revisar notebooks en formato `.ipynb` con detalle del proceso de generación del modelo y su despliegue.


## Uso de aplicativo REST API

en la carpeta `app` se encuentran los archivos del aplicativo desarrollado en FastAPI para la detección de churn.


Para crear una imagen docker con todos los artefactos debe ir a la terminal y ejecutar

```bash
docker build -t churn_detector:1.0 .
```

Una vez se haya creado la imagen, deberá ejecutarla con la siguiente instrucción en consola

```bash
docker run -d -p 5050:5005 --name <EL_NOMBRE_QUE_DESEE> churn_detector:1.0
```

La aplicación estará disponible en http://localhost:5050 o el puerto que haya definido para la misma. Una prueba rápida del modelo puede realizarse accediendo a la documentación de Swagger a través de http://localhost:5050/docs , donde podrá probar el modelo en tiempo real. Esta documentación tiene además, el formato de input que recibe el endpoint asignado para el modelo de churn, y a su vez el esquema que retorna ante una solicitud exitosa.

