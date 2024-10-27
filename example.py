from m3u8_validator import is_valid_m3u8

link = "http://example.com/playlist.m3u8"
is_secure = True
timeout = 5

if is_valid_m3u8(link, timeout=timeout, secure=is_secure):
    print("The link is a valid M3U8.")
else:
    print("The link is not a valid M3U8.")
