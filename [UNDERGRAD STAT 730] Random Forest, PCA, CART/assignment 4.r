wine = read.csv("C:/Users/dgmur/Downloads/wineFl2022.csv")
str(wine)
wine$type=as.factor(wine$type)
wine$quality=as.numeric(wine$quality)
winec = wine[1:11]
View(winec)
#1

#a
cor(winec)

cov(winec)

#b

#I chose correlation because the variables are on a different scale

winec.pca = prcomp(winec, scale. = T)

winec.pca
#c
summary(winec.pca)

screeplot(winec.pca, type = "lines")
#10 PCs

#d

c=cor(winec, winec.pca$x)
round(c,2)

#PC1: Sulfur Dioxide

#PC2: Density of Alcohol by amount of sugar

#PC3: PH level of acidity

#PC4: PH level of sulfur containing bases 

#PC5: Ph level of volatile acidity and choloride

#PC6: Chlorides residual sugar and acidity based on alcohol percantage

#PC7: PH level of volatile, citric acid and sulphate

#PC8: fixed acidity and residual sugar based on percentage of alcohol

#PCA9: acidity, chlorides and sulfur dioxide

#PCA10: Sulfur dioxide
#e 

#No, the proportion of variance is too low, and too close to PC2. PC1 has a 27% proportion of variance,while PC has 23.4%

#F 

plot(winec.pca$x[,1:2])

#There are no distingiuishing groups, however, there is an outlier that is skewed to the higher end of PC1

#bonus 

qqnorm(winec.pca$x)

#The plot shows that the distribution is not normal, this shows evidence of high variation.


#2

#a
wined = wine[-13]

cor(wined)

cov(wined)

#b I chose correlation maxtrix because the variables are not one the same scale. 

wine.pca = prcomp(wined,scale. = T)

wine.pca


#c
summary(wine.pca)

screeplot(wine.pca, type="lines")

#d

#10 PCs, however, I could get away with 9 PCs in comparison to question 1 due to PC9 in PC2 has a lower variance explained

#e
d=cor(wined, wine.pca$x)

round(d,2)

#PC1: Wine type based of acidity, chlorides and sulfur dioxide 

#PC2: Amount of density based on percentage of alcohol and residual sugar

#PC3: Acidity based on PH level and quality 

#PC4: Amount of sulphates based on quality and PH level

#PC5: Quality based on Residual sugar and chlorides

#PC6: Average Ph level based on percentage of  volatile acidity and free sulfur dioxide

#PC7: PH level of acidity 

#PC8: Total Amount of residual sugars, chlorides and citric acid based on percentage of alcohol

#PC9: Quality based Sulphates and residual sugar

#PC10: Amount of Volatile Acidity based on quality of alchohol

#Yes, my intepretations do differ, categorical variable dominated the PCs

#F 

summary(wine.pca)

#No, the proportion of variance is too close in proportion of variance to PC2


#G 

plot(wine.pca$x[,1:2])
#There are distinguishable groups, and there is one outlier on the PC1 axis. There is a difference compared to question one because the groups are distinuishable


#Bonus 
#I would prefer with categorical variables because it more easier to interpret relationships in each PC. An alternative method would be creating subsets for the data based factors of the categorical variables, and then use PCA for each subset.


#3 

library(rpart)
library(rpart.plot)



#a
wine$quality=as.factor(wine$quality)

fit= rpart(quality~., method = "class", data=wine)

printcp(fit)

plotcp(fit)

summary(fit)

pfit<- prune(fit, cp=fit$cptable[which.min(fit$cptable[,"xerror"]),"CP"])

#b
prp(pfit,main = "Pruned Classification Tree for Wine Qualities")

#The predicted the wine quality would be a 6

#c
library(randomForest)
set.seed(478)

wine$quality=as.factor(wine$quality)

x = randomForest(quality~., data=wine)

plot(x)

t = tuneRF(wine[,-12],wine[,12],
           stepFactor = 0.7, plot = TRUE,
           ntreeTry = 300,
           trace = TRUE,
           improve=1)

x1 = randomForest(quality~., ntree=300,mtry=3,nodesize=2, data=wine)
print(x1)
x2 = randomForest(quality~., ntree=300,mtry=2,nodesize=2,data=wine)
print(x2)

x3 = randomForest(quality~., ntree=300,mtry=5,data=wine)
print(x3)


plot(x3)
#x3 had the lowest oob error rate 



#I chose x3

#d
a = data.frame(fixed_acidity = 8, volatile_acidity = 0.6, citric_acid = 0.6, residual_sugar = 15, chlorides = 0.3,
                free_sulfur_dioxide = 50, total_sulfur_dioxide = 200, density = 1, pH = 3.5, sulphates = 0.75, 
                alcohol = 10, type=factor("1",c(0:1)))

b=predict(x3, a, interval="predict", level=0.95)

b

#E 

printcp(pfit)

print(x3)

#The classification tree predicted 6 while the random forest predicted 5. The error rate for
# the CT was about 56.5% while, RF was about 48% 


bikes = read.csv("C:/Users/dgmur/Downloads/SeoulBikes_Fl2022.csv")

dim(bikes)

bikes = bikes[4:16]

x.new <- data.frame(Holiday=factor("Holiday", c("Holiday", "No Holiday")), 
                    Seasons=factor("Spring", c("Autumn", "Spring", "Summer", "Winter")),
                    Functioning.Day=factor("Yes",c("No","Yes")),
                    Temperature=12.1, Humidity=29, WindSpeed=2.3,
                    Visibility=1734, DewPointTemp=-5.4, SolarRadiation=2.26,
                    Rainfall=0, Snowfall=0, 
                    DayF=factor("21",c(1:31)), MonthF=factor("3",c(1:12)), 
                    Time=factor("Morning",c("Morning","Evening")))

str(bikes)

bikes$Seasons= as.factor(bikes$Seasons)

bikes$Holiday= as.factor(bikes$Holiday)

bikes$Functioning.Day=as.factor(bikes$Functioning.Day)

bikes$Time=as.factor(bikes$Time)


#a

fit2= rpart(RentedBikeCount~., method = "anova", data=bikes)

printcp(fit2)

plotcp(fit2)

summary(fit2)

pfit2<- prune(fit2, cp=fit$cptable[which.min(fit$cptable[,"xerror"]),"CP"])

#b
prp(pfit2,main = "Pruned Classification Tree for Wine Qualities")
 #tree predicted 1486 

#c
set.seed(55)


z = randomForest(RentedBikeCount~., data=bikes)
plot(z)

t2 = tuneRF(wine[,-4],wine[,4],
           stepFactor = .5, plot = TRUE,
           ntreeTry = 400,
           trace = TRUE,
           improve=1)

z1 = randomForest(RentedBikeCount~., ntree=400,mtry=8,nodesize=2, data=bikes)
print(z1)

z2 = randomForest(RentedBikeCount~., ntree=400,mtry=8,nodesize=1, data=bikes)
print(z2)

z3 = randomForest(RentedBikeCount~., ntree=400,mtry=8,nodesize=5, data=bikes)
print(z3)

#I selected z2 

plot(z2)

#d 
zp=predict(z1, x.new, interval="predict", level=0.95)
zp
#RF predicted 1147.564

#E
printcp(pfit2)

print(z2)

#The regression tree had a rootnode error rate of 100% and rf had a 69% variance explained
zp 
# regression tree predicted 1486 while rf was 1147.564
