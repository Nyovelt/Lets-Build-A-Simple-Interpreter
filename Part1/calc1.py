# Token types: 替代类型
#
# EOF: end of file 终止符

INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF' 

class Token(object):
        def __init__(self, type, value):
                # token type: 'INTEGER', 'PLUS', 'EOF' 
                self.type = type
                # token value: 0,1 ,2 ,3 , .. ,9 , '+', or None
                self.value = value

        def __str__(self):
                """  str method 
                Examples:
                        Token(INTEGER, 3)
                        Token(PLUS '+')
                """
                return 'Token({type}, {value})'.format(
                        type  = self.type,
                        value  = str(self.value)
                        # value = repr(self.value)
                        # value = self.value
                )

        def __repr__(self):
                return self.__str__()
        
class Interpreter(object):
        '''
                解释器部分
        '''
        def __init__(self, text):
                # 记录输入, e.g. "3+5"
                self.text = text
                # 对于self.text的索引器/指针
                self.pos = 0
                # current token instance
                self.current_token = None

        def error(self):
                raise Exception('Error parsing input')

        def get_next_token(self):
                """Lexical analyzer (also known as scanner or tokenizer)

                This method is responsible for breaking a sentence
                apart into tokens. One token at a time.


                词法分析器：

                负责把输入分解成token
                """
                text = self.text

                # 当词法分析器分析到最后一个词的时候，
                # 向Token返回终止符EOF
                if self.pos > len(text) - 1:
                        return Token(EOF, None)

                # 获得当前位置的字符，并以此进行下面的判断
                current_char = text[self.pos]

                # 当前位置的字符一共有两种情况，
                # 分别是 数字 和 符号(+)
                # 如果是数字：
                #         将数字字符转为整形，并返回Token
                # 如果是符号：
                #         直接返回Token
                if current_char.isdigit():
                        token = Token(INTEGER, int(current_char))
                        self.pos += 1
                        return token
                
                if current_char == '+':
                        token = Token(PLUS, current_char)
                        self.pos += 1
                        return token

                self.error()

                