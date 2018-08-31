#6.5 Write code using find() and string slicing (see section 6.10)
#to extract the number at the end of the line below.
#Convert the extracted value to a floating point number and print it out.
#text = "X-DSPAM-Confidence:    0.8475";
data = 'X-DSPAM-Confidence:    0.8475'
popos = data.find('0')
piece = data[popos:]
print(piece)
fpiece = float(piece)
