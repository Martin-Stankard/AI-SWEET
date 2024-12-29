# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the package.json and install dependencies (if any)
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Command to run the Node.js file
CMD ["node", "src/node/tester.js"]
