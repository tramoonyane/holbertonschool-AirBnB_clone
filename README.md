# AirBnB Clone - README
This repository contains the code for an AirBnB clone, which is a command-line interface (CLI) application. The AirBnB clone is a simplified version of the popular online accommodation marketplace, AirBnB.

## Command Interpreter
The command interpreter is a CLI that allows users to interact with the AirBnB clone. It provides a set of commands to manage and manipulate objects in the system. Users can create, update, delete, and retrieve objects, as well as perform various operations on them.

## How to Start the Command Interpreter
To start the command interpreter, follow these steps:

1. Clone the repository to your local machine:
```
$ git clone https://github.com/holbertonschool-AirBnB_clone.git
```
2.Navigate to the project directory:
```
$ cd holbertonschool-AirBnB_clone
```
3.Run the command interpreter:
```
$ ./console.py
```
## How to Use the Command Interpreter
Once the command interpreter is running, you can enter commands in the following format:
```
(hbnb) command [arguments]
```
Here, command represents the action you want to perform, and arguments are any additional parameters required by the command.

The command interpreter supports the following commands:

create - Create a new object
show - Display information about an object
destroy - Delete an object
all - Display information about all objects or objects of a specific class
update - Update the attributes of an object
You can get detailed information about each command by using the help command followed by the command name. For example:
```
(hbnb) help create
```
1.Examples
Here are a few examples of how to use the command interpreter:

Create a new User object:
```
(hbnb) create User
```
2.Show information about a specific object:
```
(hbnb) show User 1234-5678-9012
```
3.Delete an object:
```
(hbnb) destroy User 1234-5678-9012
```
4.Display information about all objects:
```
(hbnb) all
```
5.Update the attributes of an object:
```
(hbnb) update User 1234-5678-9012 email "user@example.com"
```
