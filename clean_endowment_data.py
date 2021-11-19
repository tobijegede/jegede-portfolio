#import libraries
import pandas as pd
import numpy as np
import os
import re

year = 2011
filenames = []
#years = [] #used for creating the final combined dataframe
name = "endowment_data"
for i in range(7):
    year += 1
   # years.append(year)
    
    #create new filename
    file = name + "_" + str(year) + ".xls"
    filenames.append(file)
    
    
#retrieve the current directory
current_directory = os.getcwd()

#helper functions for the cleaning the data
def remove_nans(endow_list):  
    
    no_nans = [x for x in endow_list if pd.isnull(x) == False]
    return no_nans


def clean_ins(list_of_institutions):
    
    cleaned = []
    #remove the "..." & the (State_abbrev)
    for school in list_of_institutions:
        clean = re.sub("\." ,"", school) #removes the  "...."
        clean = re.sub("[\(\[].*?[\)\]]", "", clean) #removes parenthesis and everything inside
        clean = clean.strip() #removes the trailing whitespace
        cleaned.append(clean)
        
    return(cleaned)


#use a for loop to read in all of the data

df = {} #creates container for dataframe to hold the results of the below

for file in filenames:
    
    f = file.replace(".xls", "").split("_")
    year = [x for x in f if x.isdigit()][0]
    
    #step 1: read in the data 
    filepath = os.path.join(current_directory, file)
    endowment_data = pd.read_excel(filepath, header = 3, skipfooter = 6).drop([0,1,2]) #eliminates the header and the united states totals

    #step 2: separate the lists of colleges and join back together
    #-------- FIRST SET OF COLLEGES ----------- #

    institutions_part1 = endowment_data['Institution'].tolist() #names for first column of colleges
    institutions_part1_nonan = remove_nans(institutions_part1) #removes the "nan" values from the list

    endowment_part1 = endowment_data['End of FY (in thousands)'].tolist()
    endowment_part1_nonan = remove_nans(endowment_part1) #remove the "nan" values from the list

    #------- SECOND SET OF COLLEGES ------------ #
    institutions_part2 = endowment_data['Institution.1'].tolist()
    institutions_part2_nonan = remove_nans(institutions_part2)

    endowment_part2 = endowment_data['End of FY (in thousands).1'].tolist()
    endowment_part2_nonan = remove_nans(endowment_part2) #remove the "nan" values from the list


    #-------- COMBINE THE DATA INTO ONE DF -------- #

    #cleaned names for the  institutions
    clean_ins_1 = clean_ins(institutions_part1_nonan)
    clean_ins_2 = clean_ins(institutions_part2_nonan)

    all_institutions = clean_ins_1 + clean_ins_2
    all_endowments = endowment_part1_nonan + endowment_part2_nonan
    
    
    # ----- CREATE RESULTING DF ----- #
    ins_name = "institutions" + "_" + year
   # year_name = year + "_" + str(len(all_institutions))
   
    df[ins_name] = all_institutions
    df[year] = all_endowments

    
keys = ["institutions_2012", "2012"]
df_2012 = {x:df[x] for x in keys}
endow_2012 = pd.DataFrame(df_2012)

keys = ["institutions_2013", "2013"]
df_2013 = {x:df[x] for x in keys}
endow_2013 = pd.DataFrame(df_2013)

keys = ["institutions_2014", "2014"]
df_2014 = {x:df[x] for x in keys}
endow_2014 = pd.DataFrame(df_2014)

keys = ["institutions_2015", "2015"]
df_2015 = {x:df[x] for x in keys}
endow_2015 = pd.DataFrame(df_2015)

keys = ["institutions_2016", "2016"]
df_2016 = {x:df[x] for x in keys}
endow_2016 = pd.DataFrame(df_2016)

keys = ["institutions_2017", "2017"]
df_2017 = {x:df[x] for x in keys}
endow_2017 = pd.DataFrame(df_2017)

keys = ["institutions_2018", "2018"]
df_2018 = {x:df[x] for x in keys}
endow_2018 = pd.DataFrame(df_2018)



#merge the datasets together into one dataframe
all_schools = (pd.merge(endow_2012, endow_2013, 
                      how = "left", #will only use colleges from data from 2012
                     left_on = "institutions_2012",
                     right_on = "institutions_2013")
                .drop('institutions_2013', 1)
                .merge(endow_2014,
                      how = "left",
                      left_on = "institutions_2012",
                      right_on = "institutions_2014")
                .drop("institutions_2014", 1)
                .merge(endow_2015,
                      how = "left",
                      left_on = "institutions_2012",
                      right_on = "institutions_2015")
                .drop("institutions_2015", 1)
                .merge(endow_2016,
                      how = "left",
                      left_on = "institutions_2012",
                      right_on = "institutions_2016")
                .drop("institutions_2016", 1)
                .merge(endow_2017,
                      how = "left",
                      left_on = "institutions_2012",
                      right_on = "institutions_2017")
                .drop("institutions_2017", 1)
                .merge(endow_2018,
                      how = "left",
                      left_on = "institutions_2012",
                      right_on = "institutions_2018")
                .drop("institutions_2018", 1)
             )
#export
all_schools.to_csv(os.path.join(current_directory, "all_endowments.csv"), index = False)
 
