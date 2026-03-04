"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[-1]

def convert_coordinate(coordinate):
    return tuple(coordinate)


def compare_records(rui_record, azara_record):
    rui_coordinate = rui_record[1]
    rui_number = rui_coordinate[:-1]
    rui_letter = rui_coordinate[-1].upper()
    azara_number = azara_record[1][0]
    azara_letter = azara_record[1][1].upper()
    return (rui_number, rui_letter) == (azara_number, azara_letter)

def create_record(azara_record, rui_record):
    azara_coordinate = azara_record[1]
    azara_number = azara_coordinate[:-1]
    azara_letter = azara_coordinate[-1].upper()
    rui_number, rui_letter = rui_record[1]
    rui_letter = rui_letter.upper()
    if (azara_number, azara_letter) == (rui_number, rui_letter):
        return (azara_record[0],azara_record[1],rui_record[0],rui_record[1],rui_record[2])
    return "not a match"


def clean_up(combined_records):
    report = ""
    for record in combined_records:
        treasure = record[0]
        location = record[2]
        coordinate = record[3]
        quadrant = record[4]
        cleaned_record = (treasure, location, coordinate, quadrant)
        report += str(cleaned_record) + "\n"
    return report
