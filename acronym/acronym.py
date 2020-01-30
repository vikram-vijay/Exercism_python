def abbreviate(words):
    return "".join([j for j in words.replace("'", "").title() if j.isupper()])
