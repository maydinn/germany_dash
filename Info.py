import streamlit as st
from datetime import datetime

#set the page config
st.set_page_config(layout='wide', initial_sidebar_state='expanded',page_title="dofe.mi4people",
    page_icon="🇩🇪")

    


with open('visits.csv', 'a+') as f:    #Append & read mode
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(f"{timestamp}\n")
    st.write(timestamp)
    
st.sidebar.header('MI4People')
#st.subheader('Indicator')


st.sidebar.markdown('''
---
Made with ❤️ 

''')
import csv
from datetime import datetime


st.header("""
DOfE
""")

st.subheader("""
Data Open for Everyone 
""")



st.write('**Wir machen Daten zugänglich für alle**')

st.write("""
In der heutigen global vernetzten Welt ist die Nutzung von Daten zu einem integralen Bestandteil unseres täglichen Lebens geworden und dringt in nahezu jeden Aspekt vor. Wirtschaftliche Indikatoren spielen dabei eine herausragende Rolle und sind fester Bestandteil unserer Alltagsroutinen geworden. Gespräche über Themen wie Inflation, wirtschaftliche Stabilität und globale Wirtschaftstrends sind mittlerweile alltäglich geworden. Ein häufiges Problem besteht jedoch darin, dass die Indikatoren, mit denen wir tagtäglich konfrontiert sind, oft zu allgemein gehalten sind. Wir hören vielleicht von globalen Phänomenen wie steigenden Temperaturen oder sich ändernden Wettermustern, aber es fehlt uns oft ein klares Verständnis dafür, was in unserer unmittelbaren Umgebung geschieht. Diese Webseite untersucht die Bedeutung der Präsentation von wirtschaftlichen und wetterbezogenen Indikatoren auf lokaler Ebene, am Beispiel der deutschen Bundesländer, und stellt Erklärungen bereit, um Bürgerinnen und Bürgern wertvolle Einblicke zu vermitteln.
""")

