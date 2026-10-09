FROM nginx:1.30-alpine

# Copiar configuraciones y certificados
COPY nginx.conf /etc/nginx/nginx.conf
COPY certs/ /etc/nginx/certs/
RUN rm -f /var/log/nginx/access.log /var/log/nginx/error.log 

EXPOSE 443
