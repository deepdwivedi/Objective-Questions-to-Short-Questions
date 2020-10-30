

# from google.colab import drive
# drive.mount('/content/drive')

import pandas as pd
import nltk

def convert_to_superscript(temp):
  superscript_map = {
  "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
  "7": "⁷", "8": "⁸", "9": "⁹", "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ",
  "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ᶦ", "j": "ʲ", "k": "ᵏ",
  "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "q": "۹", "r": "ʳ",
  "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ",
  "z": "ᶻ", "A": "ᴬ", "B": "ᴮ", "C": "ᶜ", "D": "ᴰ", "E": "ᴱ", "F": "ᶠ",
  "G": "ᴳ", "H": "ᴴ", "I": "ᴵ", "J": "ᴶ", "K": "ᴷ", "L": "ᴸ", "M": "ᴹ",
  "N": "ᴺ", "O": "ᴼ", "P": "ᴾ", "Q": "Q", "R": "ᴿ", "S": "ˢ", "T": "ᵀ",
  "U": "ᵁ", "V": "ⱽ", "W": "ᵂ", "X": "ˣ", "Y": "ʸ", "Z": "ᶻ", "+": "⁺",
  "-": "⁻","–": "⁻", "=": "⁼", "(": "⁽", ")": "⁾"}

  SUP = str.maketrans(
  ''.join(superscript_map.keys()),
  ''.join(superscript_map.values()))
  # print(temp, temp.translate(SUP))
  return temp.translate(SUP)

def convert_to_subscript(temp):
  subscript_map = {
  "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆",
  "7": "₇", "8": "₈", "9": "₉", "a": "ₐ", "b": "♭", "c": "꜀", "d": "ᑯ",
  "e": "ₑ", "f": "բ", "g": "₉", "h": "ₕ", "i": "ᵢ", "j": "ⱼ", "k": "ₖ",
  "l": "ₗ", "m": "ₘ", "n": "ₙ", "o": "ₒ", "p": "ₚ", "q": "૧", "r": "ᵣ",
  "s": "ₛ", "t": "ₜ", "u": "ᵤ", "v": "ᵥ", "w": "w", "x": "ₓ", "y": "ᵧ",
  "z": "₂", "A": "ₐ", "B": "₈", "C": "C", "D": "D", "E": "ₑ", "F": "բ",
  "G": "G", "H": "ₕ", "I": "ᵢ", "J": "ⱼ", "K": "ₖ", "L": "ₗ", "M": "ₘ",
  "N": "ₙ", "O": "ₒ", "P": "ₚ", "Q": "Q", "R": "ᵣ", "S": "ₛ", "T": "ₜ",
  "U": "ᵤ", "V": "ᵥ", "W": "w", "X": "ₓ", "Y": "ᵧ", "Z": "Z", "+": "₊",
  "-": "₋","–": "₋", "=": "₌", "(": "₍", ")": "₎"}

  SUB = str.maketrans(
  ''.join(subscript_map.keys()),
  ''.join(subscript_map.values()))
  return temp.translate(SUB)

def cleaning(text):
  """"Function that Cleans the text and handles the superscript and subscript
  tags in the text
  Parameters
  ----------
  text: word_tokenized list of an objective question

  Returns
  --------
  index: index of a found seperator, by default -1
  """
    
  ind = 0
  text = text.replace(":","")
  n = len(text)

  """Replacing sup tag with supercript"""
  while (ind < len(text)):
    if(text[ind]=="<" and ind < n-4 and text[ind+1:ind+4]=="sup"):
      curr = ind
      curr += 5
      temp = ""
      while(True):
        if(text[curr]=="<" and text[curr+1:curr+5]=="/sup"):
          break
        temp += text[curr]
        curr += 1
      text = text[:ind] + convert_to_superscript(temp)+text[curr + 6:]
      ind = curr + 6
    else:
      ind += 1


    """Replacing sub tag with subcript"""
  ind = 0
  while (ind < len(text)):
    if(text[ind]=="<" and ind < n-4 and text[ind+1:ind+4]=="sub"):
      curr = ind
      curr += 5
      temp = ""
      while(True):
        if(text[curr]=="<" and text[curr+1:curr+5]=="/sub"):
          break
        temp += text[curr]
        curr += 1
      text = text[:ind] + convert_to_superscript(temp)+text[curr + 6:]
      ind = curr + 6
    else:
      ind += 1

  x = text
  y = re.sub('\\n', ' ',x)
  y = re.sub('\\r', ' ',y)
  y = re.sub('\\t', ' ',y)
  y = re.sub('<[^>]*>', ' ',y)
  y = y.strip()
  return y

