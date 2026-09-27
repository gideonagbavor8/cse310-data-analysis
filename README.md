# Overview

This project demonstrates how software can be used to organize, filter, sort, aggregate, and visualize real-world education data. The goal is to strengthen practical data analysis skills using Python and Pandas while producing useful information from a Ghanaian education dataset.

The dataset used in this project comes from the Ghana Ministry of Education Education Management Information System (EMIS) School Census Tracker. It contains information about schools, including their region, district, census year, school code, school name, school type, and census status.

**Dataset source:** [EMIS Ghana School Census Tracker - Outstanding Schools](https://home.moegh.com/outstanding_schools.php?region=Volta&level=&search=&year=2026)

The purpose of this software is to analyze outstanding schools in Keta Municipal and answer questions about their registration status. The program filters the national dataset to Keta Municipal, counts schools by status, calculates percentages, sorts school names alphabetically, and generates a bar chart.

The analysis focuses on the following questions:

1. How many outstanding schools in Keta Municipal are Public and Private Registered?
2. What percentage of outstanding schools in Keta Municipal are Private Registered and Public?
3. What are the names of the outstanding schools in Keta Municipal, sorted alphabetically?

A demonstration video will show the dataset, the questions and answers, the program running, and a walkthrough of the code.

[Software Demo Video](https://vimeo.com/reviews/ee29ee6a-cd34-4f46-979a-8dbce276228d/videos/1230686695)

# Data Analysis Results

### Question 1

**How many outstanding schools in Keta Municipal are Public and Private Registered?**

The analysis found **25 outstanding schools** in Keta Municipal.

* Private Registered: **17 schools**
* Public: **8 schools**

### Question 2

**What percentage of outstanding schools in Keta Municipal are Private Registered and Public?**

Based on the 25 schools identified:

* Private Registered: **68.0%**
* Public: **32.0%**

### Question 3

**What are the names of the outstanding schools in Keta Municipal, sorted alphabetically?**

The program sorts the school names alphabetically and produces the following list:

1. ABOR SENIOR HIGH TECHNICAL SCHOOL
2. AGORVINU R/C BASIC SCHOOL
3. BEACON OF HOPE MONTESSORI
4. DAYSTAR PREPARATORY SCHOOL, VUI-Dzelukope
5. DESEMMA ACADEMY
6. DIVINE STAR OF THE SEA ACADEMY
7. Divine Bless Academy Complex, Abor
8. GLOBAL EVANGELICAL BASIC SCHOOL, TETTEKOPE
9. GREAT MIND ACADEMY
10. Gethsemane Schools
11. HOPE INTERNATIONAL SCHOOL COMPLEX
12. JESUS CARES PREPARATORY SCHOOL
13. Joy Trinity Academy
14. KEDZI TECHNICAL INSTITUTE
15. KETA BRIGHT FUTURE BASIC SCHOOL
16. KETA BUSINESS COLLEGE
17. KETA SENIOR HIGH TECHNICAL SCHOOL
18. Keta Senior High Technical School
19. MAWUTOR INT. BASIC SCHOOL
20. NYRAVASE COMMUNITY SCHOOL
21. NYRAVASE COMMUNITY SCHOOL
22. SEVA A.M.E ZION BASIC SCHOOL
23. Shalom Academy- Abor Eagle Villa
24. TIANA SUCCESS
25. Vodza R/C Basic School

The analysis uses filtering to select Keta Municipal records, aggregation to count schools by status, data conversion to standardize status values, percentage calculations to compare categories, and sorting to produce the alphabetical school list.

The program also generates a bar chart named `keta_school_status.png` showing the number of schools by status.

# Development Environment

The software was developed using:

* **Visual Studio Code** for writing and managing the Python program.
* **Python** as the programming language.
* **Pandas** for loading, cleaning, filtering, sorting, counting, and analyzing the dataset.
* **Matplotlib** for creating the bar chart.
* **Git** for version control.
* **GitHub** for publishing the project repository.

The project uses a Python virtual environment to manage its dependencies.

The main analysis program is `keta_analysis.py`.

The dataset is stored in:

`data/outstanding_schools_2025.csv`

The generated visualization is stored as:

`keta_school_status.png`

# Useful Websites

* [EMIS Ghana School Census Tracker](https://home.moegh.com/outstanding_schools.php?region=Volta&level=&search=&year=2026)
* [Pandas](https://pandas.pydata.org/)
* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Matplotlib](https://matplotlib.org/)
* [Python](https://www.python.org/)
* [Git Documentation](https://git-scm.com/doc)

# Future Work

* Add analysis for additional districts and regions in Ghana.
* Add more visualizations for comparing school status across districts.
* Improve the handling and reporting of duplicate or inconsistently capitalized school names.
* Allow users to select a district from the program instead of analyzing only Keta Municipal.
* Add additional statistical questions and comparisons as the dataset is explored further.
