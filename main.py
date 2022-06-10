
# Copyright 2020 Google Inc. All Rights Reserved.
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

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    my_x = request.json['arena']['state']['https://squirtlefire-mllc3dma5q-uc.a.run.app']['x']
    my_y = request.json['arena']['state']['https://squirtlefire-mllc3dma5q-uc.a.run.app']['y']
    my_direction = request.json['arena']['state']['https://squirtlefire-mllc3dma5q-uc.a.run.app']['direction']

    if my_direction == 'N':
        for player in request.json['arena']['state']:
            player_x = player['x']
            player_y = player['y']
            if player_x == my_x and player_y - my_y <=3:
                return  'T'

    if my_direction == 'S':
        for player in request.json['arena']['state']:
            player_x = player['x']
            player_y = player['y']
            if player_x == my_x and my_y - player_y <=3:
                return  'T'
    
    if my_direction == 'W':
        for player in request.json['arena']['state']:
            player_x = player['x']
            player_y = player['y']
            if player_y == my_y and my_x - player_x <=3:
                return  'T'
    
    if my_direction == 'E':
        for player in request.json['arena']['state']:
            player_x = player['x']
            player_y = player['y']
            if player_y == my_y and player_x - my_x <=3:
                return  'T'

    return random.choice(['F', 'L', 'R'])

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
