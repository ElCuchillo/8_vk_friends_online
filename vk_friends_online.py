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
        )
        api = vk.API(session)

        friends_online = [[friends_data['first_name'],
                           friends_data['last_name']]
                          for friends_data in api.friends.get(fields='online')
                          if friends_data['online']]

        return friends_online

    except vk.exceptions.VkAuthError:
        return 'VkAuthError'


def output_friends_to_console(friends_online):
    if not friends_online:
        print('Nobody is online at the moment')
    else:
        print('Friends online: ')
        for friend_name in friends_online:
            print('{} {}'.format(friend_name[0], friend_name[1]))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    if not (friends_online == 'VkAuthError'):
        output_friends_to_console(friends_online)
