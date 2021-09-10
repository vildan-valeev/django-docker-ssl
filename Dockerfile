FROM nginx:latest
RUN mkdir /app
COPY /public /app

RUN rm /etc/nginx/conf.d/default.conf
COPY data/nginx/nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080 80 443
CMD ["nginx", "-g", "daemon off;"]
