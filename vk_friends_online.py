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
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends'
        )
        api = vk.API(session)
        online_id_list = api.friends.getOnline()
        friends_online = dict.fromkeys(online_id_list)

        for friend_id in friends_online.keys():
            friend_name = api.users.get(user_id=friend_id)[0]
            friends_online[friend_id] = friend_name['first_name'] + ' ' +\
                                        friend_name['last_name']
        return friends_online

    except vk.exceptions.VkAuthError:
        return 'VkAuthError'


def output_friends_to_console(friends_online):
    if not friends_online:
        print('Nobody is online at the moment')
    else:
        print('Friends online: ')
        for friend_name in friends_online.values():
            print('{}'.format(friend_name))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    if not (friends_online == 'VkAuthError'):
        output_friends_to_console(friends_online)
