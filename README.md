# Desplegar en local 
## Instalar python 3.8.5
```
uv python install 3.8.5
```
## Usar la version de python instalada
```
uv pin 3.8.5
```
## Ir al directorio app
```
cd tls-simulation/app 
```
## Crear entorno virtual
```
uv venv
```
### Activar entorno virtual
```
source .venv/bin/activate
```
## Instalar paquetes
```
uv pip install -r pyproject.toml
```
## Inicializar API
```
gunicorn --bind 0.0.0.0:5000 app:app
```

# Realizar prubas directas
Aqui vamos a realizar pruebas directas sin utilizar NGINX.
```
openssl s_client -connect localhost:5000 -tls1
curl localhost:5000/health
curl localhost:5000/api/v1/handshake-info
curl localhost:5000/api/v1/data
```

# Crear ceritificados autofirmados
```
cd tls-simulation/
mkdir -p nginx/certs
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout nginx/certs/server.key \
  -out nginx/certs/server.crt \
  -subj "/CN=localhost"
```

# Desplegar con docker compose
## Ir al directorio raiz 
```
cd tls-simulation/
```
## Construir imagenes y desplegar contenedores
```
docker compose up -d --build
```
### Verificar que se crearon los contenedores
```
docker compose ps 
```
### Ingresar al contenedor nginx 
```
docker exec -it nginx sh 
tail -f /var/log/nginx/access.log
```
### Ingresamos al contenedor nginx desde otra terminal
```
docker exec -it nginx sh 
tail -f /var/log/nginx/error.log 
```
```
```
## Realizar las pruebas desde VM Bionic
### Ir al directorio
```
cd bionic 
vagrant up
```
Realizamos las pruebas desde esta maquina virtual porque \
tiene todos los requisitos necesarios para las pruebas.
### Ingresar a VM 
```
vagrant ssh 
```
## Ejecutar pruebas 
### Simular Handshake TLSv 1.0 con openssl s_client
Debe cambiar la IP por la de su HOST 
```
openssl s_client -connect 192.168.0.5:443 -tls1
```
### Simular Handshake TLSv 1.1 con curl
```
curl -v --tlsv1.1 --tls-max 1.1 -k https://192.168.0.5/api/v1/handshake-info
```
::::Respuesta::::
```
{
  "client_ip": "172.18.0.1",
  "cipher_used": "ECDHE-RSA-AES256-SHA",
  "protocol_used": "TLSv1.1"
}
```
### Probar rechazo de TLS 1.2 / TLS 1.3 (Simulacion de fallo)
```
curl -v --tlsv1.2 --tls-max 1.2 -k https://192.168.0.5/health
```

# Detener contenedores y eliminar volumen
```
docker compose down -v 
```

