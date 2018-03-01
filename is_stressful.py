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
'''
函数功能是检查邮件标题中是否包含紧急关键字（'help','asap'或'urgent'，或全大写，或最后到少有三个叹号）
注：'help','asap'或'urgent'可以是中间被字符间隔开的或是重复的如：
HEEEEELP,HHHHHHHELP,H-E-L-P,H!E!L!P
'''
