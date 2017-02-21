

```python
!pip3 install agate --user
```

    Requirement already satisfied: agate in /usr/local/lib/python3.5/site-packages
    Requirement already satisfied: Babel>=2.0 in /Users/pratheekrebala/Library/Python/3.5/lib/python/site-packages (from agate)
    Requirement already satisfied: six>=1.6.1 in /usr/local/lib/python3.5/site-packages (from agate)
    Requirement already satisfied: parsedatetime>=2.1 in /usr/local/lib/python3.5/site-packages (from agate)
    Requirement already satisfied: pytimeparse>=1.1.5 in /usr/local/lib/python3.5/site-packages (from agate)
    Requirement already satisfied: isodate>=0.5.4 in /usr/local/lib/python3.5/site-packages (from agate)
    Requirement already satisfied: awesome-slugify>=1.6.5 in /usr/local/lib/python3.5/site-packages (from agate)
    Requirement already satisfied: leather>=0.3.2 in /usr/local/lib/python3.5/site-packages (from agate)
    Requirement already satisfied: pytz>=0a in /usr/local/lib/python3.5/site-packages (from Babel>=2.0->agate)
    Requirement already satisfied: future in /usr/local/lib/python3.5/site-packages (from parsedatetime>=2.1->agate)
    Requirement already satisfied: regex in /usr/local/lib/python3.5/site-packages (from awesome-slugify>=1.6.5->agate)
    Requirement already satisfied: Unidecode<0.05,>=0.04.14 in /Users/pratheekrebala/Library/Python/3.5/lib/python/site-packages (from awesome-slugify>=1.6.5->agate)



```python
import agate
```


```python
results = agate.Table.from_csv("mdcounty2014.csv")
print(results)
row = results.rows[0]
row['jurisdiction']
by_county = results.group_by('jurisdiction')
totals = by_county.aggregate([('county_total', agate.Sum('votes'))])
totals = totals.order_by('county_total', reverse=True)
totals.limit(10).print_bars('jurisdiction', 'county_total', width=80)
```

    | column          | data_type |
    | --------------- | --------- |
    | updated_at      | DateTime  |
    | id              | Date      |
    | start_date      | DateTime  |
    | end_date        | DateTime  |
    | election_type   | Text      |
    | result_type     | Text      |
    | special         | Boolean   |
    | office          | Text      |
    | district        | Text      |
    | name_raw        | Text      |
    | last_name       | Boolean   |
    | first_name      | Boolean   |
    | suffix          | Boolean   |
    | middle_name     | Boolean   |
    | party           | Text      |
    | jurisdiction    | Text      |
    | division        | Text      |
    | votes           | Number    |
    | votes_type      | Boolean   |
    | total_votes     | Boolean   |
    | winner          | Boolean   |
    | write_in        | Boolean   |
    | year            | Number    |
    | election_day    | Number    |
    | absentee        | Number    |
    | second_absentee | Number    |
    | provisional     | Number    |
    
    jurisdiction    county_total
    Montgomery         1,954,822 ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
    Baltimore          1,851,809 ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    
    Prince George's    1,501,125 ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░            
    Anne Arundel       1,240,645 ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                   
    Baltimore City       979,608 ▓░░░░░░░░░░░░░░░░░░░░░░░░                          
    Howard               749,280 ▓░░░░░░░░░░░░░░░░░░░                               
    Harford              615,680 ▓░░░░░░░░░░░░░░░                                   
    Frederick            544,177 ▓░░░░░░░░░░░░░░                                    
    Carroll              466,467 ▓░░░░░░░░░░░░                                      
    Charles              328,887 ▓░░░░░░░░                                          
                                 +-----------+------------+------------------------+
                                 0        500,000     1,000,000            2,000,000



```python
by_county = results.group_by('name_raw').group_by('jurisdiction')
totals = by_county.aggregate([('county_total', agate.Sum('votes'))])
totals = totals.order_by('county_total', reverse=True)
totals.print_table()
```

    | name_raw            | jurisdiction    | county_total |
    | ------------------- | --------------- | ------------ |
    | Peter Franchot      | Prince George's |      187,836 |
    | Brian E. Frosh      | Prince George's |      185,658 |
    | Anthony G. Brown    | Prince George's |      184,950 |
    | Peter Franchot      | Montgomery      |      178,855 |
    | Brian E. Frosh      | Montgomery      |      175,892 |
    | Peter Franchot      | Baltimore       |      165,920 |
    | Anthony G. Brown    | Montgomery      |      163,694 |
    | Larry Hogan         | Baltimore       |      155,936 |
    | Brian E. Frosh      | Baltimore       |      135,855 |
    | Larry Hogan         | Anne Arundel    |      119,195 |
    | Peter Franchot      | Baltimore City  |      117,634 |
    | Donna F. Edwards    | Prince George's |      112,224 |
    | Brian E. Frosh      | Baltimore City  |      112,168 |
    | Jeffrey N. Pritzker | Baltimore       |      110,399 |
    | Chris Van Hollen    | Montgomery      |      109,392 |
    | Anthony G. Brown    | Baltimore City  |      106,213 |
    | Anthony G. Brown    | Baltimore       |      102,734 |
    | Larry Hogan         | Montgomery      |       97,312 |
    | Jeffrey N. Pritzker | Anne Arundel    |       94,026 |
    | William H. Campbell | Baltimore       |       92,922 |
    | ...                 | ...             |          ... |



```python

```
