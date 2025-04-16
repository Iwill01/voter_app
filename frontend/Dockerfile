# Use official Nginx base image
FROM nginx:alpine

# Remove default nginx page
RUN rm -rf /usr/share/nginx/html/*

# Copy frontend files to nginx public folder
COPY . /usr/share/nginx/html

# Expose port 80 for HTTP
EXPOSE 80

# Nginx automatically starts
