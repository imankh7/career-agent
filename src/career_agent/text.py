def normalize_title(title: str) -> str:
    s_title = title.lower()
    title_list = s_title.split()
    normal_title = " ".join(title_list)
    return normal_title
