def get_posostoive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please provide a posotive number")  
                continue
            return value
        except ValueError:
            print("invalid Input")

def get_choice(prompt, valid_options):
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_options:
            return choice
        print(f"Please enter a valid opition From the list:  {','.join(valid_options)}")

def get_description(prompt ="Enter Description "):
    while True:
        desc = input(prompt.strip())

        if desc:
            return desc
        print("Description cannot be empty, Please enter a valid description")

    