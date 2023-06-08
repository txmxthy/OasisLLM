import os


def list_models(local_only=False):
    """
    List the models we have set up with the project
    :param local_only: Only list models in the local directory
    :return:
    """
    models = {
        "hkunlp/instructor-xl": "HKU NLP Instructor XL",
        "TheBloke/vicuna-7B-1.1-HF": "Vicuna 7B 1.1 HF",
        "mayaeary/pygmalion-6b_dev-4bit-128g": "Pygmalion 6B Dev 4bit 128g",
        "TheBloke/wizardLM-7B-GPTQ": "WizardLM 7B GPTQ",
    }

    if local_only:
        # Check which models are available locally
        local_models = []
        # @TODO Implement
    return models


def select(options):
    """
    Enumerate a set of options to allow for selection via CLI
    :param options: dict of options to functions/string etc
    :return: Selected option
    """
    for i, option in enumerate(options):
        print(f"{i}: {option}")
    while True:
        try:
            selection = int(input("Select an option: "))
            if selection in range(len(options)):
                selected = options[selection]
                print(f"Selected {selected}")
                return selected
            else:
                print("Invalid selection")
        except ValueError:
            print("Invalid selection")


def print_header(heading, sep="=", pad=" "):
    """
    Print a centered heading
    :param heading:
    :param sep: heading lines
    :param pad: heading spacer
    :return:
    """

    try:
        width = os.get_terminal_size().columns
    except OSError:  # When running from ide
        width = 80

    # Center
    print(width * sep)
    print(heading.center(width, pad))
    print(width * sep)
