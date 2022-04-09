#!/usr/bin/env python3

#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
import  argparse
from urllib import request as url_request
from urllib import error as  url_error
import logging
import time

logging.basicConfig(level=logging.INFO)

def request_pwned(pass_phrase):
	'''
	calls pwnedpasswords on first 5 chars of SHA-1 hasehed string and returns all the mathces in the database
	
	:param pass_phrase: str of first 5 chars of SHA-1 hash of a str
	:return: List of matches with pass_phrase
	'''

	assert len(pass_phrase) >= 5, 'Provide at least first five characters of SHA-1 hash.'

	url = f'https://api.pwnedpasswords.com/range/{pass_phrase[:5]}'

	req = url_request.Request(
            url=url,
            headers={
                'User-Agent': "pwnedpasswords (Python)"
            }
        )
	
	try:
		
		with url_request.urlopen(req) as res:
			response = res.read().decode("utf-8-sig").upper()
			time.sleep(1)
	except url_error.HTTPError as e:
		logging.debug(f'Exception while calling pwned API: {e}')
		exit()
	
	return response.split('\r\n')


def check_pwned(pass_phrase, is_sha1=False):
	'''
	checks whether your password has been pwned

	:param pass_phrase: Plain-text or SHA-1 hashed pass-phrase
	:param is_sha1: whether pass phrase is SHA-1 hashed or not
	'''
	if not is_sha1:
		pass_phrase = hashlib.sha1(pass_phrase.encode("utf8")).hexdigest()
	
	pass_phrase = pass_phrase.upper()

	potential_matches = request_pwned(pass_phrase[:5])

	potential_matches = dict(match.split(':') for match in potential_matches)

	count = potential_matches.get(pass_phrase[5:], None)

	if count:
		logging.warning(f'Your password has been pwned {count} times. Change ASAP!!!')
	else:
		logging.info('Nice job!! Your passowrd is safe. Good luck remembering all those phrases and @#$%^&* :p')
	

if __name__ == '__main__':
	parser = argparse.ArgumentParser('PwnedPassword arguments')
	parser.add_argument('--pass-phrase', type=str, help='Plain text or SHA1 hashed password phrase to check if pwned')
	parser.add_argument('--is-sha1', action='store_true', help='Set this if pass-phrase is hashed with SHA-1' )

	args = parser.parse_args()

	check_pwned(args.pass_phrase, args.is_sha1)
	# print(url('range', args.pass_phrase))


