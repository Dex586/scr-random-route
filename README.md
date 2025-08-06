# SCR Train Randomizer

This project is a simple desktop application that allows users to generate a random train route for the game Stepford County Railway (SCR). Users can select a train operator, and the application will randomly pick a train and a start and end station for that operator.

## Features

-   Select from a list of SCR train operators.
-   Generate a random train for the selected operator.
-   Generate a random route with a starting and ending station.
-   Simple and easy-to-use graphical user interface (GUI).

## Getting Started

### Prerequisites

-   Python 3.x
-   Tkinter (usually included with Python)

### Running the Application

1.  **Clone the repository:**
    ```bash
    git clonehttps://github.com/Dex586/scr-random-route
    cd scr-random-route
    ```

2.  **Run the application:**
    ```bash
    python3 main.py
    ```

## Project Structure

```
.
├── data
│   ├── operators.py
│   ├── stations_by_op.py
│   └── trains.py
├── main.py
└── README.md
```

### File Descriptions

-   **`main.py`**: The main entry point for the application. It creates the GUI using `tkinter` and handles the logic for generating random routes.
-   **`data/operators.py`**: Contains a list of the available train operators in SCR.
-   **`data/stations_by_op.py`**: Defines the stations served by each train operator.
-   **`data/trains.py`**: Lists the trains available for each operator.
-   **`README.md`**: This file, providing an overview of the project.
