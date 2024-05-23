import streamlit as st

st.set_page_config(
     page_title="Welcome"
)

st.sidebar.write("### GitHub")
st.sidebar.write("##### Pozri kód tu:")
st.sidebar.write("https://github.com/sorujko/WordCount")

st.write("# Nazdar močky! 👋")

html_code = '''
<div class="tenor-gif-embed" data-postid="14884815" data-share-method="host" data-aspect-ratio="1.77778" data-width="100%"><a href="https://tenor.com/view/bejr-majsner-psychopat-bejr-rage-gif-14884815">Bejr Majsner GIF</a>from <a href="https://tenor.com/search/bejr-gifs">Bejr GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
'''

show_html = st.toggle("Show/Hide Video" , value=1)

if show_html:
    st.components.v1.html(html_code, width=600, height=337)


st.write("#### Weather forecast - počasie")
st.write(""" 
Cygeneruje vám počasie na február a marec.
""")
if st.button("Weather forecast" , key=15641165):
    # Redirect to "/grafy" when the button is clicked
    st.markdown('<meta http-equiv="refresh" content="0; URL=/weather_forecast" />', unsafe_allow_html=True)
    
st.write("#### Text zo stránok - text extract")
st.write(""" 
Extrahuje text z url , ktoré sa nachádzajú v txt súbore.
""")
if st.button("Text zo stránok", key=4445):
    # Redirect to "/grafy" when the button is clicked
    st.markdown('<meta http-equiv="refresh" content="0; URL=/text_extract" />', unsafe_allow_html=True)
    
st.write("#### 1. Úloha - word counter")
st.write(""" 
Zo súboru Noviny  
1.vyberte časť napr. 1-3 strany údaje týkajúce sa 3 zdrojov vyhľadajte najčastejšie opakujúce sa slová  
2.vytvorte tabuľku  
3.vypočítajte základné štatistické charakteristiky
""")
st.write("<p style='color:red'>V bode č.1 nepoužijeme len 3 strany ale celý náš kontent</p>", unsafe_allow_html=True)
if st.button("1. Úloha - word counter", key=98753):
    
    st.markdown('<meta http-equiv="refresh" content="0; URL=/word_counter" />', unsafe_allow_html=True)
st.write("#### 2. Úloha - crypto_funny_staff")
st.write("""
Zo súboru Komodity  
1.vyberte časť údajov napr. 20 dní  
2.vytvorte tabuľku  
3.vypočítajte základné štatistické charakteristiky  
4.Vytvorte kontingenčnú tabuľku početností jednotlivých hodnôt pre každú komoditu  
početností intervalov hodnôt pre každú komoditu
""")
st.write("<p style='color:red'>Bod č.4 je nejaká blbosť , to sa robiť nebude</p>", unsafe_allow_html=True)
if st.button("2. Úloha - crypto_funny_staff",key=987537):
    
    st.markdown('<meta http-equiv="refresh" content="0; URL=/crypto_funny_staff" />', unsafe_allow_html=True)
st.write("#### 3. Úloha - Correlation matrix")
st.write("""
1.Vytvorte graf zmeny počtu hľadaných slov podľa času  
2.Vytvorte graf zmeny kurzu podľa času  
3.Vypočítajte model zmeny jednotlivých veličín  
4.Vypočítajte koreláciu medzi vybraným slovom a vybranou komoditou  
5.Nájdite najväčšiu závislosť komodity a používaného slova
""")
st.write("<p style='color:red'>Bod č.2 sme slpnili v crypto_funny_staff</p>", unsafe_allow_html=True)
st.write("<p style='color:red'>Bod č.3 nedáva zmysel</p>", unsafe_allow_html=True)
st.write("<p style='color:red'>Bod č.5 si sami vyznačíte v korelačnej matici v Exceli(najvačšia hodnota)</p>", unsafe_allow_html=True)
if st.button("3. Úloha - Correlation matrix",key=98753487933):
    
    st.markdown('<meta http-equiv="refresh" content="0; URL=/korelacia" />', unsafe_allow_html=True)