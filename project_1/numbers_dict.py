# dictionnaire ( nombres -> Lettres +  erreurs ) 
# v 3.0

import string
alpha = string.digits + string.ascii_uppercase + string.ascii_lowercase

errors_dict={}
errors_dict[1] = 'ERROR_TYPE_1: Invalid Request'
errors_dict[2] = 'ERROR_TYPE_2: Invalid Number Request (Negative Number)'
errors_dict[3] = "ERROR_TYPE_3: Invalid Base Request (Negative, Null, or '1' Base)"
errors_dict[4] = "ERROR_TYPE_4: Invalid  Request (Not A Number, Negative or decimal)"
errors_dict[5] = "ERROR_TYPE_5: Too Important Base ( More than 62 is UNAVAILBLE ) "
