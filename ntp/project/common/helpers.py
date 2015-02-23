def reduceTuple(key_value_tuple_list):
    output = {}
    for elem in key_value_tuple_list:
        if elem[0] in output.keys():
            output[elem[0]] += elem[1]
        else:
            output[elem[0]] = elem[1]
    return output


def chunk(listObject, chunks=4):
    
    length = len(listObject)
    chunks = chunks
    
    # Handle all numbers by finding the remainder
    remainder = length % chunks
        
    # Create a numerator that will always be divisible by the number of chunks
    properNumerator = length - remainder
    
    # Create the basic chunkIndex for slicing the list.
    chunkIndex = properNumerator/chunks
    
    # Create each slice boundary
    index = [chunkIndex * i for i in range(1,chunks)]
    # Handle the final slice boundary and remainder
    index.append(properNumerator+remainder)
    
    # Insert the origin index
    index.insert(0,0)

    # I know this is ugly.  But we are slicing through the index range to get each evenly divided chunk.
    output = [listObject[index[i]:index[i+1]] for i in range(0,len(index)) if index[i]!=index[-1]]
    
    return output


def sortDict(dictionary, val, reverse=False):
    dictionary = sorted(dictionary, key=lambda k: k[val], reverse=reverse)
    return dictionary


def unpack(list_of_lists):
    output = [inner for outer in list_of_lists for inner in outer]
    return output


def unpackCount(list_object, key):
    from collections import Counter
    
    if type(list_object) == list and type(list_object[0])==dict and type(list_object[0][key])==list:
        temp = [elem[key] for elem in list_object]
        temp = [inner for outer in temp for inner in outer]
        return Counter(temp)
    else:
        return "Input object needs to be a list of dictionaries all containing the same key.  The value must be either a list of str/unicode"


def filterText(elem, replace=" ", case="lower", type_='alpha', truncate=False, length=0):

    if type_ == 'alphaNum':    
        derp = "".join([c if c.isalnum() else replace for c in elem])
        if truncate == True:
            derp = [elem for elem in derp if len(elem)>length]
        if case != "lower":
            return derp.upper()
        return derp.lower()
    
    elif type_ == 'alpha':

        derp = "".join([c if c.isalpha() else replace for c in elem])
        if truncate == True:
            derp = [elem for elem in derp if len(elem)>length]
        if case != "lower":
            return derp.upper()
        return derp.lower()
    
    elif type_ == 'numeric':

        derp = "".join([c if c.isnumeric() else replace for c in elem])
        if truncate == True:
            derp = [elem for elem in derp if len(elem)>length]
        if case != "lower":
            return derp.upper()
        return derp.lower()