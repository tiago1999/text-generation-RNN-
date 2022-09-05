import tensorflow as tf
import re
import nltk
import random

def generate_poem(input): 

    one_step_reloaded = tf.saved_model.load('/Users/tiagoornelas/Documents/Ironhack/Projects/Final project copy/model/one_step')
    states = None
    next_char = tf.constant([input])
    result = [next_char]

    for n in range(250):
        next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
        result.append(next_char)

    result = tf.strings.join(result)
    output = result[0].numpy().decode('utf-8')
    clean_spaces = re.sub(' +', ' ', output)
    lines = re.sub(':|,|;|\.', '\n', clean_spaces).strip()
    poem_lines_list = lines.split('\n')
    

    return poem_lines_list



def generate_film(input):

    film_generator = tf.saved_model.load('/Users/tiagoornelas/Documents/Ironhack/Projects/Final project copy/model/film_generator_model')

    states = None
    next_char = tf.constant([input])
    result = [next_char]

    for n in range(95):
        next_char, states = film_generator.generate_one_step(next_char, states=states)
        result.append(next_char)

    result = tf.strings.join(result)
    decoded = result[0].numpy().decode('utf-8')

    return decoded
        