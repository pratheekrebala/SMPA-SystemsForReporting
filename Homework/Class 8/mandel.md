### Make the Table
`CREATE  TABLE "main"."mandel" ("payee" VARCHAR, "purpose" VARCHAR, "city" VARCHAR, "state" VARCHAR, "zip" VARCHAR, "amount" INTEGER, "month" INTEGER, "day" INTEGER, "year" INTEGER)`

### Rows with no state
`SELECT * FROM mandel WHERE state = ' ';`

### Totals by state
`SELECT state, sum(amount) from mandel GROUP BY state`

### Totals by purpose
`SELECT purpose,sum(amount) as amt FROM mandel GROUP BY purpose ORDER BY amt DESC;`

### All Direct Mailing expenses.
`SELECT * FROM mandel WHERE purpose LIKE '%DIRECT%'`

### Total by Month-Year
`SELECT month,year,sum(amount) as total FROM mandel GROUP BY month,year ORDER BY total DESC`

### Total by Payee
`SELECT payee,sum(amount) as total FROM mandel where purpose == 'PAYROLL' GROUP BY payee ORDER BY total DESC`