verbs = pd.read_csv ("verbs.csv",sep="\t")

def check_verb(text):
    wordsList = nltk.word_tokenize(text) 
    # print(wordlist)
    # Nouns = ["NN","NNS","NNP","NNPS"]
    Verbs = ["VB", "VBZ", "VBD","VBN","VBG","VBP"]
    tagged = nltk.pos_tag(wordsList)
    return tagged[0][1] in Verbs

def pos_tagging(s):
  tokenized = nltk.tokenize.sent_tokenize(s)
  tagged=[]
  for i in tokenized: 
    wordsList = nltk.word_tokenize(i) 
    # Nouns = ["NN","NNS","NNP","NNPS"]
    # Verbs = ["VB", "VBZ", "VBD","VBN","VBG","VBP"]
    tagged = nltk.pos_tag(wordsList)

  return tagged

def aux_verb_check(wordList):
  auxilliary_verbs = ["is","are","was","were","has","have","can","should","do","would","will","does"]
  for verb in auxilliary_verbs:
    for word in wordList:
      if word == verb:
        return wordList.index(word), verb
  return None,None

# !sudo apt-get install -y python3-enchant

# !python -m spacy download en_core_web_lg


import re
import csv

count = 0
notWh = []
notWh_ans = []
notWh_tn = []
notWh_bs = []
notWh_rs = []
notWh_ct = []
notWh_skill = []
import re
# d = enchant.Dict("en_US")
count_hindi = 0
count_other = 0
count_following = 0
count_wh = 0
count_notWh = 0
count_correct = 0
whWords = ["what","where","when","which","who","whom","why","whether","how","did"]
# with open("cleaned_question_set.csv","w") as file:
  # writer = csv.writer(file)
  # writer.writerow(data.columns)
  # for i in range(300000):
def pre_process(x):
  flag_eng = True
  print(x,"xxxxx")
  y = x.lower()
  
  if("<table" in x or  "not" in x or "<img" in x or "<li" in x or "the following" in x or "incorrect statement" in x or "of the statements" in x or "identify" in x or "<mrow" in x ):
    # print("zzz")
    return "Unable to resolve"
  # try:/
  y = cleaning(y)
  # y = a.l/ower()
  # for j in y:
  if(not re.match(r'[a-z0-9]+',y)):
    count_hindi +=1
    # print(y)
    # input()
    flag_eng = False

    # break
  # ans_y = str(answer.iloc[i])
  # print(ans_y)
  # ans_y = ans_y.lower()
  # ans_y = cleaning(ans_y)
  flag = 0
  for j in whWords:
    if(j in y or "_" in y):
      flag = 1
      count_wh +=1
  if(flag == 0 and flag_eng):
    # print(y,"------------------>",ans_y)
    return y
    # notWh.append(a)
    # print(len(notWh))
    # count_notWh +=1
    # print(notWh)
    # notWh_ans.append(ans_y)
    # notWh_tn.append(type_name.iloc[i])
    # notWh_bs.append(board_syllabus.iloc[i])
    # notWh_rs.append(repository_syllabus.iloc[i])
    # notWh_ct.append(content_type.iloc[i])
    # notWh_skill.append(skill_name.iloc[i])
    # count += 1  
    # writer.writerow(data.iloc[i])
  # except:
    # return "Unable to resolve"

 

