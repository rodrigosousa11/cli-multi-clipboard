# CLI Multi-Clipboard

This is a simple Python clipboard manager that allows you to store more than one element copied and load copied elements back to clipboard using command-line commands. It uses a JSON file to store the copied data.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository or download the `main.py` file.
2. Install the required dependencies by running the following command:

```md
pip install clipboard
```

3. Run the program using the following command:

```md
python main.py
```

## Usage

The program supports the following commands:

- `save`: Save the currently copied data with a specified name associated.
- `load`: Load a previously saved data by its name and copy it to the clipboard automatically.
- `list`: List all the saved data with their corresponding names.
- `delete`: Delete all the saved data.

When running the program, you can either provide a command as a command-line argument (e.g., `python main.py save`) or leave it empty and enter the command when prompted.

## File Structure

- `main.py`: The main Python script containing the clipboard manager implementation.
- `clipboard.json`: The JSON file used to store the copied data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
