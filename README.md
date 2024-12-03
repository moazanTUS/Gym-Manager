# Gym-Manager
Description
A Python application designed to help gym enthusiasts track their exercises and calculate key metrics like one-rep max. This project incorporates object-oriented programming principles to ensure a scalable and maintainable design. It features a graphical user interface (GUI) built using PyQt5, providing an interactive way to manage gym routines.

Features
Exercise Tracking:
Record weights and repetitions for exercises like Squat and Bench.
Automatically calculate one-rep max based on user inputs.
Graphical User Interface:
User-friendly interface built with PyQt5.
Interactive layout designed using Qt Designer.

Extendable and Modular:
Object-oriented design allows easy addition of new features or exercises.
Key OOP Concepts
Polymorphism:
The Exercise base class defines a generic calculate_one_rep_max() method.
Subclasses like Squat and Bench override this method to provide specific calculations.

Inheritance:
Classes like Squat and Bench inherit from the Exercise base class, reusing its attributes and methods.

Encapsulation:
Attributes like weight and reps are encapsulated within the Exercise class.

Modularity:
The project separates GUI (gym_gui.py) from the core logic (gymmanagerapp.py), ensuring better maintainability.

Technologies Used
Python: Core programming logic and object-oriented design.
PyQt5: GUI development.
Qt Designer: GUI layout creation and customization.
Virtual Environment: Isolated dependency management


Files in This Repository
gymmanagerapp.py:
Contains the main application logic.
Implements exercise tracking and core computations.
Integrates with the GUI file for seamless interaction.

gym_gui.py:
Auto-generated PyQt5 GUI file from a .ui layout.
Contains the graphical user interface for the application
