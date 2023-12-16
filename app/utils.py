def convert_to_object(inputClass):
    '''
    Converts a pydantic class into a dictionary. 
    '''
    finalObj = {}

    for row in inputClass:
        if row[1]:
            finalObj[row[0]] = row[1]

    return finalObj