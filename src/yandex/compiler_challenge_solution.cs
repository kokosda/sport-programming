 namespace CompilerChallenge
 {
   using System;
   using System.Text.RegularExpressions;
   using System.Collections.Generic;
      
   public class Compiler
   {
     public Ast pass1(string prog)
     {
        List<string> tokens=tokenize(prog);
       foreach (var t in tokens)
         Console.WriteLine(t);
		 var  p = Dictionary<string, string>();
		 for (int i = 0;; i++)
		 {
			 
		 }
        return null;
     }
     
     public Ast pass2(Ast ast)
     {
       return null;
     }
     
     
     public List<string> pass3(Ast ast)
     {
       return null;
     }
     
     private List<string> tokenize(string input)
     {
       List<string> tokens = new List<string>();
       Regex rgxMain = new Regex("\\[|\\]|[-+*/=\\(\\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*(\\.?[0-9]+)");
       MatchCollection matches = rgxMain.Matches(input);
       foreach (Match m in matches) tokens.Add(m.Groups[0].Value);
       return tokens;
     }
   }
 }

 /*
 [xyz](3*2*x + 2*z)/(6-y)
 stack: {(,[3,*,2],+,[2,*,z],),/,(,6,-,y,)}
 BinOp("/", 3*2*x + 2*z, 6-y)
 */