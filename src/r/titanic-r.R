print("Installing readr")
library(readr)

print("Import training dataframe")
train_df <- read_csv("src/data/train.csv")

print("See first few rows of training data")
head(train_df) #See structure of training data
print("See summary statistics of training data")
summary(train_df) #See summary statistics of training data

print("Removing all rows where Age is NA")
train_df <- train_df[!is.na(train_df$Age), ] #Removing all rows where Age is NA

print("Creating a dummy variable for Sex called Sex_dummy")
train_df$Sex_dummy <- ifelse(train_df$Sex  == "male", 0, 1) #Creating a dummy variable for Sex

print("Creating logistic regression model with Age, PClass, and Sedx_dummy as independent variables and Survived as dependent variable")
model <- glm(Survived ~ Age + Pclass + Sex_dummy, data = train_df, family = binomial) #Creating logistic regression model

print("Calculating accuracy of training model")
train_df$pred_prob <- predict(model, type = "response") #Getting predicted probabilities
train_df$pred_class <- ifelse(train_df$pred_prob > 0.5, 1, 0) #Converting predicted probabilities to 0, 1 responses
accuracy <- mean(train_df$pred_class == train_df$Survived) #Calculating proportion of correctly predicted cases
accuracy

print("Loading in test data and repeating data cleaning and wrangling steps")
test_df <- read_csv("src/data/test.csv") #Import testing dataframe

test_df <- test_df[!is.na(test_df$Age), ] #Removing all rows where Age is NA
test_df$Sex_dummy <- ifelse(test_df$Sex  == "male", 0, 1) #Creating a dummy variable for Sex

print("Applying model to test data")
test_df$pred_prob <- predict(model, newdata = test_df, type = "response") #Apply model to test data
test_df$pred_class <- ifelse(test_df$pred_prob > 0.5, 1, 0) #Converting probalities to 0, 1 variable

print("Outputting Passenger ID and predicted class for test data frame into csv")
output <- test_df[, c("PassengerId", "pred_class")] #Creating output dataframe
write.csv(output, "output_r.csv", row.names = FALSE)

