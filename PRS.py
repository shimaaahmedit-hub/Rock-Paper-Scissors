def player(prev_play, opponent_history=[]):
    # Save opponent history
    if prev_play:
        opponent_history.append(prev_play)

    # First move
    if not opponent_history:
        return "R"

    # Helper to beat a move
    def beat(move):
        if move == "R": return "P"
        if move == "P": return "S"
        if move == "S": return "R"

    # --- Strategy 1: Detect repeating patterns (like quincy) ---
    pattern_length = 3
    if len(opponent_history) > pattern_length:
        recent = opponent_history[-pattern_length:]
        for i in range(len(opponent_history) - pattern_length):
            if opponent_history[i:i+pattern_length] == recent:
                predicted = opponent_history[i+pattern_length]  # next move in pattern
                return beat(predicted)

    # --- Strategy 2: If opponent repeats their own last move (like kris) ---
    if len(opponent_history) >= 2 and opponent_history[-1] == opponent_history[-2]:
        return beat(opponent_history[-1])

    # --- Strategy 3: If opponent mirrors us (like abbey) ---
    # If opponent plays what we played last time → counter it
    if len(opponent_history) >= 2:
        # If opponent copied our previous move
        # (we don't store our own history, but we can infer)
        pass  # FCC bots don't require explicit self-history

    # --- Strategy 4: Default counter (works well vs mrugesh) ---
    predicted = opponent_history[-1]
    return beat(predicted)
