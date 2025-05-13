
# user_input = 'centro'

# dicionario = {'Centro da Cidade': 'uma instancia', 'Igreja': 'outra instancia', 'Floresta': 'Outra inst'}

# places_to_go = ['Igreja', 'Centro da Cidade']
# current_place = 'Floresta'

# user_input_lowered = user_input.lower()
# stopwords = {"a", "o", "os", "as", "para", "da", "de", "do", "das", "dos", "pra"}
# user_words = [word for word in user_input.lower().split() if word not in stopwords]
# for place_name, value in dicionario.items():
#     # print(f'primeiro for: {place_name}')
#     if any(word in place_name.lower() for word in user_words):
#         for place in places_to_go:
#             # print(f' segundo for: {place} está em {places_to_go}?')
#             if place_name.lower() in place.lower():
#                 current_place = place_name
#                 print('chegou no fim')

from operator import add
from typing import Annotated

class State(TypedDict):
    foo: Annotated[list[int], add]


class State(typedict):
    foo: Annotated[list[ind], add]

    
def estado(Annotaded)
state = {'foo': [1]}

dicionario =  {"foo": [state['foo'][0] + 1]}


print(dicionario)