def ft_tqdm(lst: range) -> None:
    """This function is a progress bar for a loop.
:param lst: range
:return: None"""

    load = [' ', '█']

    line_len = 70
    for elem in lst:
        if elem % 7 == 0 or elem >= len(lst) - 7:
            print(f"\r{format(elem / len(lst) * 100,'>3.0f')}%|"
                  f"{round(elem / len(lst) * line_len) * load[1]}"
                  f"{round((len(lst) - elem) / len(lst) * line_len) * load[0]}"
                  f"| {elem + 1}/{len(lst)}", end="")
        yield elem
