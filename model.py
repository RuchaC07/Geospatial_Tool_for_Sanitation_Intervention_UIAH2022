def model(density):
    if density<1000:
        return "Dewats"
    elif density < 8000:
        return "Sewerage"
    else:
        return "FSM"
