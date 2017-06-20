from flask import Blueprint

Learn = Blueprint('Result' , __name__)

@Learn.route('/lsa')

def home3():
    return render_template('index3.html')



def process(res):
    ex = res
    snt= sent_tokenize(ex)
    wrd= word_tokenize(ex)
    fdist1 = FreqDist(wrd)
    no_of_t=0
    no_of_s=0
    l=0
    s= []
    kt= []
    f= []
    g= []
    m= []
    count=0
    dis=0
    bnt=0
    jnt=0
    vnt=0
    smm=0
    tr= []
    fic=0
    for i in wrd:
        no_of_t = no_of_t +1 ;
    #print(no_of_t)    
    for i in snt:
        no_of_s = no_of_s +1 ;  
    for j in snt:
        u=word_tokenize(j)
        for k in u:
            tf= fdist1[k]/no_of_t
            idf= math.log(no_of_s/tf)
            l=l+(tf*idf)
            count=count+1 
        s.append(l/count)   
        count=0

    for h in s:
     print(h)
     

    if no_of_s<=20:
        a=no_of_s-4
    else:
        a=no_of_s-20

    #print(a)


    for num in range(0,a):
        f.append(s[num])
        g.append([])
    #print(f)
    for qq in range(0,10):
        for w in s:
            for y in f:
                v=w-y
                if bnt==0:
                   dis=abs(v)
                   #print(dis)
                   bnt=bnt+1
                   g[jnt].append(w)
                   jnt=jnt+1
                elif abs(v)<dis:
                    g[jnt-1].remove(w)
                    dis=abs(v)
                    #print(dis)
                    g[jnt].append(w)
                    jnt=jnt+1
            jnt=0
            bnt=0
        for uj in range(a):
            aa=sum(g[uj])
            bb=len(g[uj])
            f[uj]=aa/bb 
            if qq<9:
                g[uj]=[]
        
        
        
    #print(g)

    for rr in range(a):
        if sum(g[rr])>smm:
            smm=sum(g[rr])
            m=g[rr]
            
        
    #print(m)    
    ws=len(s)
    qqq=len(m)
    #print(ws)
    for ee in range(ws):
        #print(ee)
        for cc in range(qqq):
            if m[cc]==s[ee]:
               tr.append(ee)
    #print(tr)
    wa=len(tr)

     
    for zz in tr:
        kt.append(snt[zz])  
        fic=fic+1

        
    print("No of sentences in original passage",ws)
    print("Nu52mber of Sentences in summary made by our approach",fic)
    print("% of size of text in summary by our approach",(fic/ws)*100)
    print (time.clock() - start_time, "seconds")

    return kt



#lxa
def process2(ex):
    file = "input.txt"
    kt=[]
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    summarizer = LexRankSummarizer()

    summary = summarizer(parser.document, ex)

    for sentence in summary:
        kt.append(sentence)


    print (time.clock() - start_time, "seconds")

    return kt




#lsa function
def process3(ex):
    kt=[]
    LANGUAGE = "english"
    SENTENCES_COUNT = ex
    parser = PlaintextParser.from_file("inputtext.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        kt.append(sentence)
    print (time.clock() - start_time, "seconds")

    return kt






