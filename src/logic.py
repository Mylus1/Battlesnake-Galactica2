import random
from typing import List, Dict
from flask import request


def get_info() -> dict:
    return {
        "apiversion": "1",
        "author": "Mylus1",
        "color": "#E80978",
        "head": "bendr",
        "tail": "sharp",
    }


def choose_move(data: dict) -> str:
  my_snake = data["you"]
  my_head = my_snake["head"]
  my_body = my_snake["body"]

  possible_moves = ["up", "down", "left", "right"]
  possible_moves = _avoid_my_neck(my_body, possible_moves)
  possible_moves = avoid_walls(data['board']['height'], data['board']['width'], my_body, possible_moves)
  possible_moves = avoid_self(my_body, possible_moves)
  if not possible_moves:
    move = "up"
  else:
    move = random.choice(possible_moves)
  
  print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")

  return move


def avoid_walls(board_height: int, board_width: int, my_body: dict, possible_moves: List[str]) -> List[str]:
  my_head = my_body[0]
  my_neck = my_body[1]
  if my_head["y"] == board_height-1 and "up" in possible_moves:
    print("we're on the top row, removing up")
    possible_moves.remove("up")
  if my_head["y"] == 0 and "down" in possible_moves:
    print("we're on the bottom row, removing down")
    possible_moves.remove("down")
  if my_head["x"] == 0 and "left" in possible_moves:
    print("we're on the left column, removing left")
    possible_moves.remove("left")
  if my_head["x"] == board_width-1 and "right" in possible_moves:
    print("we're on the right comlumn, removing right")
    possible_moves.remove("right")
  
  return possible_moves


def avoid_self(my_body: List[dict], possible_moves: List[str]) -> List[str]:
  my_head = my_body[0]

  rest_of_body = my_body[2:]
  for b in rest_of_body:
    if my_head["x"] == b["x"]-1 and "right" in possible_moves and my_head["y"] == b["y"]:
      print("Body is to our right, removing right")
      possible_moves.remove("right")

    if my_head["x"] == b["x"]+1 and "left" in possible_moves and my_head["y"] == b["y"]:
      print("Body is to our left, removing left")
      possible_moves.remove("left")

    if my_head["y"] == b["y"]-1 and "up" in possible_moves and my_head["x"] == b["x"]:
      print("Body is above us, removing up")
      possible_moves.remove("up")

    if my_head["y"] == b["y"]+1 and "down" in possible_moves and my_head["x"] == b["x"]:
      print("Body is below us, removing down")
      possible_moves.remove("down")

  return possible_moves


def _avoid_my_neck(my_body: dict, possible_moves: List[str]) -> List[str]:
  my_head = my_body[0]
  my_neck = my_body[1]
    
  if my_neck["x"] < my_head["x"]:
      print("neck is left of us, removing left")
      possible_moves.remove("left")
  elif my_neck["x"] > my_head["x"]:
      print("neck is right of us, removing right")
      possible_moves.remove("right")
  elif my_neck["y"] < my_head["y"]:
      print("neck is below us, removing down")
      possible_moves.remove("down")
  elif my_neck["y"] > my_head["y"]: 
      print("neck is above us, removing up")
      possible_moves.remove("up")
  return possible_moves

