def resistor_label(colors):
    color_values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }

    tolerance_values = {
        "grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%",
        "green": "±0.5%", "brown": "±1%", "red": "±2%",
        "gold": "±5%", "silver": "±10%"
    }

    # 1-band resistor
    if len(colors) == 1:
        return "0 ohms"

    # 4-band resistor
    if len(colors) == 4:
        value = int(str(color_values[colors[0]]) + str(color_values[colors[1]]))
        multiplier = 10 ** color_values[colors[2]]
        tolerance = tolerance_values[colors[3]]

    # 5-band resistor
    elif len(colors) == 5:
        value = int(
            str(color_values[colors[0]]) +
            str(color_values[colors[1]]) +
            str(color_values[colors[2]])
        )
        multiplier = 10 ** color_values[colors[3]]
        tolerance = tolerance_values[colors[4]]

    total = value * multiplier

    # Convert to readable unit
    if total >= 1_000_000_000:
        value = total / 1_000_000_000
        unit = "gigaohms"
    elif total >= 1_000_000:
        value = total / 1_000_000
        unit = "megaohms"
    elif total >= 1_000:
        value = total / 1_000
        unit = "kiloohms"
    else:
        value = total
        unit = "ohms"

    # Format number (remove .0, keep decimals like 2.54)
    if isinstance(value, float):
        if value.is_integer():
            value = int(value)
        else:
            value = round(value, 2)

    return f"{value} {unit} {tolerance}"