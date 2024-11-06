from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # if this is only for unformatted nodes that have a text type of text
        # any node with a different value has already been formatted so return as is
        if node.text_type.value != TextType.TEXT.value:
            new_nodes.append(node)
            continue
        
        new_split_nodes = []
        split_nodes = node.text.split(delimiter)

        if (len(split_nodes) % 2) == 0:
            # matching tags will result in an odd number around the formatted word 
            # as an empty string left on the end or is in the middle
            raise ValueError("No closing tag")
        
        for i in range(len(split_nodes)):
            # delimiter at the end of the word so ignore the empty string
            if split_nodes[i] == "":
                continue

            # strings that contain enclosing delimiters will always result in the encased character being at an odd index
            # hello *there* -> ["hello ", "there"], *hello*there -> ["", "hello", "there"]
            if i % 2 == 0:
                new_split_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
            else:
                new_split_nodes.append(TextNode(split_nodes[i], text_type))
                
        new_nodes.extend(new_split_nodes)
    return new_nodes