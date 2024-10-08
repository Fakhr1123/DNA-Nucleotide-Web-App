import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

image= Image.open('dna-logo.jpg')

st.write(""" 
# DNA Nucleotide Web App
         
This app count the Nucleotide composition query of DNA!
         
***
""")

st.header("Enter DNA Sequence")

sequence_input= ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence= st.text_area("Sequence Input", sequence_input, height= 250)

sequence= sequence.splitlines()

sequence= sequence[1:]

sequence= ''.join(sequence)

st.write("""
***
""")

st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (DNA Nucleotide Count)')
st.subheader('1. Print Dictionary')
def DNA_Nuleotide_Count(seq):
    d= dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X= DNA_Nuleotide_Count(sequence)

X

st.subheader('2. Print Text')
st.write('There are '+ str(X['A']) + ' adenine(A)')
st.write('There are '+ str(X['T']) + ' thymine(T)')
st.write('There are '+ str(X['G']) + ' guanine(G)')
st.write('There are '+ str(X['C']) + ' cytosine(C)')

st.subheader('3. Display DataFrame')
df= pd.DataFrame.from_dict(X, orient='index')
df= df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df= df.rename(columns= {'index' : 'nucleotide'})
st.write(df)

st.subheader('4. Display Bar Chart')
p= alt.Chart(df).mark_bar().encode(
x='nucleotide',
y='count'
)

p=p.properties(
    width= alt.Step(80) 
)

st.write(p)


