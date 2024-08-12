from linked_list import Node, LinkedList
from flower import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key):
    return hash(key)

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]
    payload = Node([key, value])
    for i in list_at_array:
      if i[0] == key:
        i[1] = value
        return
    list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for i in list_at_index:
      if i[0] == key:
        return i[1]
    return None

blossom = HashMap(len(flower_definitions))
for i in flower_definitions:
  blossom.assign(i[0], i[1])

print(blossom.retrieve('daisy'))
