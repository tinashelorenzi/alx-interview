#!/usr/bin/python3
"""
This module provides functions for working with lockboxes.

The primary function, can_unlock_all(boxes), checks if all the boxes in
a list of boxes contain keys (indices) to other boxes, and if they can be
unlocked starting from the first box, which is assumed to be unlocked.
"""


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
    unopened_boxes = set(boxes[0]).difference(set([0]))

    while len(unopened_boxes) > 0:
        current_box_idx = unopened_boxes.pop()

        # Check for invalid box indices (negative or out of range).
        if not 0 <= current_box_idx < num_boxes:
            continue

        if current_box_idx not in seen_boxes:
            unopened_boxes = unopened_boxes.union(boxes[current_box_idx])
            seen_boxes.add(current_box_idx)

    return num_boxes == len(seen_boxes)
