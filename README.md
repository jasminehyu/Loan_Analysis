# Loan Analysis Project
## Overview
This project analyzes loan applications in Wisconsin for the year 2020, focusing on patterns in lending practices. It aims to identify and address potential disparities in loan approvals and interest rates using publicly available data from the Home Mortgage Disclosure Act (HDMA).

Lending discrimination based on factors like race has a long history, and this analysis seeks to bring more transparency to such issues by examining various aspects of the loan applications. The analysis uses data structures, algorithms, and data science techniques to extract insights from a large dataset.

## Features
- Data Analysis: Investigates loan approval rates, interest rates, and other factors influencing lending decisions.
- Data Structures: Implements binary search trees for efficient data retrieval and analysis.
- Predictive Modeling: Develops methods to identify patterns in the dataset.
- Visualization: Provides visual insights into loan distribution, interest rates, and other key metrics.

## Project Structure
- Data Preprocessing: Cleaned and organized the raw loan data for analysis.
- Modules:
   - loans.py: Defines the Loan and Applicant classes to model the dataset.
   - search.py: Implements a binary search tree for fast data retrieval.
- Testing: Used module_tester.py to validate the functionality of different components.
- Visualizations: Created plots to visualize patterns in loan approvals, interest rates, and applicant demographics.

## Results
- Interest Rate Trends: Found variations in interest rates among different banks, identifying trends and potential biases.
- Loan Applicant Insights: Highlighted the demographics of loan applicants, including age distribution and racial identities.
- Data Structure Efficiency: Demonstrated the efficiency of binary search trees for analyzing large datasets.

## Usage
To explore the project, download the repository and run the Jupyter Notebook (mp2.ipynb) to see the data analysis in action. The project files include:
- mp2.ipynb: Main analysis notebook.
- loans.py: Defines the data models.
- search.py: Implements the search tree.
- module_tester.py: Contains tests for the modules.
  
1. Clone the repository:
```bash
git clone https://github.com/yourusername/loan-analysis-project.git
```
2. Navigate to the project directory and run the Jupyter Notebook:
```bash
jupyter notebook mp2.ipynb
```
