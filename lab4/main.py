from graph_tool.all import *
from words import words
from valuable import words as dictionary
from math import log10


def get_vertex(g, name, word, vertices):
    # If we already have this vertex, just use it from cache
    if name in vertices:
        return vertices[name]
    # Otherwise we have to create new one
    a = g.add_vertex()
    word[a] = name
    # Add the vertex to cache
    vertices[name] = a
    return a


def build_graph(treshold=.1, last_word=-1):
    # Create directed graph
    g = Graph(directed=True)

    # Create 'weight' property for edge: will contain tf-idf
    weight = g.new_edge_property('float')
    # Create 'word' property for vertex: will contain string with current word
    word = g.new_vertex_property('string')
    # Dictionary with existent vertices (cache)
    vertices = {}

    for w in words[:last_word]:
        # Check, whether at least one word is in dictionary of valuable words
        if w[0] not in dictionary and w[1] not in dictionary:
            continue
        # Check, whether at least one word is valuable
        if dictionary[w[0]] < treshold and dictionary[w[1]] < treshold:
            continue
        a = get_vertex(g, w[0], word, vertices)
        b = get_vertex(g, w[1], word, vertices)
        e = g.add_edge(a, b)
        # Set weight for new edge (tf-idf)
        # Just empirical formula, which gives edges with 1 <= width < 30
        weight[e] = log10(w[2])*10 + 23

    return g, weight, word


if __name__ == '__main__':
    g, weight, word = build_graph()
    # Draw the graph;
    # Weight is responsible for edges widths
    # Word contains labels for vertices
    graph_draw(g, vertex_font_size=12, edge_pen_width=weight, vertex_text=word,
               output='words.png', output_size=(2000, 2000))
    # Alternative
    # graph_draw(g, edge_pen_width=weight, vertex_text=word, node_first=True,
    #            vertex_text_position=0, vertex_size=20, vertex_shape='double_square')
    # Or even
    # state=minimize_nested_blockmodel_dl(g)
    # draw_hierarchy(state, vertex_text=word, vertex_text_position=0)

