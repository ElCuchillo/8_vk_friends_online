import getpass
import vk

APP_ID = 6241824


def get_user_login():
    login = input('Login: ')
    return login


def get_user_password():
    password = getpass.getpass()
    return password


def get_online_friends(login, password):
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends'
        )
        api = vk.API(session)
        friends_online_ids = api.friends.getOnline()
        if friends_online_ids:
            friends_online = api.users.get(user_ids=friends_online_ids)
        else:
            friends_online = []
        return friends_online


def output_friends_to_console(friends_online):
    if not friends_online:
        print('Nobody is online at the moment')
    else:
        print('Friends online: ')
        for friend in friends_online:
            print('{} {}'.
                  format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        pass
