import sys
import requests
import time

CONF = {
    'twitch_id': '110503727',
    'client_id': '1l4mskyv7v4oymg0pnv5oreqplccwd',
    'token_url': 'https://api.twitch.tv/kraken/streams/',
    'sleep_seconds': 6,
}


def req_twitch_json(url, client_id):
    try:
        headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers)
        return r.json()
    except Exception:
        return None


if __name__ == '__main__':
    try:
        twitch_stream_url = CONF['token_url'] + CONF['twitch_id']
        while True:
            stream = req_twitch_json(twitch_stream_url, CONF['client_id'])
            if stream:
                message = '\rCurrent Viewers: {}  '.format(stream['stream']['viewers'])
            else:
                message = '\rStream offline.      '
            print(message, end='')
            time.sleep(CONF['sleep_seconds'])
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)
    except Exception as error:
        print('\nCaught Exception: {}'.format(error))
        input('\n\nYou may close this window or press <enter> to exit...\n')
        sys.exit(1)