def seperator_finding(word_tokens):
  """ Function for finding an in between comma or full-stop in an objective question.
  The first part of the question is often used for description.
  Parameters
  ----------
  word_tokens: word_tokenized list of an objective question

  Returns
  --------
  index: index of a found seperator, by default -1
  """
  
  index = -1
  endTokenIndex = len(word_tokens) - 1 if word_tokens[-1]=="." else len(word_tokens) - 2
  for i in range(endTokenIndex,-1,-1):
    if(word_tokens[i]=="," or word_tokens[i]=="."):
      # if(len(word_tokens)-i<=3):
      #   continue
      return i
  return index


def past_verb_check(taggedList):
  from nltk.stem import WordNetLemmatizer 
  lemmatizer = WordNetLemmatizer() 
  past_verb_forms = ["VBD","VBN"]
  for index,tags in enumerate(taggedList):
    if(tags[1] in past_verb_forms):
      return index, lemmatizer.lemmatize(tags[0],pos='v')
  return None,None

def on_questions(text,answer):
  import spacy
  nlp = spacy.load('en_core_web_sm')
  date_time_labels = ["DATE","TIME"]
  place_labels = ["GPE","LOC","FAC","EVENT"]
  doc = nlp(answer)
  auxilliary_verbs = ["is","are","was","were","has","have","can","should","do","would","will","does"]
  word_list = nltk.tokenize.word_tokenize(text)
  ner_labels = []
  for ent in doc.ents:
    ner_labels.append(ent.label_)
  (past_verb_index , past_verb) = past_verb_check(pos_tagging(text))
  aux_verb = 'does' if past_verb_index==None else "did"
  whWord = ""
  for label in date_time_labels:
    if label in ner_labels:
      whWord = "when"
      break 
  for label in place_labels:
    if label in ner_labels:
      whWord = "where"
      break 
  for index in range(len(word_list)-1,-1,-1):
    if word_list[index] in auxilliary_verbs:
      aux_verb = word_list[index]
      word_list.pop(index)
      break
  if(whWord==""):
    return "No pattern found"

  if(past_verb!=None and aux_verb=="did"):
    word_list.pop(past_verb_index)
    word_list.insert(past_verb_index,past_verb)
  
  ind = seperator_finding(word_list)
  if(ind!=-1):
    out = " ".join(word_list[:ind+1]) +  " " + whWord + " " + aux_verb + " " + " ".join(word_list[ind+1:len(word_list)-1])
  else:
    out = whWord + " "  + aux_verb + " " + " ".join(word_list[0:len(word_list)-1])
  # print(out)
  return out

def as_for_questions(text):
  """ Function for conversion of objective questions falling in 
  "as/for" category.

  Paramters
  ----------
  text: complete objective question after cleaning
  """
  
  word_list = nltk.tokenize.word_tokenize(text)
  n = len(word_list)
  for i in range(n):
    word_list[i]=word_list[i].strip()
  out = ""
  
  if(n-3>=0 and word_list[n-3]=="also" and word_list[n-2]=="known"):
    ind = seperator_finding(word_list)
    if(ind==-1):
      out = "What is another name of" + " " +" ".join(word_list[:n-4])
    else:
      out = " ".join(word_list[:ind+1])+" "+"what is another name of"+" "+" ".join(word_list[ind+1:n-4])
    # print(out)
    return out

  elif(n-2>=0 and  check_verb(word_list[n-2])):
    ind = seperator_finding(word_list)
    arr = ["is","was","are","were"]
    aux = "does"
    if(n-3>=0 and word_list[n-3] in arr):    
      aux = word_list[n-3]
      word_list[n-3]=""
    if(n-4>=0 and word_list[n-4] in arr):
      aux = word_list[n-4]
      word_list[n-4]=""
    if(ind==-1):
      out = "What"+" "+aux + " " +" ".join(word_list[:])
    else:
      out = " ".join(word_list[:ind+1])+" "+"what"+" "+aux+" "+" ".join(word_list[ind+1:])
  
  elif(n-2>=0 and  check_verb(word_list[n-2])==False):
    aux = "does"
    ind = seperator_finding(word_list)
    if(ind==-1):
      out = "What"+" "+aux + " " +" ".join(word_list[:])
    else:
      out = " ".join(word_list[:ind+1])+" "+"what"+" "+aux+" "+" ".join(word_list[ind+1:])

  # print(out)
  return out


  # ind = seperator_finding(word_list)
  # if(ind==-1):
  #   out = "From where" + " " +" ".join(word_list[:n-1])
  # else:
  #   out = " ".join(word_list[:ind+1])+" "+"from where"+" "+" ".join(word_list[ind+1:n-1])
  # print(out)
  # return out

