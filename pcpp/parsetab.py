
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CPP_AMPERSAND CPP_ANDEQUAL CPP_BAR CPP_BSLASH CPP_CHAR CPP_COLON CPP_COMMA CPP_COMMENT1 CPP_COMMENT2 CPP_DEREFERENCE CPP_DIVIDEEQUAL CPP_DOT CPP_DPOUND CPP_DQUOTE CPP_ENV CPP_EQUAL CPP_EQUALITY CPP_EXCLAMATION CPP_FLOAT CPP_FSLASH CPP_GREATER CPP_GREATEREQUAL CPP_HAT CPP_ID CPP_INEQUALITY CPP_INTEGER CPP_LBRACKET CPP_LCURLY CPP_LESS CPP_LESSEQUAL CPP_LINECONT CPP_LOGICALAND CPP_LOGICALOR CPP_LPAREN CPP_LSHIFT CPP_LSHIFTEQUAL CPP_MINUS CPP_MINUSEQUAL CPP_MINUSMINUS CPP_MULTIPLYEQUAL CPP_OREQUAL CPP_PERCENT CPP_PERCENTEQUAL CPP_PLUS CPP_PLUSEQUAL CPP_PLUSPLUS CPP_POUND CPP_QUESTION CPP_RBRACKET CPP_RCURLY CPP_RPAREN CPP_RSHIFT CPP_RSHIFTEQUAL CPP_SEMICOLON CPP_SQUOTE CPP_STAR CPP_STRING CPP_TILDE CPP_WS CPP_XOREQUALexp_list : expressionexp_list : exp_list expressionexpression : file_namefile_name : file_name file_namefile_name : CPP_FSLASHfile_name : CPP_ENVfile_name : CPP_IDfile_name : CPP_INTEGERfile_name : CPP_DOTexpression : CPP_PLUS CPP_ID\n    expression : CPP_AMPERSAND\n               | CPP_ANDEQUAL\n               | CPP_BAR\n               | CPP_BSLASH\n               | CPP_CHAR\n               | CPP_COLON\n               | CPP_COMMA\n               | CPP_COMMENT1\n               | CPP_COMMENT2\n               | CPP_DEREFERENCE\n               | CPP_DIVIDEEQUAL\n               | CPP_DPOUND\n               | CPP_DQUOTE\n               | CPP_EQUAL\n               | CPP_EQUALITY\n               | CPP_EXCLAMATION\n               | CPP_FLOAT\n               | CPP_GREATER\n               | CPP_GREATEREQUAL\n               | CPP_HAT\n               | CPP_INEQUALITY\n               | CPP_LBRACKET\n               | CPP_LCURLY\n               | CPP_LESS\n               | CPP_LESSEQUAL\n               | CPP_LINECONT\n               | CPP_LOGICALAND\n               | CPP_LOGICALOR\n               | CPP_LPAREN\n               | CPP_LSHIFT\n               | CPP_LSHIFTEQUAL\n               | CPP_MINUS\n               | CPP_MINUSEQUAL\n               | CPP_MINUSMINUS\n               | CPP_MULTIPLYEQUAL\n               | CPP_OREQUAL\n               | CPP_PERCENT\n               | CPP_PERCENTEQUAL\n               | CPP_PLUS\n               | CPP_PLUSEQUAL\n               | CPP_PLUSPLUS\n               | CPP_POUND\n               | CPP_QUESTION\n               | CPP_RBRACKET\n               | CPP_RCURLY\n               | CPP_RPAREN\n               | CPP_RSHIFT\n               | CPP_RSHIFTEQUAL\n               | CPP_SEMICOLON\n               | CPP_SQUOTE\n               | CPP_STAR\n               | CPP_STRING\n               | CPP_TILDE\n               | CPP_WS\n               | CPP_XOREQUAL\n    '
    
