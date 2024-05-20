import os
import shutil
import argparse
import logging
from datetime import datetime

def setup_logging(log_filename, verbose):
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename=log_filename, level=logging.DEBUG if verbose else logging.ERROR, format=log_format)

def log_error(source_file, destination_file, error_message):
    logging.error(f"Failed to copy '{source_file}' to '{destination_file}': {error_message}")

def log_info(source_file, destination_file):
    logging.info(f"Successfully copied '{source_file}' to '{destination_file}': SUCCESSFULLY COPIED")

def backup(source, destination, log_filename, verbose):
    setup_logging(log_filename, verbose)
    
    if not os.path.isdir(source):
        print(f"Source directory '{source}' does not exist")
        return
    
    if not os.path.exists(destination):
        try:
            os.makedirs(destination)
        except OSError as e:
            error_message = f"Error creating destination directory '{destination}': {e}"
            print(error_message)
            logging.error(error_message)
            return

    try:
        files = os.listdir(source)
    except OSError as e:
        error_message = f"Error listing files in source directory '{source}': {e}"
        print(error_message)
        logging.error(error_message)
        return
    
    for file_name in files:
        source_file = os.path.join(source, file_name)
        destination_file = os.path.join(destination, file_name)

        if os.path.isfile(source_file):
            try:
                shutil.copy2(source_file, destination_file)
                print(f"Copied '{source_file}' to '{destination_file}'")
                if verbose:
                    log_info(source_file, destination_file)
            except IOError as e: 
                error_message = f"Error copying '{source_file}' to '{destination_file}': {e}"
                print(error_message)
                log_error(source_file, destination_file, str(e))

def main():
    parser = argparse.ArgumentParser(description='Backup a directory to another directory')
    parser.add_argument('-s', '--source', required=True, help='Source Directory')
    parser.add_argument('-d', '--destination', required=True, help='Destination directory')
    parser.add_argument('-l', '--log', required=False, help='Log filename', default='backup.log')
    parser.add_argument('-v', '--verbose', action='store_true', help='Log successful copy operations')

    args = parser.parse_args()

    backup(args.source, args.destination, args.log, args.verbose)

if __name__ == "__main__":
    main()

