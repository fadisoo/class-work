# Chapter 6 Exercises:

str = 'X-DSPAM-Confidence:0.8475'
atpos = str.find(':')
print(atpos)

close_up = str[atpos + 1:]
numb = float(close_up)
print(numb)