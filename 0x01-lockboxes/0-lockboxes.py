#!/usr/bin/python3
'''Working with locks'''


def can_unlock_all(boxes):
    """
    Check if all the boxes can be unlocked, starting from the first box.

    Args:
    - boxes (list of lists): A list of boxes, where each box is represented
      as a list of integers containing indices of other boxes.

    Returns:
    - bool: True if all boxes can be unlocked, False otherwise.
    """
    num_boxes = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= num_boxes or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return num_boxes == len(seen_boxes)
