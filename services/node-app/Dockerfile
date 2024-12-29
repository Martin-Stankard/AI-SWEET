# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and install dependencies (if any)
COPY ../../../src/node/package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Command to run the helloWorld.js file
CMD ["node", "src/node/helloWorld.js"]
