import re
def is_stressful(subj):
    """
        recoognise stressful subject
    """
    '''
        check "red" words "help","asap","urgent"
    '''
    pattern_help=r'[Hh]+[!-.]*[Ee]+[!-.]*[Ll]+[!-.]*[Pp]+[!-.]*'
    pattern_asap=r'[Aa]+[!-.]*[Ss]+[!-.]*[Aa]+[!-.]*[Pp]+[!-.]*'
    pattern_urgent=r'[Uu]+[!-.]*[Rr]+[!-.]*[Gg]+[!-.]*[Ee]+[!-.]*[Nn]+[!-.]*[Tt]+[!-.]*'
    if re.search(pattern_help,subj) != None :
        return True
    if re.search(pattern_asap,subj) != None :
        return True
    if re.search(pattern_urgent,subj) !=None :
        return True
    
    '''
        check 3 exclamation mark
    '''
    
    if subj[-3:] == '!!!' :
        return True
        
    '''
      check upper letter.
    '''
    if re.search(r'[a-z]',subj) == None :
        return True
    return False
