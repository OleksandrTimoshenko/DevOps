FROM nginx
COPY ./load-balancer.conf /etc/nginx/conf.d/load-balancer.conf
RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.disabled
CMD ["nginx", "-g", "daemon off;"]
EXPOSE 80 443 22