import os
import shutil
import argparse

def backup(source, destination):
    if not os.path.isdir(source):
        print(f"Source directory '{source}' does not exist")
        return
    
    if not os.path.exists(destination):
        try:
            os.makedirs(destination)
        except OSError as e:
            print(f"Error creating destination directory '{destination}': {e}")
            return
        
    try:
        files = os.listdir(source)
    except OSError as e:
        print(f"Error listing files in source directory '{source}': {e}")
        return
    
    for file_name in files:
        source_file = os.path.join(source, file_name)
        destination_file = os.path.join(destination, file_name)

        if os.path.isfile(source_file):
            try:
                shutil.copy2(source_file, destination_file)
                print(f"Copied '{source_file}' to '{destination_file}'")
            except IOError as e: 
                print(f"Error copying '{source_file}' to '{destination_file}': {e}")

def main():
    parser = argparse.ArgumentParser(description='Backup a directory to another directory')
    parser.add_argument('-s', '--source', required = True, help = 'Source Directory')
    parser.add_argument('-d', '--destination', required = True, help = 'Destination directory')
    args = parser.parse_args()

    backup(args.source, args.destination)

if __name__ == "__main__":
    main()
