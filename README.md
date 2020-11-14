# Keyword Analysis Model 
Constructed for my MSc dissertation where I achieved a Distinction. The classifier was designed to categorise a large amount of dark web market listings and forum titles to one of 35 predefined codebook categories using keyword analysis algorithms.

## Assumptions
The code will operates under some key assumptions:

- All data is held within .CSV format in their respective folder within the 'data' folder.
- The CSV filenames 0-34 correspond to the categories outlined in cats.txt
- For example, the CSV file named 29-2.csv in data/gt contains the ground truth data for the PGP/GPG category.

## Adding to Ground Truth data (if required)
#### Filename: addFileToGT.py
#### Inputs: data/gt/full.csv
#### Outputs: data/gt/

This step is only required if there is ready sorted data that needs to be added to the ground truth data set.

The Python script will rip the items from the main ground truth data set into the relevant categories. Any duplicates are removed in the process. This prevents certain titles, for example where the same listing has been posted a large number of times being overrepresented. 

## 1. Extracting keywords from ground truth data.
#### Filename: keyword-analysis.py
#### Inputs: data/gt
#### Outputs: data/raw-keywords

The ground truth data is then tokenised.

- All text is treated as lowercase. For instance, 'Wifi' 'WIFI' 'WiFi' 'wifi' are treated as one token ('wifi').
- Numerical tokens are not counted.
- Meaningless tokens such as '...' and ''s' are discounted.
- A few meaningful tokens are also discounted such as 'make' and 'how'. The reasoning for this is that they were causing false positive for the 'Drugs' category during initial testing. There may be scope to potentially remove this once further ground truth data is added.

This will output x35 .CSV files corresponding to each corpus. Each file will contain every word present within that corpus and the number of times it occurs within that corpus.

## 2. Calculation of log likelihood (LL) values.
#### Filename: catKeyword.py
#### Function: calculateLogLikelihood (in addLLValues.py)
#### Inputs: data/raw-keywords
#### Outputs: data/sig-keywords
Log likelihood values are calculated for each word in each corpus.

The logic used to calculate LL has been obtained from [here](http://ucrel.lancs.ac.uk/llwizard.html) as well as the Ryan & Garside article.

Significance is also calculated for each LL value and added to the 'sig' column. The thresholds are taken from the aforementioned website.

## 3. Removal of non-significant keywords.
#### Filename: onlySigKeywords.py
#### Inputs: data/sig-keywords
#### Outputs: data/use-keywords
This simply outputs new CSV files which only contain significant keywords (<0.01). The outputs are generated in the folder 'data/use-keywords/'

The primary aim of this is to make the next stage faster and to prevent any non-significant keywords from being incorrectly utilised in the calculation of a LL score.

## 4. Calculation of a max LL score for each input item.
#### Filename: catKeyword.py
#### Inputs: data/use-keywords
Each item (in the form of a string) is broken down into tokens and for each token, an array is created containing the log-likelihood retrieved for each corpus. 

These values are then summed for each corpus respectively and provided it is above a threshold value, the corpus with the highest value is assigned to the item. If it is below the threshold value, it will be assigned to the 'Other' category.

## Other scripts: Calculating Cohen's kappa
#### Filename: cohens-calculator.py
The last Python script is used to display Cohen's kappa and the percentage of matches for each corpus. These Cohen's kappa statistic provides feedback on general agreement whereas the percentage matches for each corpus allows for a more specific insight into which corpus might need to be improved with additional data.

## Other scripts: Performing k-fold cross-validation analysis
#### Filename: k-analysis.py

The model was cross-validated using k-fold cross validation to ensure it was assigning categories to items with a high degree of accuracy.

