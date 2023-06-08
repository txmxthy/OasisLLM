import torch
from utilities.util import print_header, select
from ingestion import ingest_main
from oasis import oasis_main


def gpu_status():
    if torch.cuda.is_available():
        print(f"Cuda GPU: {torch.cuda.get_device_name(0)} is Available.")
    else:
        print("Cuda GPU Not Available.")
    input("Press Enter to continue...")


def configuration():
    """
    Present the current configuration for the model and ingestion process (Loaded from .env)
    Example parameters:
        - Model
        - Ingestion Directory
        - Number of files in ingestion directory
        - Chunk Size
        - Chunk Overlap
    :return:
    """
    pass


def main(first_run=None):
    """
    Main function for the Oasis Toolkit
    :return:
    """
    while True:
        if not first_run:
            # Clear the console
            print("\033[H\033[J")
        first_run = False
        print_header("The Oasis Toolkit")
        functions = {
            "Document Ingestion": ingest_main,
            "Query": oasis_main,
            "Config": configuration,
            "GPU Status": gpu_status,
        }
        # Call the select method and run the selected function
        choice = select([*functions.keys()])
        functions[choice]()


if __name__ == '__main__':
    main(first_run=True)
