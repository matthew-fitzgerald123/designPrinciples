# Task Manager Project
design principles project

The Task Manager project is a simple console-based application demonstrating the use of Singleton and Factory design patterns in Python.

**Process**

	1.	Implemented the Singleton Pattern: Created a TaskManager class that follows the Singleton design pattern, ensuring a single instance to manage tasks. 
 		This prevents multiple instances of task managers from 	being created and causing inconsistencies.
	2.	Created Different Task Types Using the Factory Pattern:Developed a Task base class, and implemented two different task types—SimpleTask and TimedTask. 
 		Each task type has unique behavior and methods. Utilized the Factory pattern to create tasks dynamically at runtime without specifying their concrete class.
	3.	Integrated and Managed Tasks: Integrated the TaskManager with TaskFactory to add, list, and manage tasks. This central management system allows tasks to be 
 		added dynamically and handled efficiently.
	4.	Tested and Verified the Functionality: Implemented a script to test the application by creating tasks, adding them to the manager, marking them as complete, 
 		and listing their statuses. This script ensures that the application behaves as expected.

**Libraries Used:**
Time, ABC
