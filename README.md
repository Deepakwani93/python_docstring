# python_docstring

Format.py:
Usage:
   Eg. you have abc.py as follows:
   
      def x(a,b,c):
        pass
   
   running format.py on it will result in abc.py as follows : added docstring and formated code with pep8 style
      
      def x(a, b, c):                                                                                                                                                                                             
         """                                                                        
      ..function::x(a, b, c)                                                        
                                                                               
          :param::a                                                                   
          :param::b                                                                   
          :param::c                                                                   
          :return [on success]::                                                      
          :return [on failure]::                                                             
      **Example**                                                                    
                                                                               
      .. code block::python                                                          
                                                                               
      .. codeauthor::Dipak Wani   
                                                                               
        """                                                                        
        pass


Note: 
   1. Doesn't handle multiline function declaration
   2. Need to have autopep8 installed 

    
