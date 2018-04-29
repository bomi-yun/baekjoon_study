#-*- coding: utf-8 -*-
import requests

class Scrap:
    
    def __init__(self):
        self.problem_description = "problem_description\">"
        self.sample_input = "id = \"sample-input-"
        self.start_p = "<p>"
        self.end_p = "</p>"
        self.url_q = "https://www.acmicpc.net/problem/"
        self.url_s = "https://www.acmicpc.net/step/"
        self.step_problem = "click-this\"><a href = \"/problem/"
        self.pre = "</pre>"
    
    def print_step(self, no):
        r = requests.get(self.url_s + str(no))

        try: 
            pro_str = r.text
            sample_count = pro_str.count(self.step_problem)
         
            print("****************")
            print("*   STEP   " + str(no) + "   *")
            print("****************")
            for i in range(1, sample_count + 1):
                
                pro_str = pro_str[pro_str.find(self.step_problem) + len(self.step_problem):len(pro_str)]
                problem = pro_str[0:pro_str.find("\">")]
                question = pro_str[pro_str.find("\">") + len("\">") : pro_str.find("</a></td>")]
                
                print(problem + " : " + question)

        except IOError: 
            print("IO Error")   
    
    def print_question(self, no):
        r = requests.get(self.url_q + str(no))
        
        try: 
            or_str = r.text
            sample_count = or_str.count(self.sample_input)

            de_str = or_str[or_str.find(self.problem_description): or_str.find(self.problem_description)+ 1000]
            de_str = de_str[de_str.find(self.start_p) + len(self.start_p):de_str.find(self.end_p)]

            print(de_str.strip())


            for i in range(1, sample_count + 1):
                sample_input = "id = \"sample-input-" + str(i) +"\">"
                sample_output = "id = \"sample-output-" + str(i) +"\">"
                
                sam_in = or_str[or_str.find(sample_input): or_str.find(sample_input)+ 1000]
                sam_in = sam_in[0 + len(sample_input):sam_in.find(self.pre)]

                sam_out = or_str[or_str.find(sample_output): or_str.find(sample_output)+ 1000]
                sam_out = sam_out[0 + len(sample_output):sam_out.find(self.pre)]
                print("* input " + str(i) + " *")
                print(sam_in.strip())
                print("* output " + str(i) + " *")
                print(sam_out.strip())
                print("")

        except IOError: 
            print("IO Error")
