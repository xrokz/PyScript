import Keywords
class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.keywords = [
            Keywords.t_print,
            Keywords.t_stop,
            Keywords.t_call
        ]
        
    def lex(self):
        for location in self.code:
            temp_list = []
            token_id = ''

            for char in location:

                if char == '"' and token_id == '':
                    token_id = 'char'
                    temp_list = []

                elif char == '"' and token_id == "char":
                    self.tokens.append({"id": token_id, "value": "".join(temp_list)})
                    token_id = ''
                    temp_list = []
                
                elif char == ":":
                    token_id = ''
                    self.tokens.append({"id": "label", "value": ''.join(temp_list)})
                    temp_list = []
                
                elif ''.join(temp_list) in self.keywords:
                    token_id = ''
                    self.tokens.append({"id": "keyword", "value": ''.join(temp_list)})
                    temp_list = []
                
                elif char == '\n':
                    if len(temp_list) > 0:
                        self.tokens.append({"id": "atom", 'value': ''.join(temp_list)})
                        temp_list = []

                elif char == " " and token_id != "char":
                    continue

                else:
                    temp_list.append(char)
