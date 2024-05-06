import pandas as pd
import json

def remove_parentheses(text):
    start_index = text.find('(')
    end_index = text.find(')')
    if start_index == -1 or end_index == -1:
        return text
    return text[:start_index] + text[end_index + 1:]

def remove_comma(text):
    index = text.find(',')
    if index == -1:
        return text
    return text[:index]

def remove_semicolon(text):
    index = text.find(';')
    if index == -1:
        return text
    return text[:index]

def remove_whitespace(text):
    index = text.find(' ')
    if index == -1:
        return text
    return text[:index]

def dict_to_json(dict):
    return json.dumps(dict)

def json_to_dict(file_name):
    path = 'data/' + file_name + '/' + file_name + '_processed.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    return data