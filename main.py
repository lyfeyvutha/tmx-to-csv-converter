import os
import csv
import gzip
from xml.etree import ElementTree as ET

def decompress_gz(file_path, output_path):
    """
    Decompresses a .gz file to a .tmx file.
    
    Parameters:
        file_path (str): Path to the .gz file.
        output_path (str): Path to save the decompressed .tmx file.
    """
    with gzip.open(file_path, 'rb') as gz_file:
        with open(output_path, 'wb') as tmx_file:
            tmx_file.write(gz_file.read())

def tmx_to_csv(tmx_file, output_file):
    """
    Converts a TMX file to a CSV file with proper UTF-8 encoding.
    
    Parameters:
        tmx_file (str): Path to the TMX file.
        output_file (str): Path to the output CSV file.
    """
    # Parse the TMX file
    tree = ET.parse(tmx_file)
    root = tree.getroot()

    # Define the XML namespace for TMX files
    namespace = {'xml': 'http://www.w3.org/XML/1998/namespace'}

    # Open the CSV file for writing with UTF-8 BOM encoding
    with open(output_file, mode='w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Source', 'Target'])  # Write the header row

        # Iterate through translation units in the TMX file
        for tu in root.findall('.//tu'):
            source = None
            target = None

            # Extract source and target text from <tuv> elements
            for tuv in tu.findall('./tuv'):
                lang = tuv.attrib.get(f'{{{namespace["xml"]}}}lang')
                seg = tuv.find('./seg').text if tuv.find('./seg') is not None else ''

                if lang == 'en':  # English (source language)
                    source = seg
                elif lang == 'km':  # Khmer (target language)
                    target = seg

            # Write the sentence pair to the CSV if both are present
            if source and target:
                writer.writerow([source, target])

def process_all_tmx_gz_in_folder(folder_path, output_folder):
    """
    Processes all .tmx.gz files in a folder and converts them to CSV in an output folder.
    
    Parameters:
        folder_path (str): Path to the folder containing .tmx.gz files.
        output_folder (str): Path to store the resulting CSV files.
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith('.tmx.gz'):
            gz_file_path = os.path.join(folder_path, filename)
            tmx_file_name = os.path.splitext(filename)[0] + ".tmx"
            tmx_file_path = os.path.join(folder_path, tmx_file_name)
            csv_file_name = os.path.splitext(filename)[0] + ".csv"
            csv_file_path = os.path.join(output_folder, csv_file_name)

            print(f"Decompressing {filename}...")
            decompress_gz(gz_file_path, tmx_file_path)

            print(f"Converting {os.path.basename(tmx_file_path)} to {os.path.basename(csv_file_path)}...")
            tmx_to_csv(tmx_file_path, csv_file_path)

            print(f"Conversion complete: {csv_file_path}")

if __name__ == "__main__":
    # Specify the folder containing .tmx.gz files
    input_folder = os.getcwd()  # Current working directory
    output_folder = os.path.join(input_folder, "csv_output")  # Output folder named "csv_output"

    print("Starting conversion of all .tmx.gz files in folder...")
    process_all_tmx_gz_in_folder(input_folder, output_folder)
    print("All conversions completed!")
