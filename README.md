*Task Manager*

**Overview**

The Task Manager project is a simple console-based application demonstrating the use of Singleton and Factory design patterns in Python. This project showcases object-oriented programming, software design principles, and design patterns, making it a great addition to any developer’s portfolio.

**Project Structure**

The Task Manager application includes the following features:

	1.	Singleton Pattern: Ensures there is only one instance of the TaskManager throughout the application, managing all tasks from a single point.
	2.	Factory Pattern: Dynamically creates different types of tasks using a Factory class, demonstrating polymorphism and clean code practices.

**Process**

	1.	Implemented the Singleton Pattern:
	•	Created a TaskManager class that follows the Singleton design pattern, ensuring a single instance to manage tasks. This prevents multiple instances of task managers from being created and causing inconsistencies.
	2.	Created Different Task Types Using the Factory Pattern:
	•	Developed a Task base class, and implemented two different task types—SimpleTask and TimedTask. Each task type has unique behavior and methods.
	•	Utilized the Factory pattern to create tasks dynamically at runtime without specifying their concrete class.
	3.	Integrated and Managed Tasks:
	•	Integrated the TaskManager with TaskFactory to add, list, and manage tasks. This central management system allows tasks to be added dynamically and handled efficiently.
	4.	Tested and Verified the Functionality:
	•	Implemented a script to test the application by creating tasks, adding them to the manager, marking them as complete, and listing their statuses. This script ensures that the application behaves as expected.

The Task Manager project successfully demonstrates the practical application of two fundamental design patterns, resulting in a robust, maintainable, and extensible application. It provides a valuable learning experience in object-oriented design, software architecture, and code modularity.

This project is a fully functional task manager application with core functionalities and can be further expanded to include additional features such as priority management, deadlines, and user interfaces.

**Libraries Used**

Time, ABC
