FROM node:16-alpine
ADD front-build /app/front-build
WORKDIR /app
RUN npm install serve -g
EXPOSE 3001
CMD ["serve", "-s", "front-build", "-p", "3001"]
