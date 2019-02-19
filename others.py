def avg(lst):
    return round(sum(lst) / len(lst), 2)

def avg_labeled(lbl, lst):
    return (lbl, round(sum(lst) / len(lst), 2))