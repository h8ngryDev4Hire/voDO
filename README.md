# vooDO! Your Todo Task Manager

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-GPLv3-blue)](https://opensource.org/license/gpl-3-0)

vooDO! is a command-line utility for managing and tracking tasks using a simple TODO file format. It allows you to create, update, and mark tasks as completed, making it easy to stay organized and keep track of your pending tasks. It's not magic, it's vooDO!

## Inspiration

As a developer working on my personal projects, I find it often difficult to remember tasks that need to be done after a long day of coding. This led me down the path of creating vooDO, which I use for task tracking on my projects which has helped a lot in terms of centralizing my thoughts.


## Features

- Add new tasks with a title, status, and notes
- Update task status and notes interactively
- Mark tasks as completed
- Automatically generate and update a formatted TODO file
- Easy installation via a one-liner curl command

## Installation

To install Voodoo, simply run the following command in your terminal:

```bash
curl -sSL https://raw.githubusercontent.com/h8ngryDev4Hire/Voodoo/main/install.sh | bash
```

This command will download and execute the `install.sh` script, which will clone the Voodoo repository, install the necessary files, and make the `voodo` command available in your system.

## Usage

To use Voodoo, open your terminal and run the `voodo` command followed by the task title and any additional options:

```bash
voodo "review new NotificationManager class and apply error handling to notate.js using said class" -s 2 
```

### Options

- `-s, --status`: Specify the status of the task. Available options are:
 - `1`: To be determined
 - `2`: In progress
 - `3`: Blocked
- `-n, --notes`: Add additional notes to the task for better context.
- `-d, --delete-preexisting`: Delete the existing TODO file in the current working directory.
- `-i, --interactive`: Spawn an interactive session to update task status and notes. (CURRENTLY NOT FUNCTIONAL)

## TODO File Format

Voodoo creates and updates a TODO file named `TODO` in the current working directory. The file follows a simple tab-separated format with the following columns:

- `ID`: The unique identifier of the task.
- `TASK`: The title of the task.
- `TIME`: The timestamp of when the task was created or last updated.
- `STATUS`: The current status of the task.
- `NOTES`: Additional notes associated with the task.

Example:

```
ID      TASK                                                                                    TIME                    STATUS          NOTES
1       fix search bar tags not displaying correctly                                            2024-03-23 23:21:24     COMPLETED       N/A
2       review new NotificationManager class and apply error handling to notate.js using class  2024-03-25 12:49:03     in-progress     N/A

```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/h8ngryDev4Hire/Voodoo).

## License

This project is licensed under the [GPLv3 License](https://opensource.org/license/gpl-3-0).
