def calculate_score(keywords):
    present_count = len(keywords["present"])
    missing_count = len(keywords["missing"])
    total = present_count + missing_count
    
    if total == 0:
        return 0
    
    score = (present_count / total) * 100
    return min(100, round(score))