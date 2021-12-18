# Lab Sheet

![[Lab 6 Working with a Twitter time line using SQL.pdf]]

# Answers

1) 
```sql
SELECT * FROM Epipen_new1 WHERE retweets > 12;
```
2) 
```sql
SELECT REALNAME FROM Epipen_new1 WHERE SCREENNAME LIKE REALNAME;
```
3) 
```sql
SELECT REALNAME FROM Epipen_new1 WHERE(SCREENNAME LIKE REALNAME) AND LINKURL IS NULL;
```
4) 
```sql
SELECT TWEET FROM Epipen_new1 WHERE TWEET LIKE "%#%";
```
5) This query gave me back a number of 1029:
```sql
SELECT count(TWEET) FROM Epipen_new1 WHERE TWEET LIKE "%#%";
```

6) 
```sql
SELECT DISTINCT SENTPOS, count(SENTPOS) FROM Epipen_new1 GROUP BY SENTPOS;
```
7) 19
8) 
```sql
SELECT DISTINCT count(TWEET) FROM Epipen_new1 WHERE SENTNET IS 0;
```
9) 1554

