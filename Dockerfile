# Use the official Node.js image from the Docker Hub
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install the required packages
RUN npm install

# Copy the entire application code to the container
COPY . .

# Build the application
RUN npm run build

# Install a lightweight server to serve the built app
RUN npm install -g serve

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["serve", "-s", "build"]
