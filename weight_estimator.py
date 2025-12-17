def estimate_weight_index(bbox_area):
    """
    Relative weight proxy based on bounding box area.
    """
    return round(bbox_area / 1000, 2)