def from_questions(text):
  """ Function for conversion of objective questions falling in 
  "from" category.

  Paramters
  ----------
  text: complete objective question after cleaning
  """
  
  word_list = nltk.tokenize.word_tokenize(text)
  n = len(word_list)
  ind = seperator_finding(word_list)
  if(ind==-1):
    out = "From where" + " " +" ".join(word_list[:n-1])
  else:
    out = " ".join(word_list[:ind+1])+" "+"from where"+" "+" ".join(word_list[ind+1:n-1])
  # print(out)
  return out

def because_questions(text):
  """ Function for conversion of objective questions falling in 
  "because" category.

  Paramters
  ----------
  text: complete objective question after cleaning
  """
  
  word_list = nltk.tokenize.word_tokenize(text)
  n = len(word_list)
  ind = seperator_finding(word_list)
  if(ind==-1):
    out = "Why" + " " +" ".join(word_list[:n-1])
  else:
    out = " ".join(word_list[:ind+1])+" "+"why"+" ".join(word_list[ind+1:n-1])
  # print(out)
  return out

def called_questions(text):
  """ Function for conversion of objective questions falling in 
  "called" category.

  Paramters
  ----------
  text: complete objective question after cleaning
  """
  
  word_list = nltk.tokenize.word_tokenize(text)
  n = len(word_list)
  arr = ["is",'are','was',"were"]

  if(n-2>=0 and word_list[n-2] in arr):
    ind = seperator_finding(word_list)
    if(ind==-1):
      out = "What" + " "+word_list[n-2] + " "+" ".join(word_list[:n-2])+" "+" ".join(word_list[n-1:])
    else:
      out = " ".join(word_list[:ind+1])+" "+"what"+" "+word_list[n-2]+" "+" ".join(word_list[n-1:])
    # print(out)
    return out

  elif(n-3>=0 and word_list[n-3] in arr):
    ind = seperator_finding(word_list)
    if(ind==-1):
      out = "What" + " "+word_list[n-3] + " "+" ".join(word_list[:n-3])+" "+" ".join(word_list[n-2:])
    else:
      out = " ".join(word_list[:ind+1])+" "+"what"+" "+word_list[n-3]+" "+" ".join(word_list[n-2:]) 
    # print(out)
    return out

  else:
    return "No Pattern Found"

def be_helper(text):
  """ Helper Function for conversion of objective questions falling in 
  "be" category. It is used to find a separator from end

  Return 
  ----------
  index: the index of the separator 
  """

  index = -1
  arr = ["would","should","will","shall","can"]
  endTokenIndex = len(text) - 1 if text[-1]=="." else len(text) - 2
  for i in range(endTokenIndex,-1,-1):
    if(text[i] in arr):
      return i
  return index

def be_questions(text):
  """ Function for conversion of objective questions falling in 
  "be" category.

  Paramters
  ----------
  text: complete objective question after cleaning
  """

  word_list = nltk.tokenize.word_tokenize(text)
  ind = seperator_finding(word_list)
  aux_verb_ind = be_helper(word_list)

  n = len(word_list)

  if(aux_verb_ind==-1):
    word_list.insert(n-1,"would")
    word_list[n] = ""
    aux_verb_ind = n-1
  if(ind!=-1):
    out =  " ".join(word_list[:ind+1])+" "+ "what"+" "+" ".join(word_list[aux_verb_ind:])+" "+" ".join(word_list[ind+1:aux_verb_ind])
  else:
    out =  "What"+" "+" ".join(word_list[aux_verb_ind:])+" "+" ".join(word_list[:aux_verb_ind])
  # print(out)
  return out

