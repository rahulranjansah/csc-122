# """
#    *
#    * Id factory Class
#    *
#    * @author Rahul Ranjan Sah
#    * @date   02/12/2025
# """

def extract_valid_lines(contents : list[str]) -> list[str]:
    """
    Start of actual parsing of the playback file:
        (1) Remove comments (#)
        (2) Return all lines of valid, non-commented text.
    """
    # Read line by line, ignore comments
    # Result is a list of lines (strings with text)
    filtered = []
    for line in contents:

        line = line.split("#")[0].strip()
        if line:
            filtered.append(line)

    return filtered

