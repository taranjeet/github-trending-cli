import os


def get_console_size():
    '''
    returns no of rows, no of cols
    '''
    with os.popen('stty size', 'r') as f:
        size = map(int, f.read().split())
    return size


def get_print_size_for_repo(data):
    name, lang, star = [0]*3
    for each in data:
        repo_name = each.get('repo_name')
        stars = each.get('stars')
        language = each.get('language')
        name = max(len(repo_name), name)
        lang = max(len(language), lang)
        star = max(len(stars), star)

    return {
        "NAME": name+1,
        "LANG": lang+1,
        "STAR": star+1,
        "IDX": 3,
    }


def get_print_size_for_dev(data):
    dev, repo = [0]*2
    for each in data:
        dev_name = each.get('dev_name')
        repo_name = each.get('repo_name')
        dev = max(len(dev_name), dev)
        repo = max(len(repo_name), repo)

    return {
        "DEV": dev+1,
        "REPO": repo+1,
        "IDX": 3,
    }


def get_color_code():
    return {
        "IDX": "white",
        "NAME": "yellow",
        "LANG": "red",
        "STARS": "green",
        "DESC": "blue",
        "REPO": "green",
    }
