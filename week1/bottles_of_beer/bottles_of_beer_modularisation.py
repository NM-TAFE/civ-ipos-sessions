import time


def _get_correct_plural_verse(count):
    """
    Generate the appropriate verse for a given bottle count, handling pluralization.

    Args:
        count (int): The number of bottles.

    Returns:
        str: The appropriate verse for the given bottle count.
    """
    return f"{count} bottle{'s' if count != 1 else ''} of beer"


def _sing_verse(bottle_count, pause):
    """
    Sing one verse of the '99 bottles of beer' song, with a pause in the middle and end.

    Args:
        bottle_count (int): The number of bottles for this verse.
        pause (int): The length of time to pause.

    Side Effects:
        This function will cause the program to pause twice, once after printing each line of the verse.
    """
    bottle_text = _get_correct_plural_verse(bottle_count)
    next_bottle_text = _get_correct_plural_verse(bottle_count - 1)
    print(f"{bottle_text} on the wall, {bottle_text}.")
    time.sleep(pause)
    print(f"Take one down, pass it around, {next_bottle_text} on the wall.\n")
    time.sleep(pause + 1)  # Longer pause between verses


def sing_bottles_of_beer(count=99, pause=2):
    """
    Sing the '99 bottles of beer' song, with a pause between verses.

    Args:
        count (int): The number of bottles to start with (default is 99).
        pause (int): The base timing between and within verses (default is 2 seconds).
    """
    for bottle_count in range(count, 0, -1):
        _sing_verse(bottle_count, pause)


sing_bottles_of_beer(99)
