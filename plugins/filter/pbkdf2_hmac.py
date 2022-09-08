# (c) 2022, Guido Grazioli <ggraziol@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import base64
import sys
import hashlib


def pbkdf2_hmac(string, hexsalt, iterations=1024):
    key = hashlib.pbkdf2_hmac(
        hash_name='sha1',
        password=str.encode(string),
        salt=bytearray.fromhex(hexsalt),
        iterations=iterations,
        dklen=64
    )
    return key.hex().upper()


class FilterModule(object):

    def filters(self):
        return {
            # pbkdf2_hmac
            'pbkdf2_hmac': pbkdf2_hmac
        }
