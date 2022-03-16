# HW3
#Due Date: 03/13/2021, 11:59PM

"""                                   
### Collaboration Statement:
             
"""

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.top == None:
            return True
        return False



    def __len__(self): 
        # YOUR CODE STARTS HERE
        c = 0
        current = self.top 
        while current:
            c += 1 
            current = current.next 
        return c 

    def push(self,value):
        # YOUR CODE STARTS HERE

        if self.isEmpty():
            new_node = Node(value)
            self.top = new_node
            new_node.next = None  
        else: 
            new_node = Node(value)
            new_node.next = self.top 
            self.top = new_node



     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        old_top = self.top.value
        self.top = self.top.next 
        return old_top 
  

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        return self.top.value



#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try:
            float(txt)
        except (ValueError):
            return False
        else:
            return True









    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        infix = txt.split()
        
        postfix = "" 
        postfixlst = []
        operators = ['+', '-', '^', '*', '/'] 
        #print(infix)

        
        if self.isOperator(infix) == False:
            return None 

        for element in infix:
            #print(infix.index(element))

            if self._isNumber(element):
                element = float(element)
                element = str(element)
                postfix += element + ' '
                postfixlst.append(element)


            else:
                if postfixStack.isEmpty():
                    postfixStack.push(element)

                elif element == '(':
                    if self.parenthesesMatch(infix):
                        postfixStack.push(element)
                    else:
                        return None

                elif element == ')':
                    if self.parenthesesMatch(infix):

                        while postfixStack.isEmpty() == False:
                            top = postfixStack.pop()
                            if top == '(':
                                break 
                            
                            if top != ')':
                                    postfix += top + ' '
                                    postfixlst.append(top)
                    else:
                        return None 
                        
                        
                elif element in operators:
                    # If Element is exponent, it must be followed by a number or the code will not run properly. 
                    if element == '^':
                        index = infix.index(element) + 1 
                        if not self._isNumber(infix[index]):
                            return None 



                    while not postfixStack.isEmpty():
                        # If the item at the top of the stack has higher precedence than the current element, break
                        if self.isLowerPrecedence(postfixStack.top.value, element): 
                            break
                        else:
                            top = postfixStack.pop()
                            if top != '(' and top != ')':
                                postfix += top + ' '
                                postfixlst.append(top)
                    postfixStack.push(element) 
                else:
                    #print(element)
                    return None       
   
        if postfixStack.isEmpty():


            return " ".join(postfixlst)

        else:
            top = postfixStack.top
            while top != None:
                temp = top 
                if top.value != '(' and top.value != ')':
                                postfix += str(top.value) + ' '
                                postfixlst.append(str(top.value))
               

                top = temp.next 
        return " ".join(postfixlst)

    def isOperator(self, expr):
        # determines if there is an operator, the correct amount of parentheses, and if the amount of operators match n+1 the amount of numbers 

        noOperators = 0
        openPara = 0
        closedPara = 0
        numCount = 0
        operatorCount = 0
        for num in expr:
            if self._isNumber(num):
                numCount += 1
            else:
                if num != '(' and num != ')':
                    operatorCount += 1 
        for operator in ['+', '-', '^', '*', '/', '(', ')']:
            if operator == '(' and operator in expr:
                openPara = expr.count('(')
            elif operator == ')' and operator in expr:
                closedPara = expr.count(')')
            if operator not in expr:
                noOperators += 1 
        if noOperators == 7:
            if numCount == 1:
                return True
            else:            
                return False
        if numCount - 1 != operatorCount:
            #print(numCount, operatorCount)

            return False

        if openPara != closedPara:
            return False



    def isLowerPrecedence(self, top_operator, operator):
        # returns True if current TOP has lower precedence than new operator 
        precedence = {'(': 4, ')': 4, '^': 1, '*': 2, '/': 2, '+': 3, '-': 3} 
        if top_operator == '^' and operator == '^':
            return True

        if precedence[top_operator] > precedence[operator]:
            return True
        else:
            return False 


    def parenthesesMatch(self, lst):
        # Determines if element has a matching closed/open (, ) 
        
        index = 0 
        para = [] 
        while len(lst) > index:
            item = lst[index]
            if item == '(':
                para.append(item)
            elif item == ')':
                if '(' not in para:
                    return False
                para.pop()
            index += 1
        return True 
       

    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( ( ( 10 - 2 * 3 ) ) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate


        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        postfix_str = self._getPostfix(self.__expr)
        if postfix_str == None:
            return None
        
        postfix = postfix_str.split()
        #print(postfix)

        if len(postfix) <= 1:
            return postfix[0]

        for element in postfix:
            if self._isNumber(element):
                calcStack.push(float(element))
            else:
                #print(element)
                if len(calcStack) == 1:
                    return calcStack.pop()
                if element == "+":
                    result1=calcStack.pop()
                    result2=calcStack.pop()
                    calcStack.push(result1+result2)
                elif element == "-":
                    result1=calcStack.pop()
                    result2=calcStack.pop()
                    calcStack.push(result2-result1)
                elif element == "*":
                    result1=calcStack.pop()
                    result2=calcStack.pop()
                    calcStack.push(result1*result2)
                elif element == "/":
                    result1=calcStack.pop()
                    result2=calcStack.pop()
                    calcStack.push(result2/result1)
                elif element == "^":
                    result1=calcStack.pop()
                    result2=calcStack.pop()
                    calcStack.push(result2**result1)
                else:
                    return None
        if len(calcStack) > 1:
            return None
        return calcStack.pop()

                    



#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        if word[0].isalpha() == False:
            return False

        for letter in word:
            if letter.isalpha():
                pass
            elif Calculator._isNumber(self, letter):
                pass
            else:
                return False
        return True

       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        exprLst = expr.split()
        expression = []
        for item in exprLst: 
            if self._isVariable(item):
                try:
                    expression.append(str(self.states[item]))
                except KeyError:
                    return None
            elif item in ['+', '-', '^', '*', '/', '(', ')']:
                expression.append(item)
            elif Calculator._isNumber(self, item):
                expression.append(item)
            else:
                return None
        return " ".join(expression)

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        lst = self.expressions.split(';')

        
        for item in lst:

            
            if 'return' in item:
                self.states['_return_'] = item


            else:
                templst = item.split('=')
                variable = templst[0].strip()

                expr = self._replaceVariables(templst[1])
                calcObj.setExpr(expr)
                
                self.states[variable] = calcObj.calculate
                
        
                
        return self.states
        
