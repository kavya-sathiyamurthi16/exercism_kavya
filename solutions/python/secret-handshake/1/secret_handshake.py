def commands(binary_str):
    num = int(binary_str, 2)
    actions = []

    if num & 1:  
        actions.append("wink")
    if num & 2:   
        actions.append("double blink")
    if num & 4:   
        actions.append("close your eyes")
    if num & 8:   
        actions.append("jump")
    if num & 16:  
        actions.reverse()

    return actions