## Step 1: Find A Visualization + Its Associated Data


### Overview 
I was inspired to recreate data on the livability index in Pittsburgh because it was something that I was taken aback by when I first moved to the city. Pittsburgh's outcomes for Black and White residents is drastically different, leading  Mayor Bill Peduto to acknowledge in his 2020 Mayoral 
bid video that many residents in the city feel as though there is a "white Pittsburgh" and a "black Pittsburgh" [^1]. Pittsburgh is a city of stark constrasts -- the city has repeatedly been listed on "Most Livable Cities" lists while there have also been articles noted that the life characteristics of **black women** would change drastically by *just* picking up and leaving Pittsburgh for greener pastures [^2]. The City of Pittsburgh's Gender Equity Commitee Released a report in September of 2019 highlighting this "livability" divide further across dimensions such as health outcomes, educational outomces, and career outcomes. [^3]

For the purposes of this recretation, I focused on the health outcome disparties for black women in Pittsburgh, because this data all came from the same dataset, the National Vital Statistics System. The Bloomberg CityLab article that the following visualizations came from is this one: https://www.bloomberg.com/news/articles/2019-09-20/how-pittsburgh-fails-black-women-in-6-charts. 

### Original Visualizations
Here is the original infant mortality rate visualization from the Bloomberg CityLab article. The title of the visualization is "Infant mortality rate, Pittsburgh vs peer cities". From the original report associated with the visualization, there were "89 cities of similar size and characteristics nationwide" that were used as the unit of comparison.


![Image of Infant Mortality](infant_mort.png)




### Data Source Description

National Vital Statistics System.

~~From the equity report that was released, fetal mortality is defined as: "Fetal death includes any spontaneous intrauterine death of a fetus at any time during pregnancy. In Pennsylvania, all pregnancies at least 16 weeks past gestation that end in a fetal death are recorded. This includes "stillbirths" or fetuses born 20 weeks after gestation who demonstrate no signs of life at birth. We calculated fetal mortality as the number of fetal deaths divided by the number of pregnancies within the year. We calculated pregnancies within the year as the total number of babies born plus the number
of fetal deaths. In other words, pregnancies that end before 16 weeks after gestation are not included."~~

The equity report defines infant mortality in the following way:
**infant mortality**: We define the infant mortality rate as the number of babies under the age of one that pass away in a
given year divided by the number of live births in that year.


To access the data, I visited the following website: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm and downloaded the 2019 birth files data


## Step 2: Critique the Visualization


**Usefulness** -- this infor
**Completeness** 

**Perceptibility**

**Truthfulness** -- a certain inability to fact check or interrogate the extent of the validity of the gaps in the data because of the lack of visual information provided.

**Intuitiveness** -- I think about this in the context of "how quickly can I craft a 1 sentence summary about the graph" -- I can do this very quickly -- black women have worse infant mortality outcomes in Pittsburgh than both the other racial categories in pittsburgh and worse than infant mortality rates for other black women in other peer cities.

**Aesthetics** - generally pretty simple but could even use brighter colors to make some part of the data 

**Enagement** - (with some aestheic enhancement with brighter colors), it could engage the reader even more than it currently does because there is a grave disparity shown but using the same color for all of the Pittsburgh diamond makes it seem like the issue with high infant mortality rates for black women seems potenitally problematic.



### Question 1: Describe your overall observations about the data visualization here. What stood out to you? What did you find worked really well? What didn't? What, if anything, would you do differently?


In both of the above visualizations, I think their strength is also their weakness in some regard -- simplicity. The first words that come to mind when I see this visualization are "simplicity" and "minimalism".

The double-edged sword of this simplicity is that it is a bit unclear on what scale the data is measured in as well as what exactly is being considered a "similar" city.


This visualization seems to suffer from the paradox of being so simple that it becomes unclear, similar to the "simple, unclear bar chart" from the Crafting for Clarity chapter of "Good Charts".

It is also unclear what year the data displayed is from, as it is not listed in the title of the chart nor is it clearly highlighted in the related article. It is assumed that the  data is from 2019, given that this was the year in which the newspaper article was written.


### Question 2: Who is the primary audience for this tool? Do you think this visualization is effective for reaching that audience? Why or why not? *

The primary audience for this tool is likely Pittsburgh residents who are not already aware of the disparties that exist in the city. Generally, I think this visualization is effective at reaching the audience because it presents the diff






### Question 3: how successful what this method at evaluating the data visualization you selected? Are there measures you feel are missing or not being captured here? What would you change? Provide 1-2 recommendations (color, type of visualization, layout, etc.)


My initial reaction to the above visualization was that I was pleased by how the overall simplicity and minimalism of the deisgn. The use of the faint gray line also indicated immediately to be that there was some baseline or average from which a deviation in the data was being measured. Additionally, the visualization uses a simple diamond to point out Pittsburgh's position along the line, where it is compares to other similar sized cities.


The general approach that I'm taking in this critique is to find a different way of representing the above data. While I think the simplicity of the data visualization is effective, I think it also masks important information about the degree to which the infant mortality rate for black girls in Pittsburgh is lower than their non-black peers. There is no imformation provided on the x-axis of about what the middle gray line that denotes the cutoff between "worse than peers" and "better than peers" is actually in reference to. For instance, the mean infant mortality rate could be 2%, with each of the increments away from that line being 0.1 of a percentage point, which could indicate a far smaller different in infant mortality rates than what the visualizing is actually showing. 

Also, the data masks information about what other cities Pittsburgh is being compared against. It would be useful from the readers perspective to know if the comparisons that are being made and the cities that are considered to be "peers" are actually comparable.
Furthermore, the overall comparison in the data is actually about how specifically black women fare in pittsburgh along different livability axes vs their non-black female pairs. It seems like an effective use of color/shape, would be use to the diamond shape to represent pittsburgh and them some red or other distinct color to call out how black women/girls are falling short on that particular metric in the city.

Another thing I notice, because the x-axis dimensions/scale is unclear, is that the subtitle of the graph has to do the job of explaining what the lines actually mean because this is not readly apparent in the visualization. Specifcally, the subtitle is doing a lot of the explanatory work: "Lines indicate range of variation for Pittsburgh's peer cities". I also think that readers tend to look from top to bottom when initially staring at the graph and because the middle line dividing the "worse" and "better" parts of the visual is at the bottom, it takes a few extra seconds to understand what informaiton is being shown on each side ofthe dividing line.

A little confusing at first what the unit/dimension of comparison is -- 
1. At first I thought, is it comparing black women to all other race/gender categories in Pittsburgh? OR is it comparing black women in Pittsburgh to black women in each of the peer cities, and it seems like it may actually be doing both things simultaneously.

Overall, the visualization achieves it's goal of highlighting racial and gender disparties in infant mortality rates but this could be done more effectively and efficiently.  


## Step 3: Wireframe a Solution


## Step 4: Test the Solution


## Step 5: Build Your Solution (Voila!)






### References

[^1]: https://www.politicspa.com/peduto-addresses-racial-equity-criticism-in-first-ad/97795
[^2]: https://www.bloomberg.com/news/articles/2020-01-09/the-best-and-worst-cities-for-black-women)
[^3]: https://apps.pittsburghpa.gov/redtail/images/10645__Pittsburgh's_Inequality_Across_Gender_and_Race_JULY_2020.pdf
