# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only package files first (to leverage caching)
COPY package*.json ./

# Install dependencies
RUN npm install

# Install nodemon globally for live-reloading
RUN npm install -g nodemon

# Copy the rest of the application code
COPY . .

# Expose the application port (if needed)
EXPOSE 3000

# Command to run the application with nodemon
CMD ["nodemon", "src/node/tester.js"]
