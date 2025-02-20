# TMX to CSV Converter

## Description

This Python script automates the process of converting Translation Memory eXchange (TMX) files compressed in .gz format to CSV files. It's designed to handle English-Khmer language pairs, extracting source (English) and target (Khmer) sentences from TMX files and saving them in a structured CSV format.

## Features

- Decompresses .tmx.gz files
- Converts TMX files to CSV format
- Handles UTF-8 encoding with BOM
- Processes all .tmx.gz files in a specified folder
- Creates a separate output folder for CSV files

## Requirements

- Python 3.x
- No external libraries required (uses only built-in Python modules)

## Usage

1. Place the script in the same directory as your .tmx.gz files.
2. Run the script:
```bash
   python main.py
   ```

3. The script will:
- Decompress all .tmx.gz files in the current directory
- Convert each TMX file to a CSV file
- Save the CSV files in a new folder named "csv_output"

## Functions

### `decompress_gz(file_path, output_path)`
Decompresses a .gz file to a .tmx file.

### `tmx_to_csv(tmx_file, output_file)`
Converts a TMX file to a CSV file with proper UTF-8 encoding.

### `process_all_tmx_gz_in_folder(folder_path, output_folder)`
Processes all .tmx.gz files in a folder and converts them to CSV in an output folder.

## Output

- CSV files will be created in the "csv_output" folder
- Each CSV file will contain two columns: "Source" (English) and "Target" (Khmer)

## Note

This script assumes that the source language is English ('en') and the target language is Khmer ('km'). If you need to process different language pairs, modify the language codes in the `tmx_to_csv` function.

## Author

[Chealyfey Vutha]

## License

Here's a simple paragraph for the license section in your README file:

## License

This project is licensed under the MIT License. The MIT License is a permissive open-source license that allows for free use, modification, and distribution of the software, both for commercial and non-commercial purposes. It provides users with extensive freedoms while requiring only that the original copyright notice and license terms be included in any substantial portions of the software. For more details, please see the [LICENSE](https://github.com/lyfeyvutha/tmx-to-csv-converter/blob/main/LICENSE) file in this repository or visit [opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).