def to_questions(text):
  word_list = nltk.tokenize.word_tokenize(text)
  whWord = "Why"
  out = None
  (past_verb_index , past_verb) = past_verb_check(pos_tagging(text))
  aux_verb = 'does' if past_verb_index==None else "did"
  ind = seperator_finding(word_list)
  temp = 0 if ind==-1 else ind
  if(word_list[-2].strip()=="due"):
    # try:
    if(aux_verb_check(word_list[temp:]) != (None,None)):
      (index,aux_verb) = aux_verb_check(word_list)
      if(ind==-1):
        out = whWord +  " " + aux_verb + " " + " ".join(word_list[:index]) +  " "  + " ".join(word_list[index+1:-2])
      else:
        out = " ".join(word_list[:ind+1]) + " " + whWord +  " " + aux_verb + " " + " ".join(word_list[ind+1:index]) +  " "  + " ".join(word_list[index+1:-2])
    else:
      if(aux_verb=="did"):
        word_list.pop(past_verb_index)
        word_list.insert(past_verb_index,past_verb)
      if(ind==-1):
        out = whWord +  " " + aux_verb + " " + " ".join(word_list[:-2])
      else:
        out = " ".join(word_list[:ind+1]) + " " + whWord +  " " + aux_verb + " " + " ".join(word_list[ind+1:-2])
    # print(out)
    # except:
    #   continue

  return out
 
# !git clone https://github.com/gutfeeling/word_forms.git

# !pip install -e word_forms


def is_are_was_were_questions(text,lastWord):
  """ Function for conversion of objective questions falling in 
  "is/are/was/were" category.

  Paramters
  ----------
  text: complete objective question after cleaning
  """
  
  word_list = nltk.tokenize.word_tokenize(text)
  index = seperator_finding(word_list)
  if(index==-1):
    question = "What" + " " + lastWord +  " " + " ".join(word_list[:-1])
  else:
    question = " ".join(word_list[:index]) + ", " + "what" + " " + lastWord + " " +  " ".join(word_list[index+1:-1])
  # print(question)
  return question

def the_questions(text):
  """Function for conversion of objective questions falling in "the"
  category.

  Parameters
  -----------
  text: complete objective question after cleaning
  """

  from nltk.stem import WordNetLemmatizer 
  lemmatizer = WordNetLemmatizer() 
  word_list = nltk.tokenize.word_tokenize(text)
  last_word = text.split()[-1]
  second_last_word = text.split()[-2]
  auxilliary_verbs = ["is","are","was","were","has","have","can","should","do","would","will","does"]
  whWord = "What"

  if(second_last_word=="in" or second_last_word=="inside" or second_last_word=="into"):
    """ Handling particular sub-category of questions having their second-last word as
    "in" or some similar words such as "inside" or "into"
    """
    whWord = "Where"
  elif(second_last_word=="by"):
    ques = by_questions(" ".join(word_list[:-1]))

  flag = 0
  index = seperator_finding(word_list)
  for verb in auxilliary_verbs:
    if verb in word_list:
      ind = word_list.index(verb)
      if(index == -1):
        ques = whWord + " "  + verb + " " + " ".join(word_list[0:ind]) +  " " + " ".join(word_list[ind+1:len(word_list)-2])
      else:
        ques =  " ".join(word_list[0:index]) + whWord + " "  + verb + " " + " ".join(word_list[index:ind]) +  " " + " ".join(word_list[ind+1:len(word_list)-2])
      # print(ques)
      flag =  1
      break
  if(flag==0):
    past_verb_forms = ["VBD","VBN"]
    thirdPerson_verb_forms = ["VBZ"]
    check=0
    check2=0
    taggedList = pos_tagging(text)
    for tags in taggedList:
      if(tags[1] in past_verb_forms):
        check=1-check
        new_word = lemmatizer.lemmatize(tags[0],pos='v')
        ind = word_list.index(tags[0])
        word_list.remove(tags[0])
        word_list.insert(ind,new_word)
        if(index == -1):
          ques = whWord + " " + "did" +  " " + " ".join(word_list[0:-2])
        else:
          ques = " ".join(word_list[0:index]) + " " + whWord + " " + "did" +  " " + " ".join(word_list[index:-2])
        return ques
        # break
    if(check==0):
      for tags in taggedList:
        if(tags[1] in thirdPerson_verb_forms):
          check=1-check
          new_word = lemmatizer.lemmatize(tags[0],pos='v')
          index = word_list.index(tags[0])
          word_list.remove(tags[0])
          word_list.insert(index,new_word)
          if(index == -1):
            ques = whWord + " " + "does" +  " " + " ".join(word_list[0:-2])
          else:
            ques = " ".join(word_list[0:index]) + " " + whWord + " " + "does" +  " " + " ".join(word_list[index:-2])
          return ques
          # break
      if(check==0):
          
        if(index == -1):
          ques = whWord + " " + "does" +  " " + " ".join(word_list[0:-2])
        else:
          ques = " ".join(word_list[0:index]) + " " + whWord + " " + "does" +  " " + " ".join(word_list[index:-2])
        # print(ques)
        return ques

