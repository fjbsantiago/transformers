def build_hierarchy(elements, fields):
    """Groups dictionaries in an hierarchical way
    respecting the order provied by "fields". First field will be used 
    to group the first layer.
    
    :param elements: list of JSON objects
    :param fields: list of fields to use as grouping keys. Order matters
    :return: a JSON list with the format [{title: "something1", nodes:[{title: "something2", nodes:[...]}]}] 
    """
    
    nodes = []

    if not fields:
        return elements

    # Clone list and remove first element
    fields = fields[:]
    field = fields.pop(0)
    # Sort elements by current field to allow grouping
    ordered_elements = sorted(elements, key=lambda k: k[field])

    for k, g in itertools.groupby(ordered_elements, lambda el: el[field]):
        node = {
            'title': k,
            'nodes': build_hierarchy(list(g), fields)
        }

        nodes.append(node)

    return nodes

