# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Install Vite globally
RUN npm install -g vite

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port that Vite will use
EXPOSE 8080 

# Command to run Vite in development mode
CMD ["npm", "run", "dev"]
