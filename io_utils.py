def read_file_as_non_empty_stripped_list(f):
    lines = f.readlines()
    lines_stream = map(lambda u: u.strip(), lines)
    lines_stream = filter(lambda u: u, lines_stream)
    lines = list(lines_stream)
    return lines
