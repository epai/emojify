delim = '---'

accepted = 'abcdefghijklmnopqrstuvwxyz-?!.'

letters = \
"""
 #
# #
###
# #
# #
{0}
##
# #
##
# #
##
{0}
 ##
#
#
#
 ##
{0}
##
# #
# #
# #
##
{0}
###
#
###
#
###
{0}
###
#
###
#
#
{0}
 ##
#
# ##
#  #
 ##
{0}
# #
# #
###
# #
# #
{0}
###
 #
 #
 #
###
{0}
  #
  #
  #
  #
##
{0}
#  #
# #
##
# #
#  #
{0}
#
#
#
#
###
{0}
 ###
# # #
# # #
# # #
# # #
{0}
#  #
## #
# ##
#  #
#  #
{0}
 #
# #
# #
# #
 #
{0}
##
# #
##
#
#
{0}
 #
# #
# #
# #
 ###
{0}
##
# #
##
# #
# #
{0}
 ##
#
 #
  #
##
{0}
###
 #
 #
 #
 #
{0}
# #
# #
# #
# #
###
{0}
# #
# #
# #
# #
 #
{0}
#   #
# # #
# # #
# # #
 ###
{0}
# #
# #
 #
# #
# #
{0}
# #
# #
 #
 #
 #
{0}
###
  #
 #
#
###
{0}


###


{0}
###
  #
 #

 #
{0}
 #
 #
 #

 #
{0}




 #
""".format(delim).split(delim)
letters = [l[1:-1] for l in letters]

def get_letter(letter):
    try:
        letter_index = accepted.index(letter.lower())
    except ValueError:
        raise LookupError(
            "Invalid character '{}'.  Acceptable characters: '{}'"
            .format(letter, accepted))
    else:
        letter = letters[letter_index]
        lines = letter.split('\n')
        length = max(len(l) for l in lines)
        return [l.ljust(length) for l in lines]

def letter_length(letter):
    return len(get_letter(letter)[0])

def get_word(string):
    string = string.upper()
    letters = (get_letter(l) for l in string)
    lines = [' '.join(line) for line in zip(*letters)]
    return lines