import pandas as pd

def by_helper(end,verb,start,Wh,flag = 0):
    """ Helper Function for conversion of objective questions falling in 
    "by" category. It concatenates the subarrays of the Objective question

    Paramters
    ----------
    verb: Verb which will be concatenated in front
    end: String after b in the cleaned objective question
    start: Cleaned Objective question from starting index upto the last verb i.e. b
    Wh: Wh- word to be concatnated in front
    flag: Indicate the order of concatenation

    Return 
    ----------
    out: Subjective Question
    """
    try:
      verb = [verb[0].values[0]]
    except:
      verb = verb
   
    ind = seperator_finding(start)
    if(ind!=-1 and flag==0):
      verb += start[ind+1:]
      start = start[:ind]
      out =" ".join(start) + " "+ Wh.lower() + " " + " ".join(verb + end)

    elif(ind!=-1 and flag==1):
      verb = start[ind+1:] + verb
      start = start[:ind]
      out = verb + end + start
      out = Wh + " " + " ".join(out)
    else:
      out = verb + end + start
      out = Wh + " " + " ".join(out)

    return out


verbs = pd.read_csv ('verbs.csv',sep="\t")
def by_questions(text):
  """ Function for conversion of objective questions falling in 
  "by" category.

  Paramters
  ----------
  text: complete objective question after cleaning
  """
  word_list = nltk.tokenize.word_tokenize(text)
  n = len(word_list)
  for i in range(n):
      word_list[i]=word_list[i].strip()

  # Removing the string "by" from end
  if(word_list[-1]=="by"):
    word_list = word_list[:-1]
    n = len(word_list)

  # Renaming the columns of csv file
  col = ["present_simple_1st", "present_simple_3rd","past_simple","past_participle","present_participle"]
  verbs.columns = col

  # Searching for the verb from end
  for i in range(n-1,-1,-1):
      
      question = ""
      flag = False
      temp = ""
      index = -1
      for j in range(4):
          if((verbs[col[j]] == word_list[i]).any()):
              temp = col[j]
              index = j
              flag = True
              break
      
      
      if(flag == True):

          # Found a verb

          if(word_list[i-1] == "is" or word_list[i-1] == "are" or word_list[i-1] == "am"):
    
              v = word_list[i]
              if(index == 2): # past_simple
                v = verbs[verbs[temp] == word_list[i]].present_simple_3rd
                question = by_helper([""],[""],word_list,"How")

              if(index == 3): # past_participle
                v = verbs[verbs[temp] == word_list[i]].past_simple
                question = by_helper(word_list[i+1:],[v],word_list[:i-1],"Who")
   
          elif(word_list[i-1] == "was" or word_list[i-1] == "were"):

              v = verbs[verbs[temp] == word_list[i]].past_simple
              question = by_helper(word_list[i+1:],[v],word_list[:i-1],"Who")
          
          elif(word_list[i-1] == "be"):
           
              v = verbs[verbs[temp] == word_list[i]].present_simple_1st     
              question = by_helper([""],[""],word_list,"How") 
       
          elif(word_list[i-1] == "being" and (word_list[i-2] == "is" or word_list[i-2] == "are" or word_list[i-2] == "am")):
     
              v = word_list[i-2] + " "+ verbs[verbs[temp] == word_list[i]].present_participle
              question = by_helper([""],[""],word_list,"How") 
           
          elif(word_list[i-1] == "been" and (word_list[i-2] == "has" or word_list[i-2] == "have")):
            
              v = word_list[i-2]+ " " + word_list[i]
              question = by_helper(word_list[i+1:],[v],word_list[:i-2],"How",1)
       
          else:
              return "No Pattern Found"
          
          try:
              question = question.values[0].replace(".","")
          except:
              question = question.replace(".","")
          
        
          question = nltk.tokenize.word_tokenize(question)
          n = len(question)
          for i in range(n):
              question[i] = question[i].strip()
          question = " ".join(question)

          # print(question)
          # print("================")
          return question

