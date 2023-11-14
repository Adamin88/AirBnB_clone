# AirBnB Clone - The Console

![AirBnB Clone](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231114%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231114T144335Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5c045da501c3800a1728674a44ca9c0037951700671bf56d1d3599543af22609)

**Project:** 0x00. AirBNB Clone - The Console | **By:** Guillaume

**Weight:** 5 | **Project Duration:** Nov 6, 2023 4:00 AM - Nov 13, 2023 4:00 AM 

**Team Members:** Ayoub Baalla, Elhihi Mohamed

Welcome to the AirBnB Clone project! This project is the first step towards building a full web application that emulates the functionality of Airbnb. In this project, we are going to create a command-line interface (CLI) known as "The Console," which allows us to manage AirBnB objects using various commands.

## Table of Contents

- [Background Context](#background-context)
- [Installation](#installation)
- [Usage](#usage)  
- [Commands](#commands)
- [File Structure](#file-structure)
- [Contributors](#contributors)  
- [License](#license)

## Background Context

This project is designed to teach us various fundamental concepts in Python, including: 

- Python packages and modules
- Object-Oriented Programming (OOP)
- Creating a command-line interface (CLI)
- Serialization and deserialization of objects
- Unit testing using the `unittest` framework

The project aims to mimic the basic functionalities of Airbnb, focusing on creating classes to represent different elements of the application, managing object serialization and deserialization, and providing a command-line interface for interacting with the objects.

## Installation

1. Clone the repository:

`git clone https://github.com/MinightDev/AirBnB_clone`

2. Navigate to the project directory:

`cd AirBnB_clone`

3. Run the console:

`./console.py`

## Usage

Once the console is launched, you can start using various commands to manage your AirBnB objects. For a list of available commands, type `help` or `help <command>` to get more information about a specific command.

## Commands

The following commands are available in the console:

- `create`: Creates a new instance of a class and saves it to a JSON file.

- `show`: Displays the string representation of an instance.

- `destroy`: Deletes an instance based on the class name and ID.

- `all`: Displays all instances of a class or all instances in the storage.

- `update`: Updates the attributes of an instance.

For a complete list of available commands, refer to the console's built-in help feature.

## File Structure

The project file structure is organized as follows:

- `console.py`: The main command-line interface (CLI) script.

- `models/`: Directory containing class definitions for different AirBnB objects.

- `models/engine/`: Directory containing the storage engine implementation.

- `tests/`: Directory containing unit tests for the project.

## Contributors

- Ayoub Baalla (Team Member)

- Elhihi Mohamed (Team Member)

## License

This project is licensed under the [MIT License](LICENSE).
