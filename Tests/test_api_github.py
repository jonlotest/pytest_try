import requests
from config import SECOND_SITE

resp = requests.get(SECOND_SITE)
print(resp.json())
var = {
    'meta': {
        'pagination': {
            'total': 3771,
            'pages': 378,
            'page': 1,
            'limit': 10,
            'links': {
                'previous': None,
                'current': 'https://gorest.co.in/public/v1/users?page=1',
                'next': 'https://gorest.co.in/public/v1/users?page=2'
            }
        }
    },
    'data': [
        {'id': 3843, 'name': 'Dr. Deeptendu Chattopadhyay', 'email': 'dr_deeptendu_chattopadhyay@wyman-gerlach.com',
         'gender': 'male', 'status': 'active'},
        {'id': 3842, 'name': 'Kailash Naik', 'email': 'naik_kailash@hand-vonrueden.net', 'gender': 'male',
         'status': 'active'},
        {'id': 3841, 'name': 'Mandakini Butt', 'email': 'butt_mandakini@moore-wilderman.org', 'gender': 'male',
         'status': 'active'},
        {'id': 3840, 'name': 'Chaanakya Chaturvedi', 'email': 'chaanakya_chaturvedi@marquardt.net', 'gender': 'male',
         'status': 'inactive'},
        {'id': 3839, 'name': 'Chandani Khatri Jr.', 'email': 'jr_khatri_chandani@collier-goyette.biz',
         'gender': 'female',
         'status': 'inactive'},
        {'id': 3838, 'name': 'Nimit Asan', 'email': 'asan_nimit@becker.com', 'gender': 'female', 'status': 'inactive'},
        {'id': 3837, 'name': 'Bhupen Johar Jr.', 'email': 'johar_jr_bhupen@kozey.name', 'gender': 'female',
         'status': 'active'},
        {'id': 3832, 'name': 'Bela Nayar MD', 'email': 'md_bela_nayar@koch.com', 'gender': 'female',
         'status': 'active'},
        {'id': 3831, 'name': 'Bhavani Dhawan', 'email': 'dhawan_bhavani@barton-blanda.co', 'gender': 'female',
         'status': 'inactive'},
        {'id': 3830, 'name': 'Anala Asan', 'email': 'anala_asan@davis.biz', 'gender': 'female', 'status': 'active'}]}
