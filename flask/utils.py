


def validate_onionlink(long_url):
    if '.onion' not in long_url:
        return False
    if long_url