import os

def run(event, context):
    os.environ['CONFIG_FILE_PATH'] = '/tmp/config.txt'
    with open(os.environ['CONFIG_FILE_PATH'], mode='w') as f:
        f.write(os.environ['CONFIG_TXT'])

    from splatnet2statink.splatnet2statink import check_for_updates, populate_battles
    if check_for_updates():
        return
    populate_battles(
        False, # is_s
        False, # is_t
        True,  # is_r
        False  # debug
    )
