def label(colors):
    color_map = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6,
        "violet": 7, "grey": 8, "white": 9
    }
    first = color_map[colors[0]]
    second = color_map[colors[1]]
    base_value = int(f"{first}{second}")
    multiplier = 10 ** color_map[colors[2]]
    resistance = base_value * multiplier
    if resistance >= 1_000_000_000:
        return f"{resistance // 1_000_000_000} gigaohms"
    elif resistance >= 1_000_000:
        return f"{resistance // 1_000_000} megaohms"
    elif resistance >= 1_000:
        return f"{resistance // 1_000} kiloohms"
    else:
        return f"{resistance} ohms"