import nltk
# nltk.download('all')
# nltk.download('punkt')
""" Driver code for conversion of collected questions based on the category
"""
def compute(x):
  # notWh = []
  # print("#######",len(notWh))
  notWh = []
  notWh.append(x)
  notWh_ans.append("")
  mat = []
  count = 0
  print(len(notWh))
  for i in range(len(notWh)):
    # if(i%1000==0):
      # print("...")

    temp = []
    flag = 0
    last_word = x.split(" ")[-1]

    last_word = re.sub(r'[^\w\s]', '', last_word)
    last_word = re.sub(r'[ \t]', '', last_word)
    last_word = last_word.lower()
    notWh[i] = x[0].lower() + x[1:]
    # if(len(res)>0 and res.isalnum() and len(match)>0):
    #   if(res in freq):
    #     freq[res] += 1
    #   else:
    #     freq[res]=1
    

    in_synonym_words = ["in","inside","into"]
    commonCategories = ["is","are","was","were"]

    """Capturing "the/in/inside/into" cateogries"""
    if(last_word in in_synonym_words or last_word=="the"):
      # print("Given Objective Question:", notWh[i])
      # print("Answer to the objective Question:", notWh_ans[i])
      # print("Converted Question:",end=" ")
      text = notWh[i] + " " + "the"
      temp.append(notWh[i])
      temp.append(notWh_ans[i])
      temp.append(the_questions(text))
      # print("=============")

      """Capturing "be" cateogry"""
    elif(last_word=="be"):
      text = notWh[i]
      # print(notWh[i]," -------->",notWh_ans[i])
      temp.append(notWh[i])
      temp.append(notWh_ans[i])
      temp.append(be_questions(text))
      # be_questions(text)
      # print("==============")

      """Capturing "called" cateogry"""
    elif(last_word=="called"):
      text = notWh[i]
      # print(notWh[i]," -------->",notWh_ans[i])
      temp.append(notWh[i])
      temp.append(notWh_ans[i])
      temp.append(called_questions(text))
      # called_questions(text)
      # print("==============")

      """Capturing "because" cateogry"""
    elif(last_word=="because"):
      text = notWh[i]
      # print(notWh[i]," -------->",notWh_ans[i])
      temp.append(notWh[i])
      temp.append(notWh_ans[i])
      temp.append(because_questions(text))
      # because_questions(text)
      # print("==============")

      """Capturing "a" cateogry"""
    elif(last_word=="a"):
      text = notWh[i]
      # print(notWh[i]," -------->",notWh_ans[i])
      word_list = nltk.tokenize.word_tokenize(text)
      n = len(word_list)
      if(n-2>=0):
        if(word_list[n-2] in in_synonym_words):
          temp.append(notWh[i])
          temp.append(notWh_ans[i])
          temp.append(the_questions(" ".join(word_list[:n-1])+" "+"the"))
          
        elif(word_list[n-2] in commonCategories): 
          last_word_index = commonCategories.index(word_list[n-2])
          last_word = commonCategories[last_word_index]
          temp.append(notWh[i])
          temp.append(notWh_ans[i])
          temp.append(is_are_was_were_questions(" ".join(word_list[:n-1]),last_word))
          
        # print("==============")

      # """Not Done ---- Capturing "from" cateogry"""
    elif(last_word=="from"):
      text = notWh[i]
      temp.append(notWh[i])
      temp.append(notWh_ans[i])
      temp.append(from_questions(text))
      # print(notWh[i]," -------->",notWh_ans[i])
      
      # print("==============")

      # if(last_word=="then"):
      #   text = notWh[i]
      #   print(notWh[i]," -------->",notWh_ans[i])
      # #   from_questions(text)
      #   print("==============")

    

      """Capturing "as/for" cateogry"""
    elif(last_word=="for" or last_word=="as"):
      text = notWh[i]
      # print(notWh[i]," -------->",notWh_ans[i])
      temp.append(notWh[i])
      temp.append(notWh_ans[i])
      temp.append(as_for_questions(text))
      
        # print("==============")

    elif(last_word=="ftto" and "Math" not in notWh_bs[i]):   
      # print(notWh[i]," -------->",notWh_ans[i])
      # print(notWh_skill[i])
      # to_questions(notWh[i])
      # print("========================")
      temp.append(notWh[i])
      temp.append(notWh_ans[i])
      temp.append(to_questions(notWh[i]))



      # if(last_word=="of" and "Math" not in notWh_bs[i]):
      #   print(notWh[i]," -------->",notWh_ans[i])
          
        # form_question(notWh[i],notWh_ans[i],notWh_bs[i])
      
      """Capturing "on" category"""
    elif(last_word=="on"):
      # print(notWh[i]," -------->",notWh_ans[i])
      
      temp.append(notWh[i])
      temp.append(notWh_ans[i])
      temp.append(on_questions(notWh[i],notWh_ans[i]))
      # print("--------------------")

      """Capturing "is/are/was/were" categories"""
    elif(last_word in commonCategories):
      # print("Given Objective Question:", notWh[i])work music
      # print("Answer to the objective Question:", notWh_ans[i])
      # print("Converted Question:",end=" ")
      last_word_index = commonCategories.index(last_word)
      last_word = commonCategories[last_word_index]
            
      temp.append(notWh[i])
      temp.append(notWh_ans[i])
      temp.append(is_are_was_were_questions(notWh[i],last_word))
      
      # print("=============")

      """Capturing "by" category"""
    elif(last_word=="by"):
      # print("Given Objective Question:", notWh[i])
      # print("Answer to the objective Question:", notWh_ans[i])
      # print("Converted Question:",end=" ")
      temp.append(notWh[i])
      temp.append(notWh_ans[i])
      temp.append(by_questions(notWh[i]))
      # print(temp)
    if(len(temp)>0 and temp[2] is not None and temp[2].lower()!="no pattern found"):
      # print(temp[0])
      # input()
      # print(temp[1])
      # input()
      # print(temp[2])
      temp[0] = temp[0][0].upper() + temp[0][1:]
      temp[2] += " ?"
      temp[2] = temp[2][0].upper() + temp[2][1:]
      temp.append("")
      temp.append("")

      mat.append(temp)
    count += 1
  return mat,count
    # print()
# import pandas as pd
# mat,count = compute()
# # pr.int(mat)
# df = pd.DataFrame(mat)
# # print(df.head)
# df.columns = ["Objective Question","Answer", "Subjective Question" , "Score of Conversion" , "Possible Other Conversion (if any)"]
# df.to_csv(r'convertedQuestion.csv', index = False)
# print("Accuracy : ",len(mat)/count )
# count_correct = len(mat)
# print(count_correct, count_following, count_wh, count_other, count_hindi,count_notWh)
# print(mat)

def run(ques):
  ques = pre_process(ques)
  print(ques)
  if(ques!="Unable to resolve"):
    mat,count = compute(ques)
    print(mat)
    return mat[0][2]
  else:
    return None
