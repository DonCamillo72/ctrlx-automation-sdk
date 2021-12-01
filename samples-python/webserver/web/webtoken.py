# MIT License
#
# Copyright (c) 2020-2021 Bosch Rexroth AG
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import jwt
import json


def checkPermissions (token : str, scopes_list):

    try:
        token_decoded=jwt.decode(token,options={"verify_signature": False})
        
        if 'scope' in token_decoded is None:
            print("ERROR Decoding bearertoken: No scope found")
            return None
        scopes_token = token_decoded['scope']
        scopes_validated_json = {}
        for scope in scopes_list:
            if scope in scopes_token:
                scopes_validated_json[str(scope)]= True
            else:
                scopes_validated_json[str(scope)]= False
            
        return scopes_validated_json
    except jwt.DecodeError:
        print("ERROR Decoding bearertoken")
        return None
    
