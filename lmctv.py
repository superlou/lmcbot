def determine_watch_method(msg):
    cablevision_keywords = ['cablevision', 'altice', 'optimum']
    verizon_keywords = ['verizon', 'fios']
    online_keywords = ['online', 'site', 'web', 'internet', 'net']
    roku_keywords = ['roku']
    youtube_keywords = ['youtube']

    msg = msg.lower()

    source = None
    channel = None

    if any(keyword in msg for keyword in youtube_keywords):
        source = 'youtube'

    if any(keyword in msg for keyword in cablevision_keywords):
        source = 'cablevision'

    if any(keyword in msg for keyword in verizon_keywords):
        source = 'verizon'

    if '75' in msg:
        source = 'cablevision'
        channel = 75
    elif '76' in msg:
        source = 'cablevision'
        channel = 76
    elif '77' in msg:
        source = 'cablevision'
        channel = 77
    elif '34' in msg:
        source = 'verizon'
        channel = 34
    elif '35' in msg:
        source = 'verizon'
        channel = 35
    elif '36' in msg:
        source = 'verizon'
        channel = 36
    elif any(keyword in msg for keyword in online_keywords):
        source = 'online'
    elif any(keyword in msg for keyword in roku_keywords):
        source = 'roku'

    return source, channel
