def convert_to_object(inputClass):
    '''
    Converts a pydantic class into a dictionary. 
    '''
    finalObj = {}

    for row in inputClass:
        if row[1] and isinstance(row[1], str):
            finalObj[row[0]] = row[1]
        elif row[1] > 0:
            finalObj[row[0]] = row[1]

    return finalObj