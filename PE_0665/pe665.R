# PE 0665
# February 2020
# Michael Hunt

library(tidyverse)

df<-read_csv('pe665.csv')
names(df)<-c('n','m','branch')
glimpse(df)

df<-mutate(df,ratio=m/n)
df<-mutate(df,delta=m-n)
glimpse(df)

hilo<-filter(df,branch!='wt')
hilo100<-filter(df,branch!='wt',m+n<=100)
hilo200<-filter(df,branch!='wt',m+n<=200)
wythoff<-filter(df,branch=='wt')

dflow<-filter(df,branch=='low')
dfhigh<-filter(df,branch=='hi')


g0<-ggplot(wythoff,aes(x=n,y=m))+
geom_point(size=2)+
  # geom_smooth(method = "lm", se = FALSE)+
  theme_bw()
g0

M=200
g1<-ggplot(filter(df,n+m<=M),aes(x=n,y=m,colour=branch))+
  geom_point(size=3)+
  geom_smooth(method = "lm", se = FALSE)+
  theme_bw()
g1

fithigh<-lm(m~0+n,data=filter(df,hilow=='hi'))
fitlow<-lm(m~0+n,data=filter(df,hilow=='low'))
dflow<-df %>% filter(hilow=='low') %>% mutate(fit=predict(fitlow))
dfhigh<-df %>% filter(hilow=='hi') %>% mutate(fit=predict(fithigh))

dflow<-mutate(dflow,diff=abs(fit-m)/m)

dfhigh<-mutate(dfhigh,diff=abs(fit-m)/m)

dflow100=filter(dflow,n+m<=100)
sum(dflow100$n)+sum(dflow100$m)

dfhigh100=filter(dfhigh,n+m<=100)

sum(dfhigh100$n)+sum(dfhigh100$m)
fithigh$coefficients  
fitlow$coefficients 
 
glow<-ggplot(filter(dflow,n>0),aes(x=n,y=m))+
  geom_point()+
  geom_line(aes(y = fit), size = 1,colour='red')+
  theme_bw()
glow

glowdiff<-ggplot(filter(dflow,diff<0.1),aes(x=n,y=diff))+
  geom_point()+
  ggtitle('glow diff')+
  theme_bw()
glowdiff

ghigh<-ggplot(dfhigh,aes(x=n,y=m))+
  geom_point()+
  geom_line(aes(y = fit), size = 1,colour='blue')+
  theme_bw()
ghigh

ghighdiff<-ggplot(filter(dfhigh,diff<0.1),aes(x=n,y=diff))+
  geom_point()+
  ggtitle('ghigh diff')+
  theme_bw()
ghighdiff

glow_ratio<-ggplot(filter(dflow,n>0),aes(x=n,y=ratio))+
  geom_point()+
  ggtitle('glow ratio')+
  theme_bw()
glow_ratio

ghigh_ratio<-ggplot(filter(dfhigh,diff<0.1),aes(x=n,y=ratio))+
  geom_point()+
  ggtitle('ghigh ratio')+
  theme_bw()
ghigh_ratio

