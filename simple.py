from flask import Flask, request, render_template, session, redirect

import pandas as pd
import json
import requests


app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'])
def html_table():
    url='https://inf551-faa51.firebaseio.com/vgsales.json'
    response = requests.get(url)
    k=json.dumps(response.json(), indent=4)
    k_=json.loads(k)
    df=pd.DataFrame(k_)
    df = df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]


    return render_template('simple.html',  tables=[df.to_html(classes='data', header="true",index=False)])

@app.route('/name_asc',methods = ['POST', 'GET'])
def sorter_name_asc():
    NameSort=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json')
    name=json.dumps(NameSort.json(),indent=4)
    name_=json.loads(name) 
    name_df=pd.DataFrame(name_)
    name_df = name_df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
    name_df=name_df.sort_values(by='Name')
    return render_template('name_sort.html',  tables=[name_df.to_html(classes='data', header="true",index=False)])

@app.route('/name_des',methods = ['POST', 'GET'])
def sorter_name_des():
    NameSort=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json')
    name=json.dumps(NameSort.json(),indent=4)
    name_=json.loads(name) 
    name_df=pd.DataFrame(name_)
    name_df = name_df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
    name_df=name_df.sort_values(by='Name',ascending=False)
    return render_template('name_sort.html',  tables=[name_df.to_html(classes='data', header="true",index=False)])


@app.route('/publisher_asc',methods = ['POST', 'GET'])
def pub_name_asc():
    PublisherSort=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json')
    publisher=json.dumps(PublisherSort.json(),indent=4)
    publisher_=json.loads(publisher) 
    publisher_df=pd.DataFrame(publisher_)
    publisher_df = publisher_df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
    publisher_df=publisher_df.sort_values(by='Publisher')
    return render_template('publisher_sort.html',  tables=[publisher_df.to_html(classes='data', header="true",index=False)])

@app.route('/publisher_des',methods = ['POST', 'GET'])
def pub_name_des():
    PublisherSort=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json')
    publisher=json.dumps(PublisherSort.json(),indent=4)
    publisher_=json.loads(publisher) 
    publisher_df=pd.DataFrame(publisher_)
    publisher_df = publisher_df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
    publisher_df=publisher_df.sort_values(by='Publisher',ascending=False)
    return render_template('publisher_sort.html',  tables=[publisher_df.to_html(classes='data', header="true",index=False)])

@app.route('/NA_Sales_asc',methods = ['POST', 'GET'])
def nasales_name_asc():
    NA_SalesSort=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json')
    nasales=json.dumps(NA_SalesSort.json(),indent=4)
    nasales_=json.loads(nasales) 
    nasales_df=pd.DataFrame(nasales_)
    nasales_df = nasales_df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
    nasales_df=nasales_df.sort_values(by='NA_Sales')
    return render_template('nasales_sort.html',  tables=[nasales_df.to_html(classes='data', header="true",index=False)])


@app.route('/NA_Sales_des',methods = ['POST', 'GET'])
def nasales_name_des():
    NA_SalesSort=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json')
    nasales=json.dumps(NA_SalesSort.json(),indent=4)
    nasales_=json.loads(nasales) 
    nasales_df=pd.DataFrame(nasales_)
    nasales_df = nasales_df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
    nasales_df=nasales_df.sort_values(by='NA_Sales',ascending=False)
    return render_template('nasales_sort.html',  tables=[nasales_df.to_html(classes='data', header="true",index=False)])


@app.route('/EU_Sales_asc',methods = ['POST', 'GET'])
def eusales_name_asc():
    EU_SalesSort=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json')
    eusales=json.dumps(EU_SalesSort.json(),indent=4)
    eusales_=json.loads(eusales)
    eusales_df=pd.DataFrame(eusales_)
    eusales_df = eusales_df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
    eusales_df=eusales_df.sort_values(by='EU_Sales')
    return render_template('eusales_sort.html',  tables=[eusales_df.to_html(classes='data', header="true",index=False)])

@app.route('/EU_Sales_des',methods = ['POST', 'GET'])
def eusales_name_des():
    EU_SalesSort=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json')
    eusales=json.dumps(EU_SalesSort.json(),indent=4)
    eusales_=json.loads(eusales)
    eusales_df=pd.DataFrame(eusales_)
    eusales_df = eusales_df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
    eusales_df=eusales_df.sort_values(by='EU_Sales',ascending=False)
    return render_template('eusales_sort.html',  tables=[eusales_df.to_html(classes='data', header="true",index=False)])

@app.route('/gn_filter', methods = ['POST', 'GET'])
def my_form_post():
    text = request.form['text']

    genre=['Sports' ,'Platform', 'Racing', 'Role-Playing', 'Puzzle', 'Misc', 'Shooter',
 'Simulation' ,'Action', 'Fighting', 'Adventure', 'Strategy']
    word_low=text.lower()
    genre_low=[x.lower() for x in genre]
    flist2=[]
    for i in genre_low:
        if word_low in i:
            flist2.append(genre[genre_low.index(i)])
            
    if not flist2:
        return render_template('error2.html')

    
    else:
        genre_tot=pd.DataFrame(columns=['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'])

        GenreFilter=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json?orderBy="Genre"')
        genre=json.dumps(GenreFilter.json(),indent=4)
        genre_=json.loads(genre)
        genre_df=pd.DataFrame(genre_)
        genre_df = genre_df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
        for x in flist2:
            gen_df=genre_df[genre_df['Genre']==x]
            genre_tot=pd.concat([genre_tot,gen_df])
        
        return render_template('genre_filter.html',  tables=[genre_tot.to_html(classes='data', header="true",index=False)])

@app.route("/yr_filter", methods = ['POST', 'GET'])
def test():
    yr_tot=pd.DataFrame(columns=['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'])
    yr_range=[]
    text1 = request.form["Dropdown1"]
    text2 = request.form["Dropdown2"]
    text1_=int(text1)
    text2_=int(text2)
    if text1_ > text2_:
        return render_template('error.html')
    
    else:    
        for x in range(text1_,text2_+1):
            yr_range.append(x)
        
        YearFilter=requests.get('https://inf551-faa51.firebaseio.com/vgsales.json?orderBy="Year"')
        yr=json.dumps(YearFilter.json(),indent=4)
        yr_=json.loads(yr)
        yr_df=pd.DataFrame(yr_)
        yr_df = yr_df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
        for i in yr_range:
                yr_df1=yr_df[yr_df['Year']==i]
                yr_tot=pd.concat([yr_tot,yr_df1])
   
        yr_tot=yr_tot.sort_values(by='Year')
   
        return render_template('yr_filter.html',  tables=[yr_tot.to_html(classes='data', header="true",index=False)])

    

if __name__ == '__main__':
    app.run()
    
    
