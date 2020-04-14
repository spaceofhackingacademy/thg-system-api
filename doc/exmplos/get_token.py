# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    get_token.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: darkcode357 <darkcode357@gmail.com>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/12 19:11:46 by darkcode357       #+#    #+#              #
#    Updated: 2020/04/12 19:23:41 by darkcode357      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
API_URL = 'http://127.0.0.1:5000/'
login = requests.get('http://127.0.0.1:5000/login', auth=('user', 'password'))
jsonlogin = login.json()
for token, key in jsonlogin.items():
    pass
print("voce tem que usar o token desse jeito aqui\nsua rota?token={}".format(key))