_lr_action_items = {'CPP_PLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[4,4,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_AMPERSAND':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[6,6,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_ANDEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[7,7,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_BAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[8,8,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_BSLASH':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[9,9,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_CHAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[10,10,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_COLON':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[11,11,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_COMMA':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[12,12,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_COMMENT1':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[13,13,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_COMMENT2':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[14,14,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_DEREFERENCE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[15,15,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_DIVIDEEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[16,16,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_DPOUND':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[17,17,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_DQUOTE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[18,18,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_EQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[19,19,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_EQUALITY':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[20,20,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_EXCLAMATION':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[21,21,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_FLOAT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[22,22,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_GREATER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[23,23,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_GREATEREQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[24,24,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_HAT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[25,25,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_INEQUALITY':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[26,26,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_LBRACKET':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[27,27,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_LCURLY':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[28,28,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_LESS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[29,29,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_LESSEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[30,30,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_LINECONT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[31,31,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_LOGICALAND':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[32,32,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_LOGICALOR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[33,33,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_LPAREN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[34,34,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_LSHIFT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[35,35,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_LSHIFTEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[36,36,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[37,37,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_MINUSEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[38,38,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_MINUSMINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[39,39,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_MULTIPLYEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[40,40,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_OREQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[41,41,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_PERCENT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[42,42,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_PERCENTEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[43,43,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_PLUSEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[44,44,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_PLUSPLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[45,45,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_POUND':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[46,46,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_QUESTION':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[47,47,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_RBRACKET':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[48,48,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_RCURLY':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[49,49,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_RPAREN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[50,50,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_RSHIFT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[51,51,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_RSHIFTEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[52,52,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_SEMICOLON':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[53,53,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_SQUOTE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[54,54,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_STAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[55,55,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_STRING':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[56,56,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_TILDE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[57,57,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_WS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[58,58,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_XOREQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[59,59,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),'CPP_FSLASH':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[60,60,-1,60,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,60,-10,]),'CPP_ENV':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[61,61,-1,61,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,61,-10,]),'CPP_ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[5,5,-1,5,66,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,5,-10,]),'CPP_INTEGER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[62,62,-1,62,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,62,-10,]),'CPP_DOT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[63,63,-1,63,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,63,-10,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[0,-1,-3,-49,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-5,-6,-8,-9,-2,-4,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exp_list':([0,],[1,]),'expression':([0,1,],[2,64,]),'file_name':([0,1,3,65,],[3,3,65,65,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp_list","S'",1,None,None,None),
  ('exp_list -> expression','exp_list',1,'p_expression_lst_create','path_yacc.py',21),
  ('exp_list -> exp_list expression','exp_list',2,'p_expression_lst_append','path_yacc.py',25),
  ('expression -> file_name','expression',1,'p_expression_basic','path_yacc.py',34),
  ('file_name -> file_name file_name','file_name',2,'p_file_name_merge','path_yacc.py',39),
  ('file_name -> CPP_FSLASH','file_name',1,'p_filename_init','path_yacc.py',43),
  ('file_name -> CPP_ENV','file_name',1,'p_env_expand_','path_yacc.py',47),
  ('file_name -> CPP_ID','file_name',1,'p_file_name_cpp_id','path_yacc.py',51),
  ('file_name -> CPP_INTEGER','file_name',1,'p_file_name_cpp_integer','path_yacc.py',55),
  ('file_name -> CPP_DOT','file_name',1,'p_file_name_cpp_dot','path_yacc.py',59),
  ('expression -> CPP_PLUS CPP_ID','expression',2,'p_exp_plus_id_plus','path_yacc.py',63),
  ('expression -> CPP_AMPERSAND','expression',1,'p_error_process','path_yacc.py',69),
  ('expression -> CPP_ANDEQUAL','expression',1,'p_error_process','path_yacc.py',70),
  ('expression -> CPP_BAR','expression',1,'p_error_process','path_yacc.py',71),
  ('expression -> CPP_BSLASH','expression',1,'p_error_process','path_yacc.py',72),
  ('expression -> CPP_CHAR','expression',1,'p_error_process','path_yacc.py',73),
  ('expression -> CPP_COLON','expression',1,'p_error_process','path_yacc.py',74),
  ('expression -> CPP_COMMA','expression',1,'p_error_process','path_yacc.py',75),
  ('expression -> CPP_COMMENT1','expression',1,'p_error_process','path_yacc.py',76),
  ('expression -> CPP_COMMENT2','expression',1,'p_error_process','path_yacc.py',77),
  ('expression -> CPP_DEREFERENCE','expression',1,'p_error_process','path_yacc.py',78),
  ('expression -> CPP_DIVIDEEQUAL','expression',1,'p_error_process','path_yacc.py',79),
  ('expression -> CPP_DPOUND','expression',1,'p_error_process','path_yacc.py',80),
  ('expression -> CPP_DQUOTE','expression',1,'p_error_process','path_yacc.py',81),
  ('expression -> CPP_EQUAL','expression',1,'p_error_process','path_yacc.py',82),
  ('expression -> CPP_EQUALITY','expression',1,'p_error_process','path_yacc.py',83),
  ('expression -> CPP_EXCLAMATION','expression',1,'p_error_process','path_yacc.py',84),
  ('expression -> CPP_FLOAT','expression',1,'p_error_process','path_yacc.py',85),
  ('expression -> CPP_GREATER','expression',1,'p_error_process','path_yacc.py',86),
  ('expression -> CPP_GREATEREQUAL','expression',1,'p_error_process','path_yacc.py',87),
  ('expression -> CPP_HAT','expression',1,'p_error_process','path_yacc.py',88),
  ('expression -> CPP_INEQUALITY','expression',1,'p_error_process','path_yacc.py',89),
  ('expression -> CPP_LBRACKET','expression',1,'p_error_process','path_yacc.py',90),
  ('expression -> CPP_LCURLY','expression',1,'p_error_process','path_yacc.py',91),
  ('expression -> CPP_LESS','expression',1,'p_error_process','path_yacc.py',92),
  ('expression -> CPP_LESSEQUAL','expression',1,'p_error_process','path_yacc.py',93),
  ('expression -> CPP_LINECONT','expression',1,'p_error_process','path_yacc.py',94),
  ('expression -> CPP_LOGICALAND','expression',1,'p_error_process','path_yacc.py',95),
  ('expression -> CPP_LOGICALOR','expression',1,'p_error_process','path_yacc.py',96),
  ('expression -> CPP_LPAREN','expression',1,'p_error_process','path_yacc.py',97),
  ('expression -> CPP_LSHIFT','expression',1,'p_error_process','path_yacc.py',98),
  ('expression -> CPP_LSHIFTEQUAL','expression',1,'p_error_process','path_yacc.py',99),
  ('expression -> CPP_MINUS','expression',1,'p_error_process','path_yacc.py',100),
  ('expression -> CPP_MINUSEQUAL','expression',1,'p_error_process','path_yacc.py',101),
  ('expression -> CPP_MINUSMINUS','expression',1,'p_error_process','path_yacc.py',102),
  ('expression -> CPP_MULTIPLYEQUAL','expression',1,'p_error_process','path_yacc.py',103),
  ('expression -> CPP_OREQUAL','expression',1,'p_error_process','path_yacc.py',104),
  ('expression -> CPP_PERCENT','expression',1,'p_error_process','path_yacc.py',105),
  ('expression -> CPP_PERCENTEQUAL','expression',1,'p_error_process','path_yacc.py',106),
  ('expression -> CPP_PLUS','expression',1,'p_error_process','path_yacc.py',107),
  ('expression -> CPP_PLUSEQUAL','expression',1,'p_error_process','path_yacc.py',108),
  ('expression -> CPP_PLUSPLUS','expression',1,'p_error_process','path_yacc.py',109),
  ('expression -> CPP_POUND','expression',1,'p_error_process','path_yacc.py',110),
  ('expression -> CPP_QUESTION','expression',1,'p_error_process','path_yacc.py',111),
  ('expression -> CPP_RBRACKET','expression',1,'p_error_process','path_yacc.py',112),
  ('expression -> CPP_RCURLY','expression',1,'p_error_process','path_yacc.py',113),
  ('expression -> CPP_RPAREN','expression',1,'p_error_process','path_yacc.py',114),
  ('expression -> CPP_RSHIFT','expression',1,'p_error_process','path_yacc.py',115),
  ('expression -> CPP_RSHIFTEQUAL','expression',1,'p_error_process','path_yacc.py',116),
  ('expression -> CPP_SEMICOLON','expression',1,'p_error_process','path_yacc.py',117),
  ('expression -> CPP_SQUOTE','expression',1,'p_error_process','path_yacc.py',118),
  ('expression -> CPP_STAR','expression',1,'p_error_process','path_yacc.py',119),
  ('expression -> CPP_STRING','expression',1,'p_error_process','path_yacc.py',120),
  ('expression -> CPP_TILDE','expression',1,'p_error_process','path_yacc.py',121),
  ('expression -> CPP_WS','expression',1,'p_error_process','path_yacc.py',122),
  ('expression -> CPP_XOREQUAL','expression',1,'p_error_process','path_yacc.py',123),
]
